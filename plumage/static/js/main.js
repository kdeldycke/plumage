// Activate Bootstrap's tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
tooltipTriggerList.forEach(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// Stick the navigation to the top on scroll.
//
// Both lookups can come back empty: base.html wraps this markup in a `nav` block, so a
// theme extending Plumage can replace it with its own, brand and all. Calling a method
// on nothing throws, and an uncaught error here would take every script after it down
// with it, so the handler is only wired up when there is something to move.
const nav = document.querySelector('.navbar')
const brand = document.querySelector('.navbar-brand')
if (nav && brand) {
  // The container of the navigation, which base.html puts right under <body>: a sticky
  // box never leaves its parent. The browser pins it in step with the scroll, where the
  // handler below runs a few frames late: on a fast scroll, a navigation that waits for
  // the handler is off screen for that long.
  const bar = nav.closest('body > *')
  bar.classList.add('sticky-top')
  let isStuck = false
  // Gives the pinned navigation its full-width look, with the site name in it.
  window.onscroll = function () {
    // A pixel of slack, so the test holds however the browser rounds the position of a
    // pinned box.
    const shouldStick = bar.getBoundingClientRect().top < 1
    if (shouldStick === isStuck) {
      return
    }
    isStuck = shouldStick
    // That look takes the navigation out of the flow, and the container then holds its
    // place. Without it the content below moves up. A browser with scroll anchoring
    // scrolls by the same height to cancel that move, and that scroll calls this handler
    // again: the navigation flips between its two looks.
    bar.style.minHeight = shouldStick ? `${bar.getBoundingClientRect().height}px` : ''
    // A sticky box stacks its content as one layer, which the site thumbnail sits over.
    // Hand the pinning to the navigation itself: fixed-top stacks it above the thumbnail.
    bar.classList.toggle('sticky-top', !shouldStick)
    nav.classList.toggle('fixed-top', shouldStick)
    nav.classList.toggle('rounded-3', !shouldStick)
    nav.classList.toggle('d-block', !shouldStick)
    brand.classList.toggle('d-none', !shouldStick)
  }
}
