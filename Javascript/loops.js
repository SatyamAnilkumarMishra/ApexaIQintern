// for loop
for (let i = 0; i < 3; i++) {
    console.log("For loop:", i);
}

// while loop
let i = 0;
while (i < 3) {
    console.log("While loop:", i);
    i++;
}

// do-while loop
let j = 0;
do {
    console.log("Do While:", j);
    j++;
} while (j < 3);

// for...of (arrays)
let nums = [10, 20, 30];
for (let val of nums) {
    console.log("For of:", val);
}

// for...in (objects)
let person = { name: "Satyam", age: 20 };
for (let key in person) {
    console.log("For in:", key, person[key]);
}