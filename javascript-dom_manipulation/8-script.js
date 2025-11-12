#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
    const value_hello = document.getElementById('hello');
fetch ('https://hellosalut.stefanbohacek.com/?lang=fr')
.then(response => response.json())
.then(data => value_hello.textContent = data.hello)
})
