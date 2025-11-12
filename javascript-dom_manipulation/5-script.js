#!/usr/bin/node
const text_header = document.querySelector('header');
const updateButton = document.getElementById('update_header');
updateButton.addEventListener('click', function () {
    text_header.textContent = 'New Header!!!';
});
