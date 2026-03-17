// normal function
function greet(name) {
    return "Hello " + name;
}
console.log(greet("Bro"));

// function expression
const add = function(a, b) {
    return a + b;
};
console.log("Add:", add(2, 3));

// arrow function
const multiply = (a, b) => a * b;
console.log("Multiply:", multiply(3, 4));

// default parameter
function sayHi(name = "Guest") {
    console.log("Hi", name);
}
sayHi();

// callback function
function processUser(callback) {
    console.log("Processing...");
    callback();
}
processUser(() => console.log("Callback executed"));