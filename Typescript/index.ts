/*Typescript has data types like any, unkwown, never, enum, tuple
You can separate very long digits with underscores
Tuples are usually used with two variables
*/


// 1. Explicitly type 'level' to avoid the 'any' warning
let sales = 123_456_789;
let course: string = 'Typescript';
let is_published: boolean = false;
let level: number;

// 2. PascalCase is standard for Enum members
enum Size { Small, Medium, Large };
let mySize: Size = Size.Medium; // Assigning it so it's not "unused"

// 3. Keep the logic, but we will log the result below
function calculateTax(income: number, taxYear: number): number {
    if (taxYear > 2022)
        return income * 1.2;
    return income * 1.3;
}

// 4. Wrap the call in console.log so the result is actually seen
console.log(calculateTax(10_000, 2022));

// 5. Renamed to 'employee' (singular) since it's one person
let employee: {
    readonly id: number;
    name: string;
    retire: (date: Date) => void
} = {
    id: 1,
    name: 'Edith',
    retire: (date: Date) => {
        console.log(date);
    }
};

console.log(employee);