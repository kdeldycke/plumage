// Activate Bootstrap's tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
tooltipTriggerList.forEach(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// Fix navigation to the top on scroll.
//
// Both lookups can come back empty: base.html wraps this markup in a `nav` block, so a
// theme extending Plumage can replace it with its own, brand and all. Reading offsetTop
// off nothing throws, and an uncaught error here would take every script after it down
// with it, so the handler is only wired up when there is something to move.
const nav = document.querySelector('.navbar')
const brand = document.querySelector('.navbar-brand')
if (nav && brand) {
  const navTop = nav.offsetTop
  let isFixed = false
  window.onscroll = function () {
    if (window.scrollY >= navTop && !isFixed) {
      isFixed = true
      nav.classList.add('fixed-top')
      nav.classList.remove('rounded-3', 'd-block')
      brand.classList.remove('d-none')
    } else if (window.scrollY <= navTop && isFixed) {
      isFixed = false
      nav.classList.remove('fixed-top')
      nav.classList.add('rounded-3', 'd-block')
      brand.classList.add('d-none')
    }
  }
}
