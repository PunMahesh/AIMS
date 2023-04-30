const profileBar = document.querySelector(".profile-bar");
const sideBar = document.querySelector(".sidebar");
if (profileBar) {
    profileBar.remove();
}
if (sideBar) {
    sideBar.remove();
}

document.getElementById("go-back").addEventListener("click", () => {
    window.history.back();
});

const redirect = () => {
    const referrer = document.referrer;
    const redirectTimerElem = document.getElementById("redirect-timer");
    if (!referrer) {
        redirectTimerElem.remove();
        return;
    }

    var timeLeft = 5;
    var redirectTimer = setInterval(function(){
        if(timeLeft <= 0){
            clearInterval(redirectTimer);
            window.location.href = referrer;
        }
        document.getElementById("show-seconds").textContent = timeLeft;
        timeLeft -= 1;
    }, 1000);
}
redirect();
