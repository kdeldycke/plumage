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
  // Takes the place of the navigation while it is fixed. A fixed element leaves the flow,
  // so without a stand-in of the same height the content below moves up. A browser with
  // scroll anchoring then scrolls by that height to keep the content in place, and that
  // scroll calls the handler again: the navigation flips between its two states.
  const placeholder = document.createElement('div')
  let isFixed = false
  window.onscroll = function () {
    const shouldFix = window.scrollY >= navTop
    if (shouldFix === isFixed) {
      return
    }
    isFixed = shouldFix
    if (shouldFix) {
      placeholder.style.height = `${nav.getBoundingClientRect().height}px`
      nav.before(placeholder)
    } else {
      placeholder.remove()
    }
    nav.classList.toggle('fixed-top', shouldFix)
    nav.classList.toggle('rounded-3', !shouldFix)
    nav.classList.toggle('d-block', !shouldFix)
    brand.classList.toggle('d-none', !shouldFix)
  }
}
