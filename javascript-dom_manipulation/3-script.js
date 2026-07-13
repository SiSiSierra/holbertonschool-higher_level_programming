function toggle () {
  const h = document.querySelector('header');
  if (h.className === 'green') {
    h.className = 'red';
  } else if (h.className === 'red') {
    h.className = 'green';
  }
}
const d = document.querySelector('#toggle_header');
d.addEventListener('click', toggle);
