#!/usr/bin/node
async function change () {
  const char = document.querySelector('#character');
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const data = await response.json();
  char.innerHTML = data.name;
}
change();
