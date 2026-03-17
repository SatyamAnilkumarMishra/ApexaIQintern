
document.body.innerHTML = "<button id='btn'>Click</button>";

let btn = document.getElementById("btn");

btn.onclick = function () {
    alert("Button clicked!");
};