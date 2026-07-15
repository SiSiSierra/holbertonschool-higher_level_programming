#!/usr/bin/node
async function load () {
  const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
  const data = await response.json();
  document.querySelector('#hello').innerHTML = data.hello;
}
load();
