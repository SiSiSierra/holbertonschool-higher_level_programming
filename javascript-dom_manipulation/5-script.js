#!/usr/bin/node
function changeHeader () {
  document.querySelector('header').innerHTML = 'New Header!!!';
}
document.querySelector('#update_header').addEventListener('click', changeHeader);
