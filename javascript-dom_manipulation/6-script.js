#!/usr/bin/node
const char_name = document.getElementById('character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    char_name.textContent = data.name;
    });
