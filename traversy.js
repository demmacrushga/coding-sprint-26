//console.log('Hello World');
//let, const, always use const unless you know you are going to reassign the value 
//string, numbers, boolean, null, undefined
//Arrays are variables that hols multiple values 

const name = 'John';
const age = 30;
const isCool = true;
const rating = 4.5;
const x = null;
const y = undefined;

console.log('My name is ' + name + ' and I am ' + age);
console.log(`My name is ${name} and I am ${age}`);//works only inside backticks(template literals)

const fruits = ['apples', 'oranges', 'pears'];

console.log(fruits[10]); 

const person = {
    firstname : 'Edith',
    lastname : 'Dziwornu',
    age : 30,
    hobbies : ['music', 'movies', 'sports'],
    address: {
        street: 'tea street',
        city: 'Tema',
        state: 'Tema'
    }
}

console.log(person.hobbies[1]);  
const todos = [
    {
        id: 1, 
        text: 'Take out trash',
        isCompleted: true
    },
    {
        id: 2,
        text: 'Meeting with boss',
        isCompleted: true
    },
    {
        id: 3, 
        text: 'Dentist appointment', 
        isCompleted:false
    }
];

console.log(todos[1].text)  

const todoJSON = JSON.stringify(todos);
console.log(todoJSON);

//forEach, map, filter 
const todoCompleted = todos.filter(function(todo) {
    return todo.isCompleted ===true;
}).map(function(todo) {
    return todo.text;

})

console.log(todoCompleted) 


