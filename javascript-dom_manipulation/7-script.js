#!/usr/bin/node
async function load () {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const movies = await response.json();
  const list = document.querySelector('#list_movies');
  for (let i = 0; i < movies.results.length; i++) {
    const div = document.createElement('div');
    div.innerHTML = movies.results[i].title;
    list.appendChild(div);
  }
}
load();
