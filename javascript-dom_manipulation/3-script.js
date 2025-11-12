#!/usr/bin/node
const header = document.querySelector('header');
const redHeaderButton = document.getElementById('toggle_header');
redHeaderButton.addEventListener('click', function () {
 if (header.classList. contains('red')) {
   header.classList.remove('red');
   header.classList.add('green');
 } else {
   header.classList.remove('green');   
   header.classList.add('red');
 }
});

