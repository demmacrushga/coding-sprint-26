//console.log('Hello World');
//let, const, always use const unless you know you are going to reassign the value 
//string, numbers, boolean, null, undefined
//Arrays are variables that hols multiple values 

/*const name = 'John';
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


const x = 11; 

const color = x > 10 ? 'red' : 'blue';

switch(color) {
    case 'red':
        console.log('color is red');
        break;
    case 'blue':
        console.log('color is blue');
        break;
    default:
        console.log('color is neither red or blue')
}


function addNums(num1, num2){
    return(num1 + num2);
}

console.log(addNums(5,4));
//OR you can use 

function addNum(num3=3, num4=6) {
    return(num3 + num4);
}
console.log(addNum); */

//Constructor function 
function Person(firstname, lastname, dob) {
    this.firstname = firstname;
    this.lastname = lastname;
    this.dob = dob;
    this.getBirthYear = function(){
        return this.dob.getFullYear();
    }
    this.getFullName = function() {
        return `${this.firstname} ${this.lastname}`;
    }
}

//Instantiate object 
const person1 = new Person('Jane', 'Doe', '4-3-1980');
const person2 = new Person('Kurt', 'Weller', '3-4-1990')

console.log(person1);
console.log(person2.firstname);
console.log(person1.getFullName);
console.log(person1.getBirthYear);