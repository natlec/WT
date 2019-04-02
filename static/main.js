/*** 
	Copyright 2019, Nathan Lecompte 
		ID: 45423725
***/

window.onload = function() {
    // Enable back button if needed
    if(document.referrer.indexOf('127.0.0.1:8010') > -1 && history.length > 0) {
        document.getElementsByClassName('home-button')[0].classList.add('back-button');
    } else {
        document.getElementsByClassName('home-button')[0].classList.remove('back-button');
    }
}

// Handle back button click
document.getElementsByClassName('home-button')[0].onclick = function() {
    if(document.referrer.indexOf('127.0.0.1:8010') > -1 && history.length > 0) {
        window.history.back();
    }
};

// Handle menu button click on mobile
document.getElementsByClassName('menu-button')[0].onclick = function() {
    if(window.innerWidth<800) {
        let menu = document.getElementsByTagName('nav')[0];
        menu.style.top = (menu.style.top != '80px') ? '80px' : '50px';
        menu.style.height = (menu.style.height != '270px') ? '270px' : 0;
        menu.style.padding = (menu.style.padding != '10px 20px 20px') ? '10px 20px 20px' : '0 20px 0';
    }
};

// Handle menu hide for unfocus tap on mobile
document.getElementsByTagName('main-button')[0].onclick = function() {
    if(window.innerWidth<800) {
        let menu = document.getElementsByTagName('nav')[0];
        menu.style.top = '50px';
        menu.style.height = 0;
        menu.style.padding = '0 20px 0';
    }
};

// Handle menu hide for resize on mobile
window.onresize = function() {
    // Enable back button if needed
    let menu = document.getElementsByTagName('nav')[0];
    if(window.innerWidth<800) {
        menu.style.top = '50px';
        menu.style.height = 0;
        menu.style.padding = '0 20px 0';
    } else {
        menu.style.top = '';
        menu.style.height = '';
        menu.style.padding = '';
    }
}