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

    // Add bootstrap table style to table elements
    $("#content table").addClass('table').addClass('table-hover');

    // Let's make videos take the full width
    // TODO; fix aspect ratio
    $(".container").fitVids();

    // Apply masonry smart layout, only when all images are loaded
    // Source: http://stackoverflow.com/a/7257177
    var $container = $('.masonry');
    $container.imagesLoaded(function(){
      $container.masonry({
        itemSelector: '.thumbnail',
        isFitWidth: true,
      });
    });

  })
}(window.jQuery);