let arr2 = [1, 2, 3];

// push
arr2.push(4);

// pop
arr2.pop();

// shift
arr2.shift();

// unshift
arr2.unshift(0);

// map
let squared = arr2.map(x = x * x);

// filter
let filtered = arr2.filter(x = x > 1);

// reduce
let sum = arr2.reduce((acc, val) = acc + val, 0);

// find
let found = arr2.find(x => x === 2);

// includes
console.log(arr2.includes(2));

// slice
console.log(arr2.slice(1, 3));

// splice
arr2.splice(1, 1);

console.log("Array Methods:", arr2, squared, filtered, sum, found);