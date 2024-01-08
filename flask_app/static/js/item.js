// ======================== COUNTER =========================


var decrease = document.getElementById("minus");
var increase = document.getElementById("plus");
const countNum = document.getElementById("count");
const inputValue = document.getElementsByTagName("input");
const label = document.querySelector(".count_num");
let count = 0;

function increaseBtn(){
    count++;
    label.innerText = count;
}

function decreaseBtn(){
    count--;
    label.textContent = count;

}