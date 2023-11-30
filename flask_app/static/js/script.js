
const mainTitle = document.querySelector('.main_title');
const matchaLogo = document.querySelector('.matcha_logo');


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


    function darkMode(){
        const element = document.body;
        const inputs = document.querySelectorAll(".input_class");
        element.classList.toggle("dark_mode");
        inputs.classList.toggle("input_dark_mode");
    }