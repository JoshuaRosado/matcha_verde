
// ======================================
// FUNC to HAVE ONE DETAILS TAG OPEN AT A TIME

if (document.querySelector('details')) {
    const details = document.querySelectorAll('details');

    details.forEach((targetDetail) => {
        targetDetail.addEventListener("click", () => {
            // CLOSE ALL DETAILS THAT ARE NOT TARGET BY THE USER(targetDetail)
            // FOR EACH DETAILS
            details.forEach((detail) => {
                // THAT IS NOT OPENED OR TARGET
                if (detail !== targetDetail) {
                    // CLOSE TAG
                    detail.removeAttribute("open");
                }
            });
        });
    });
}
// ======================================

// ====== landing page title anim ======
var mainTitle = document.querySelector('.main_title');
var matchaLogo = document.querySelector('.matcha_logo');
    function TitleColorAnim(){
        mainTitle.classList.add("main_title_anim");
    }

    function removeTitleColorAnim(){
        mainTitle.classList.remove("main_title_anim");
    }

    function logoTranslation(){
        matchaLogo.classList.add("matcha_logo_click");
        mainTitle.classList.add("main_title_anim");
    }


    // ======================SLIDESHOW ARROW's FUNCTION=========================================

let slider = document.querySelectorAll(".slide"),
leftArrow = document.querySelector(".left_arrow"),
rightArrow = document.querySelector(".right_arrow"),
current = 0

    // function fadeSlides(){
    //     slider.classList.add("fade_in");
    // }

    // RESET FUNC
    function reset(){
        for (let i = 0; i < slider.length; i++) {
            slider[i].style.display = "none";
        }
    }

    function startSlide(){
        reset();
        slider[0].style.display = "block";
    }

    function slidePrev(){
        reset();
        slider[current - 1].style.display = "block";
        slider[current - 1].classList.add('fade_in');
        current--;
    }

    function slideNext(){
        reset();
            slider[current + 1].style.display = "block";
            slider[current + 1].classList.add('fade_in');
            current++;
    }
    leftArrow.addEventListener("click", function(){
        if (current === 0 ){
            current = slider.length;
        }
        slidePrev();
    });

    rightArrow.addEventListener("click", function()  {
        if (current === slider.length - 1){
            current = -1
        }
        slideNext();
    });


// =============== AUTO SLIDE EVERY 5s =======================

    setInterval(function() {
        if (current === slider.length -1){
            current = -1
        }
        slideNext()
    }, 6000);
// ==========================================================


startSlide();

    




// ==================================================================
    // function darkMode(){
    //     const element = document.body;
    //     element.classList.toggle("dark_mode");
    // }



    let count = 0;

//  BUG IN THE SHOPPING BAG DROPDOWN WINDOW
    function plusBtn(a, b) {
        var input = b.previousElementSibling;
        var value = parseInt(input.value, 10);
        value = isNaN(value) ? 0 : value;
        value++;
        input.value = value;
    }
    
    function minusBtn(a, b) {
        var input = b.nextElementSibling;
        var value = parseInt(input.value, 10);
        if (value > 1) {
        value = isNaN(value) ? 0 : value;
        value--;
        input.value = value;
        }
    }