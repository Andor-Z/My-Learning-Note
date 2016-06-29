// var my_heading = document.querySelector('h1');
// my_heading.innerHTML = 'Hello world!';
// document.querySelector('html').onclick = function(){
//     alert('click');
// };

var my_image = document.querySelector('img');
my_image.onclick = function(){
    var mySrc = my_image.getAttribute('src');
    if(mySrc === 'images/firefox-icon.png'){
        my_image.setAttribute('src', 'images/0.jpg');
    } else {
        my_image.setAttribute('src', 'images/firefox-icon.png')
    }
}

var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName(){
    var myName = prompt('Please enter your name:');
    localStorage.setItem('name', myName);
    myHeading.innerHTML = myName + 'is cool!';
}

if(!localStorage.getItem('name')){
    setUserName();
}else {
    var storedName = localStorage.getItem('name');
    myHeading.innerHTML = storedName + 'is coll!';
}

myButton.onclick = function(){
    setUserName();
}