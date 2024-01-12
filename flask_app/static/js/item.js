// ======================== IMG SELECTION FUNCTION =========================
let mainImg = document.getElementById("main_img");
let smallImg = document.querySelectorAll(".small_img");

smallImg[0].onclick = function(){
    mainImg.src = smallImg[0].src;
}
smallImg[1].onclick = function(){
    mainImg.src = smallImg[1].src;
}
smallImg[2].onclick = function(){
    mainImg.src = smallImg[2].src;
}
smallImg[3].onclick = function(){
    mainImg.src = smallImg[3].src;
}
smallImg[4].onclick = function(){
    mainImg.src = smallImg[4].src;
}




// =======================================================================
// ======================== COUNTER =========================


let count = 0;


function increaseBtn(a, b) {
    var input = b.previousElementSibling;
    var value = parseInt(input.value,10);
    value = isNaN(value) ? 0 : value;
    value++;
    input.value = value;
}

function decreaseBtn(a, b) {
    var input = b.nextElementSibling;
    var value = parseInt(input.value, 10);
    if (value > 1) {
    value = isNaN(value) ? 0 : value;
    value--;
    input.value = value;
    }
zź}
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