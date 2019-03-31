/*** 
	Copyright 2019, Nathan Lecompte 
		ID: 45423725
***/

// Handle menu button click on mobile
document.getElementsByClassName('menu')[0].onclick = function() {
    let menu = document.getElementsByTagName('nav')[0];
    menu.style.display = (menu.style.display != 'block') ? 'block' : 'none';
};