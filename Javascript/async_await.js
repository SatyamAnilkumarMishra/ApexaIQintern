function getData() {
    return new Promise(function(resolve) {
        setTimeout(function() {
            resolve("Data loaded");
        }, 1000);
    });
}

async function showData() {
    let data = await getData();
    console.log(data);
}

showData();
