var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");

function opentab(e, tabname) {
    for (let tablink of tablinks) {
        tablink.classList.remove("active-link");
    }
    for (let tabcontent of tabcontents) {
        tabcontent.classList.remove("active-tab");
    }
    // Change 'event' to 'e' here
    e.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");
}

var sidemenu = document.getElementById("sidemenu");

function openmenu() {
    sidemenu.style.right = "0";
}

function closemenu() {
    sidemenu.style.right = "-200px";
}

const scriptURL = 'https://script.google.com/macros/s/AKfycbwmALCmCu8jkOHjXlhoh3GcSHoQdia1JtqvF34hmmhT8Lo0QHiuhWEXiG3gmceYqkTKrg/exec';
// Make sure this matches your HTML <form name="...">
const form = document.forms['submit-to-google-sheet']; 
const msg = document.getElementById("msg");

form.addEventListener('submit', e => {
    e.preventDefault();
    fetch(scriptURL, { method: 'POST', body: new FormData(form), mode: 'no-cors' })
        .then(() => {
            msg.innerHTML = "Message sent successfully ✓";
            setTimeout(function() {
                msg.innerHTML = "";
            }, 5000);
            form.reset();
        })
        .catch(error => console.error('Error!', error.message));
});