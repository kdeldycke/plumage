Plumage
=======

Plumage is a theme for [Pelican](http://getpelican.com), a static site generator written in Python.

I initially created this theme for [my blog](http://kevin.deldycke.com), but now the theme is supposed to be generic enough to have its own repository.


TODO
----

  * Hack google search to integrate search result within theme design ?
  * Replace Google custom search by https://swiftype.com/ ? Or better, static search: http://ralsina.com.ar/weblog/posts/standalone-search-in-nikola.html
  * Fix embedded video aspect-ratio
  * Use a big carousel for front-page articles (ex: http://twitter.github.com/bootstrap/examples/carousel.html ) + a bit of http://srobbin.com/jquery-plugins/backstretch/ to keep aspect-ratio
  * Check some web-dev essentials: http://webdevchecklist.com/
  * Add a fancy zoom for images
  * Use custom jinja filters instead of heavy tag soup in my theme ? Example: https://bitbucket.org/sirex/blog/src/32c192ff7a10/pelican.conf.py#cl-53
  * Add progressive image loading. See: http://www.appelsiini.net/projects/lazyload
  * Concatenate and minify CSS and Javascript. See:
      * https://pypi.python.org/pypi/mincss
      * http://ralsina.com.ar/weblog/posts/mincss-is-amazing.html
      * https://pypi.python.org/pypi/pelican-minify
  * Inline and embed all CSS in the page ? See: http://www.peterbe.com/plog/100-percent-inline-css
  * Use LESS version of bootstrap for cleaner customizations ?
  * Check and fix style on mobile (especially ugly margins)
  * Look at app-template for code inspiration and ideas:
      *  https://github.com/nprapps/app-template/blob/master/templates/_base.html
      *  https://github.com/nprapps/app-template/blob/master/render_utils.py
  * Add progressive loading on masonery layouts. See: http://masonry.desandro.com/demos/infinite-scroll.html
  * Contibute theme to Pelican's repository ? For the moment I have 2 fans:
      * https://twitter.com/_alagappan/status/328299060815618048
      * https://twitter.com/Jonas_Wallin/status/346373684912599040
  * Remove hard-coded Ad
  * Remove hard-coded Google Analytics code
  * Remove hard-coded Disqus code
  * Remove hard-coded header avatar
  * Replace Previous/Next article navigation with Pelican plugin: https://github.com/getpelican/pelican-plugins/tree/master/neighbors
  * Re-integrate Related Posts: the Disqus widget doesn't do a good job. Use: https://github.com/getpelican/pelican-plugins/tree/master/related_posts
  * Make footer content dynamic
  * Remove GoSquared


License
-------

The content of this repository is copyrighted (c) 2012-2013 Kevin Deldycke.

Unless contrary mention, the content in this repository is licensed under a [GNU/GPL licence, v2.0](http://www.fsf.org/licensing/licenses/gpl.html).


Third-party assets
------------------

The theme uses external softwares, scripts, libraries and artworks:

    jQuery MGlass v1.1
    Copyright (c) 2012 Younès El Biache
    Distributed under a MIT license
    Source: https://github.com/younes0/jQuery-MGlass

    Solarized Pygment style v0.1.0
    Copyright (c) 2012 Shoji KUMAGAI
    Distributed under a MIT license
    Source: http://pypi.python.org/pypi/pygments-style-solarized

    Fabric (Plaid)
    Copyright (c) 2012 James Basoo
    Distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license
    Source: http://subtlepatterns.com/fabric-plaid/

    Cream paper
    Copyright (c) 2012 Devin Holmes
    Distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license
    Source: http://subtlepatterns.com/cream-paper/
