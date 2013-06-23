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

    // Allow videos to take the full width of a page
    // TODO; fix aspect ratio
    $(".container").fitVids();

    // Apply masonry smart layout, only when all images are loaded
    // Source: http://stackoverflow.com/a/7257177
    // TODO: try to hide re-pagination animation
    var $container = $('.masonry');
    $container.imagesLoaded(function(){
      $container.masonry({
        itemSelector: '.thumbnail',
        isFitWidth: true,
      });
    });

    // YouTube URL parser. Source: http://stackoverflow.com/questions/2964678/jquery-youtube-url-validation-with-regex/10315969#10315969
    function parse_youtube_url(url) {
      var p = /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
      return (url.match(p)) ? RegExp.$1 : false;
    }

    // Display an icon overlay for images enclosed in a link in the main content column
    $("#content a img:not(.icon)").each(function(i, image){
      $(image).mglass({opacity: 1,});
      var image_link = $(image).closest("a");
      if (parse_youtube_url(image_link.attr("href")) != false) {
        image_link.addClass("video");
      };
    });

  })
}(window.jQuery);
