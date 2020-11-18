const form = document.querySelector(".js-form");
const input = form.document.querySelector("input");
const greeting = document.querySelector(".js-greetings");
const User_LS = "currentUser";
const SHOWING_CN = "showing";

function paintGreeting(text) {
    form.classList.remove(SHOWING_CN);
    greeting.innerText = `Hello ${text}`;
    greeting.classList.add(SHOWING_CN);
}

function loadName() {
    const currentUser = localStorage.getItem(User_LS);
    if(currentUser == ull) {

    } else {
        paintGreeting(currentUser);
    }
}

function init() {
    loadName();
}

init();