#Preparing two text datasets (users + tasks), showing them, and saving as CSV
import pandas as pd

# --- Sample user profiles (edit if you want different examples) ---
sample_users = [
    ("U1", ["python", "nlp", "tensorflow", "pandas", "data cleaning"]),
    ("U2", ["sql", "excel", "reporting", "powerpoint"]),
    ("U3", ["javascript", "react", "css", "html"]),
    ("U4", ["python", "flask", "api", "docker", "aws"]),
    ("U5", ["r", "statistics", "ggplot2", "data visualization"])
]

# Sample task descriptions 
sample_tasks = [
    ("T1", "Build an NLP pipeline using Python and TensorFlow to preprocess text and train a model"),
    ("T2", "Create a dashboard with Excel to show monthly sales reports"),
    ("T3", "Implement responsive UI components in React and style them with CSS"),
    ("T4", "Deploy a Flask REST API to AWS using Docker"),
    ("T5", "Perform statistical analysis and visualizations in R for survey data"),
    ("T6", "Clean and preprocess data using pandas before training a model")
]

# Converting user skills lists into comma-joined strings for CSV/storage
df_users = pd.DataFrame([{"user_id": uid, "skills": ", ".join(skills)} for uid, skills in sample_users])
df_tasks = pd.DataFrame([{"task_id": tid, "description": desc} for tid, desc in sample_tasks])

# Displaying to console
print("=== Users ===")
print(df_users.to_string(index=False))
print("\n=== Tasks ===")
print(df_tasks.to_string(index=False))

# Save CSV files in current working directory
users_csv = "assignment3_users.csv"
tasks_csv = "assignment3_tasks.csv"
df_users.to_csv(users_csv, index=False)
df_tasks.to_csv(tasks_csv, index=False)
print(f"\nSaved users -> {users_csv}")
print(f"Saved tasks -> {tasks_csv}")

print(f"\n#users = {len(df_users)}, #tasks = {len(df_tasks)}")



#Preprocessing function 
import re
import pandas as pd

def preprocess_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)   # remove punctuation (keep letters/numbers/spaces)
    text = re.sub(r'\s+', ' ', text).strip()   # collapse extra spaces
    return text

# Quick test using the CSVs 
df_users = pd.read_csv("assignment3_users.csv")
df_tasks = pd.read_csv("assignment3_tasks.csv")

example_user_raw = df_users.loc[0, 'skills']
example_task_raw = df_tasks.loc[0, 'description']
example_user_pre = preprocess_text(example_user_raw)
example_task_pre = preprocess_text(example_task_raw)

print("User raw:   ", example_user_raw)
print("User pre:   ", example_user_pre)
print()
print("Task raw:   ", example_task_raw)
print("Task pre:   ", example_task_pre)



#TF-IDF top-k keywords for a user-task pair
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

#Loading CSVs and take first pair
df_users = pd.read_csv("assignment3_users.csv")
df_tasks = pd.read_csv("assignment3_tasks.csv")

user_raw = df_users.loc[0, 'skills']
task_raw = df_tasks.loc[0, 'description']

user_text = preprocess_text(user_raw)
task_text = preprocess_text(task_raw)

print("User (pre):", user_text)
print("Task (pre):", task_text)

def top_k_keywords_pair(user_text: str, task_text: str, k: int = 5):
    vec = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    X = vec.fit_transform([user_text, task_text])
    features = np.array(vec.get_feature_names_out())
    def top_k(row_idx):
        row = X[row_idx].toarray().ravel()
        if row.sum() == 0:
            return []
        idx = np.argsort(row)[-k:][::-1]
        return features[idx].tolist()
    return top_k(0), top_k(1)

user_kw, task_kw = top_k_keywords_pair(user_text, task_text, k=5)
print("\nTop keywords (user):", user_kw)
print("Top keywords (task):", task_kw)


#Implementing match_score and computing full user×task matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

