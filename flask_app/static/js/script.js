const checkBox = document.querySelector(".nav_toggle_label");
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
        element.classList.toggle("dark_mode");
    }


