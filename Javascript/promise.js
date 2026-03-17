let promise = new Promise(function(resolve, reject) {
    resolve("Done!");
});

promise.then(function(result) {
    console.log(result);
});