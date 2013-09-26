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
    };

    // Add bootstrap table style to table elements
    $("#content table").addClass('table').addClass('table-hover');

    // Allow videos to take the full width of a page
    $(".container").fitVids();

    // Apply masonry smart layout, only when all images are loaded
    // Source: http://stackoverflow.com/a/7257177
    // TODO: try to hide re-pagination animation
    var $container = $('.masonry');
    if ($container.length) {
      $container.imagesLoaded(function(){
        $container.masonry({
          itemSelector: '.thumbnail',
        });
      });
    };

    // YouTube URL parser. Source: http://stackoverflow.com/questions/2964678/jquery-youtube-url-validation-with-regex/10315969#10315969
    function parse_youtube_url(url) {
      var p = /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
      return (url.match(p)) ? RegExp.$1 : false;
    };

    // Activate zoom on content images in the main column and add an icon overlay (but ignore icons)
    $("#content img:not(.icon)").each(function(){
      // Until we properly generate thumbnails and their links on Pelican's side, we just link an image to itself.
      if ($(this).parents('a').length == 0) {
        $(this).wrap(
          $('<a/>').attr('href', $(this).attr('src'))
        );
      };
      // Add a special class for images linking to videos
      var link_tag = $(this).closest('a');
      if (parse_youtube_url(link_tag.attr('href')) != false) {
        link_tag.addClass("video");
      } else {
        // Activate zoom popup
        link_tag.magnificPopup({
          type: 'image',
          closeOnContentClick: true,
          midClick: true,
          mainClass: 'mfp-with-zoom',
          zoom: {
            enabled: true,
            duration: 300,
            easing: 'ease-in-out',
          },
        });
      };
      // Add overlay zoom icon
      $(this).mglass({opacity: 1,});
    });

  });
}(window.jQuery);
