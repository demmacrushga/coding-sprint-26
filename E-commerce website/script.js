// ------Menu Toggle------
var MenuItems = document.getElementById("MenuItems");
MenuItems.style.maxHeight = "0px";

function menutoggle() {
    if (MenuItems.style.maxHeight == "0px") {
        MenuItems.style.maxHeight = "200px";
    } else {
        MenuItems.style.maxHeight = "0px";
    }
}

// ------Product Gallery (only runs on product page)------
var ProductImg = document.getElementById("ProductImg");
var SmallImg = document.getElementsByClassName("small-img");

if (ProductImg && SmallImg.length > 0) {
    SmallImg[0].onclick = function () { ProductImg.src = SmallImg[0].src; }
    SmallImg[1].onclick = function () { ProductImg.src = SmallImg[1].src; }
    SmallImg[2].onclick = function () { ProductImg.src = SmallImg[2].src; }
    SmallImg[3].onclick = function () { ProductImg.src = SmallImg[3].src; }
}

// ------Login/Register Toggle------
var LoginForm = document.getElementById("LoginForm");
var RegForm = document.getElementById("RegForm");
var Indicator = document.getElementById("Indicator");

function login() {
    LoginForm.style.transform = "translateX(0px)";
    RegForm.style.transform = "translateX(300px)";
    Indicator.style.transform = "translateX(0px)";
}

function register() {
    LoginForm.style.transform = "translateX(-300px)";
    RegForm.style.transform = "translateX(0px)";
    Indicator.style.transform = "translateX(100px)";
}