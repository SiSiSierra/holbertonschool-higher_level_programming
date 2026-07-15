#!/usr/bin/node
function addLi () {
  const parent = document.getElementsByClassName('my_list')[0];
  const li = document.createElement('li');
  li.innerHTML = 'Item';
  parent.appendChild(li);
}
document.querySelector('#add_item').addEventListener('click', addLi);
