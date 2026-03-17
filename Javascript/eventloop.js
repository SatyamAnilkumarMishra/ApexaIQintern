console.log("Start");

setTimeout(function() {
    console.log("Timeout");
}, 0);

Promise.resolve().then(function() {
    console.log("Promise");
});

console.log("End");