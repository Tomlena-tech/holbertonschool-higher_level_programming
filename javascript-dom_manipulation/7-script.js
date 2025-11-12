#!/usr/bin/node
const movies_name = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        data.results.forEach(movie => {
            const listTitles = document.createElement('li');
            listTitles.textContent = movie.title;
            movies_name.appendChild(listTitles);
        });
    });