# match_score which returns score and top keywords
def match_score(user_skills, task_description, top_k_keywords=5, mode='tfidf'):
    # prepare texts
    if isinstance(user_skills, list):
        user_text = preprocess_text(" ".join(user_skills))
    else:
        user_text = preprocess_text(user_skills)
    task_text = preprocess_text(task_description)

    # keywords using pairwise TF-IDF
    try:
        user_kw, task_kw = top_k_keywords_pair(user_text, task_text, k=top_k_keywords)
    except Exception:
        user_kw = user_text.split()[:top_k_keywords]
        task_kw = task_text.split()[:top_k_keywords]

    # TF-IDF vectors for the pair and cosine similarity
    V = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    Xp = V.fit_transform([user_text, task_text])
    v_user = Xp[0].toarray()
    v_task = Xp[1].toarray()

    if np.linalg.norm(v_user) == 0 or np.linalg.norm(v_task) == 0:
        score = 0.0
    else:
        score = float(cosine_similarity(v_user, v_task)[0,0])

    return {"score": round(score, 6), "method": "tfidf", "user_keywords": user_kw, "task_keywords": task_kw}

# Quick single test
df_users = pd.read_csv("assignment3_users.csv")
df_tasks = pd.read_csv("assignment3_tasks.csv")
res = match_score(df_users.loc[0,'skills'], df_tasks.loc[0,'description'], top_k_keywords=5)
print("Single-pair match_score result (first user vs first task):")
print(res)

# Showing full user×task matrix
rows = []
for _, row_u in df_users.iterrows():
    uid = row_u['user_id']
    skills = row_u['skills']
    for _, row_t in df_tasks.iterrows():
        tid = row_t['task_id']
        desc = row_t['description']
        r = match_score(skills, desc, top_k_keywords=5)
        rows.append({
            "user_id": uid,
            "task_id": tid,
            "tfidf_score": r['score'],
            "user_keywords": "; ".join(r['user_keywords']),
            "task_keywords": "; ".join(r['task_keywords'])
        })

df_matches = pd.DataFrame(rows)
print("\nHead of user-task match matrix:")
print(df_matches.head(12).to_string(index=False))

#Saving CSV
out_csv = "assignment3_match_scores_user_task_tfidf.csv"
df_matches.to_csv(out_csv, index=False)
print("\nSaved full matrix to:", out_csv)



import pandas as pd
df = pd.read_csv("assignment3_match_scores_user_task_tfidf.csv")
best = df.sort_values(['task_id','tfidf_score'], ascending=[True, False]).groupby('task_id').first().reset_index()
print(best.to_string(index=False))



#Matching embeddings 
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

print("Loading model 'all-MiniLM-L6-v2' (may take ~30–90s first run)...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded.")

#Loading CSVs
df_users = pd.read_csv("assignment3_users.csv")
df_tasks = pd.read_csv("assignment3_tasks.csv")

#Computing embeddings and pairwise scores
rows = []
for _, ru in df_users.iterrows():
    uid = ru['user_id']
    skills = preprocess_text(ru['skills'])      # use your preprocess_text
    for _, rt in df_tasks.iterrows():
        tid = rt['task_id']
        desc = preprocess_text(rt['description'])
        emb_u = model.encode([skills], convert_to_numpy=True)
        emb_t = model.encode([desc], convert_to_numpy=True)
        score = float(cosine_similarity(emb_u, emb_t)[0, 0])
        rows.append({"user_id": uid, "task_id": tid, "emb_score": round(score, 4)})

df_emb = pd.DataFrame(rows)

#best user per task
best_emb = df_emb.sort_values(['task_id', 'emb_score'], ascending=[True, False]) \
                 .groupby('task_id').first().reset_index()

print("\n=== Best User per Task (Embeddings) ===")
print(best_emb.to_string(index=False))

#Saving full results
out_emb = "assignment3_match_scores_user_task_embeddings.csv"
df_emb.to_csv(out_emb, index=False)
print("\nSaved:", out_emb)

