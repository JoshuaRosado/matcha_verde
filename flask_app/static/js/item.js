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
// =============================================================
// ======================== STAR RATING =========================

const stars = document.querySelectorAll(".stars i");


stars.forEach((star, index1) => {
    // event added when star is clicked
    star.addEventListener("click", () => {
        stars.forEach((star, index2) => {
            // add the class to the star clicked and any stars lower index
            // remove class from any stars higher index
            index1 >= index2 ? star.classList.add("active") : star.classList.remove("active")
        });
    });
});
// =============================================================