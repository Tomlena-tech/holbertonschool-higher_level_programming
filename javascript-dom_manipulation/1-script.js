#!/usr/bin/node
const header = document.querySelector('header');
const redHeaderButton = document.getElementById('red_header');
redHeaderButton.addEventListener('click', () => {header.style.color = '#FF0000';});
