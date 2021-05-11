const menuBtn = document.querySelector('.menu-btn');
// const bg = document.querySelector('.bg');
const yellow = document.querySelector('.navyellow');
// const nav1 = document.querySelector('.nav-1');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if(!menuOpen) {
        // bg.classList.add('is-active');
        yellow.classList.add('is-active');
        // nav1.classList.add('is-active');
        menuBtn.classList.add('open');
        menuOpen = true;
    }
    else {
        // bg.classList.remove('is-active');
        yellow.classList.remove('is-active');
        // nav1.classList.remove('is-active');
        menuBtn.classList.remove('open');
        menuOpen=false;
    }
});