
// Activate Bootstrap's tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// Fix navigation to the top on scroll.
var nav = document.querySelector(".navbar")
var brand = document.querySelector(".navbar-brand")
var navTop = nav.offsetTop
var isFixed = 0
window.onscroll = function (event) {
  if (window.scrollY >= navTop && !isFixed) {
    isFixed = 1
    nav.classList.add('fixed-top');
    nav.classList.remove("rounded-3", "d-block");
    brand.classList.remove('d-none');
  } else if (window.scrollY <= navTop && isFixed) {
    isFixed = 0
    nav.classList.remove('fixed-top');
    nav.classList.add("rounded-3", "d-block");
    brand.classList.add('d-none');
  }
};