/*** 
	Copyright 2019, Nathan Lecompte 
		ID: 45423725
***/

// Handle menu button click on mobile
document.getElementsByClassName('menu-button')[0].onclick = function() {
    if(window.innerWidth<800) {
        let menu = document.getElementsByTagName('nav')[0];
        menu.style.height = (menu.style.height != '270px') ? '270px' : 0;
        menu.style.padding = (menu.style.padding != '20px') ? '20px' : '0 20px 0';
    }
};

// Handle menu hide for unfocus tap on mobile
document.getElementsByTagName('main')[0].onclick = function() {
    if(window.innerWidth<800) {
        let menu = document.getElementsByTagName('nav')[0];
        menu.style.height = 0;
        menu.style.padding = '0 20px 0';
    }
};

// Handle menu hide for resize on mobile
window.onresize = function() {
    // Enable back button if needed
    let menu = document.getElementsByTagName('nav')[0];
    if(window.innerWidth<800) {
        menu.style.height = 0;
        menu.style.padding = '0 20px 0';
    } else {
        menu.style.transform = '';
        menu.style.height = '';
        menu.style.padding = '';
    }
}