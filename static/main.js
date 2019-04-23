/*** 
	Copyright 2019, Nathan Lecompte 
		ID: 45423725
***/

// Mobile menu navigation
var menu = document.querySelector('nav');

// Function to hide mobile menu
function hideMenu() {
    if(window.innerWidth < 800) {
        menu.style.height = 0;
        menu.style.padding = '0 20px 0';
    } else {
        menu.style.transform = '';
        menu.style.height = '';
        menu.style.padding = '';
    }
};

// Handle menu hide/reset for window resize
window.onresize = function() { hideMenu() };

if(window.innerWidth < 800) {
    // Handle menu button click
    document.querySelector('.menu-button').onclick = function() {
        menu.style.height = (menu.style.height != '270px') ? '270px' : 0;
        menu.style.padding = (menu.style.padding != '20px') ? '20px' : '0 20px 0';
    };

    // Handle mobile menu hide on scroll or page tap
    document.querySelector('main').onclick = function() { hideMenu() };
    window.onscroll = function() { hideMenu() };
    document.body.ontouchmove = function() { hideMenu() };
}