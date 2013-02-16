!function ($) {
  $(function(){

    // Activate Bootstrap's tooltips
    $("[rel*=tooltip]").tooltip();

    // Subnav fixing code from https://github.com/thomaspark/bootswatch/blob/gh-pages/js/application.js
    var $win = $(window)
      , $nav = $('.navbar')
      , navTop = $('.navbar').length && $('.navbar').offset().top
      , isFixed = 0
    processScroll()
    $win.on('scroll', processScroll)
    function processScroll() {
      var i, scrollTop = $win.scrollTop()
      if (scrollTop >= navTop && !isFixed) {
        isFixed = 1
        $nav.addClass('navbar-fixed-top')
      } else if (scrollTop <= navTop && isFixed) {
        isFixed = 0
        $nav.removeClass('navbar-fixed-top')
      }
    }

    // Let's make videos take the full width
    // TODO; fix aspect ratio
    $(".container").fitVids();

  })
}(window.jQuery);


// Apply masonry smart layout, only at the end of the document load
$(document).ready(function(){
  $('.masonry').masonry({
    itemSelector: '.thumbnail',
    isFitWidth: true,
  });
});
