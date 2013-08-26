Plumage
=======

Plumage is a theme for [Pelican](http://getpelican.com) 3.2, a static site generator written in Python.

I initially created this theme for [my blog](http://kevin.deldycke.com), but now the theme is supposed to be generic enough to have its own repository.

![Plumage article view](http://github.com/kdeldycke/plumage/raw/master/plumage-article-screenshot.png)


Features
--------

  * Based on Twitter Bootstrap
  * Project template
  * Tags grouped by tiers
  * External assets (Bootstrap, Jquery, etc...) uses CDN
  * YouTube links
  * Direct link to edit articles on Github
  * Pygments syntax highlighting


Plugins
-------

Plumage has built-in support for the following plugins:

  * [`neighbors`](https://github.com/getpelican/pelican-plugins/tree/master/neighbors)
  * [`related_posts`](https://github.com/getpelican/pelican-plugins/tree/master/related_posts)
  * [`typogrify`](https://github.com/getpelican/pelican-typogrify)


Settings
--------

Plumage can be customized by adding these optionnal parameters to your `pelicanconf.py` file:

  * `SITE_THUMBNAIL`: Site's thumbnail URL as displayed in the header. Should be a square image of at least 80x80 pixels.
  * `SITE_THUMBNAIL_TEXT`: Text displayed behind site's thumbnail.
  * `SITESUBTITLE`: Set the subtitle from the site's header.
  * `MENUITEMS`: A list of tuples (Title, URL) for additional menu items to appear at the beginning of the main menu.
  * `GOOGLE_SEARCH`: [Google's Custom Search Engine](https://www.google.com/cse/) ID (e.g. `partner-pub-0123456789098765:0123456789`) to activate blog specific search.
  * `LEFT_SIDEBAR`, `RIGHT_SIDEBAR`: HTML content to put as-is in the left or right sidebar.
  * `ARTICLE_EDIT_LINK`: Generate an edit link besides each article. Can use `%(slug)s` to include dynamic article's slug in the link.
  * `SOCIAL`: A list of tuples (Title, URL) to appear in the first columns of the footer.
  * `SOCIAL_TITLE`: Ovveride the title of the first column of the footer. Default value: `Social`.
  * `LINKS`: A list of tuples (Title, URL) for links to appear in the second column of the footer.
  * `LINKS_TITLE`: Ovveride the title of the second column of the footer. Default value: `Links`.
  * `COPYRIGHT`: Additional copyright statement to add in the third column of the footer.
  * `DISQUS_SITENAME`: Disqus sitename identifier.
  * `GOOGLE_ANALYTICS`: Google Analytics unique identifier (e.g. `UA-XXXX-YYYY`).
  * `GOOGLE_ANALYTICS_DOMAIN`: Add the `_setDomainName` variable to Google Analytics' Javascript code.

Most of these [parameters are similar to `notmyidea`'s](http://docs.getpelican.com/en/latest/settings.html#themes) (Pelican's default theme). For usage example, please have a look into [my own `pelicanconf.py`](https://github.com/kdeldycke/kevin-deldycke-blog/blob/master/pelicanconf.py).

The theme is also sensible to this list of [standard Pelican parameters](http://docs.getpelican.com/en/latest/settings.html):

  * `ARCHIVES_SAVE_AS`
  * `AUTHOR_SAVE_AS`
  * `CATEGORY_FEED_ATOM`
  * `CATEGORY_FEED_RSS`
  * `CATEGORY_SAVE_AS`
  * `DEFAULT_LANG`
  * `DEFAULT_PAGINATION`
  * `DISPLAY_PAGES_ON_MENU`
  * `FEED_ALL_ATOM`
  * `FEED_ALL_RSS`
  * `FEED_ATOM`
  * `FEED_DOMAIN`
  * `FEED_RSS`
  * `PDF_PROCESSOR`
  * `SITENAME`
  * `SITEURL`
  * `TAG_FEED_ATOM`
  * `TAG_FEED_RSS`
  * `TAGS_SAVE_AS`


TODO
----

  * Hack google search to integrate search result within theme design ?
  * Replace Google custom search by https://swiftype.com/ ? Or better, static search: http://ralsina.com.ar/weblog/posts/standalone-search-in-nikola.html
  * Fix embedded video aspect-ratio. Maybe the following may help:
      * https://github.com/toddmotto/fluidvids
      * https://github.com/chriscoyier/Fluid-Width-Video
  * Use a big carousel for front-page articles (ex: http://twitter.github.com/bootstrap/examples/carousel.html ) + a bit of http://srobbin.com/jquery-plugins/backstretch/ to keep aspect-ratio
  * Check some web-dev essentials:
      * http://webdevchecklist.com/
      * https://github.com/getpelican/pelican-plugins/tree/master/w3c_validate
      * https://github.com/dypsilon/frontend-dev-bookmarks
  * Use custom jinja filters instead of heavy tag soup in my theme ? Example: https://bitbucket.org/sirex/blog/src/32c192ff7a10/pelican.conf.py#cl-53
  * Add progressive image loading. See:
      * https://github.com/vvo/lazyload
      * https://github.com/tuupola/jquery_lazyload
      * https://github.com/luis-almeida/unveil
  * Concatenate and minify CSS and Javascript. See:
      * https://pypi.python.org/pypi/mincss
      * http://ralsina.com.ar/weblog/posts/mincss-is-amazing.html
      * https://pypi.python.org/pypi/pelican-minify
      * https://github.com/getpelican/pelican-plugins/tree/master/assets
  * Inline and embed all CSS in the page ? See: http://www.peterbe.com/plog/100-percent-inline-css
  * Use LESS version of bootstrap for cleaner customizations ?
  * Check and fix style on mobile (especially ugly margins)
  * Look at app-template for code inspiration and ideas:
      *  https://github.com/nprapps/app-template/blob/master/templates/_base.html
      *  https://github.com/nprapps/app-template/blob/master/render_utils.py
  * Make Masonry responsive ? See:
      * http://osvaldas.info/responsive-jquery-masonry-or-pinterest-style-layout
      * http://deanclatworthy.com/2012/09/responsive-twitter-bootstrap-masonry/
      * http://www.maurizioconventi.com/2012/06/19/responsive-example-integrating-twitter-bootstrap-and-jquery-masonry/
  * Add progressive loading on masonery layouts. See: http://masonry.desandro.com/demos/infinite-scroll.html
  * Generate thumbnails in article content. See:
      * https://github.com/getpelican/pelican-plugins/pull/40
      * https://github.com/getpelican/pelican-plugins/pull/43
  * Auto-enhance created thumbnails ? See: https://news.ycombinator.com/item?id=5999201
  * Generate Disqus static comments for SEO ? See: https://github.com/getpelican/pelican-plugins/tree/master/disqus_static
  * Group contiguous images in a post into a tiled galery:
      * as in WordPress' jetpack plugin: https://github.com/crowdfavorite-mirrors/wp-jetpack/tree/master/modules/tiled-gallery
      * or thanks to https://github.com/jakobholmelund/fitpicsjs
  * Replace MGlass zoom icon overlay with pure CSS. Inspirations:
      * Cover effect at http://h5bp.github.io/Effeckt.css/dist/captions.html
      * http://codepen.io/Twikito/pen/Jeaub
      * To center the zoom icon, we can use one of these trick: http://codepen.io/shshaw/full/gEiDt
  * CSS typography: http://www.newnet-soft.com/blog/csstypography


Contributors
------------

  * [Kevin Deldycke](https://github.com/kdeldycke)
  * [Cedric Bosdonnat](https://github.com/cbosdo)
  * [Jeff Smith](https://github.com/jeffreyksmithjr)


Changelog
---------

* **0.4.dev** (unreleased)
  * Drop support of old browsers.
  * Move from jQuery 1.x to 2.x.

* **0.3** (2013-08-16)
  * Add auto-zoom of images based on Magnific Popup.
  * Let the content take the available width if there is no right or left sidebars.
  * Add an dynamic feed link in footer.
  * Do not wrap code in code blocks.
  * Fix code highlight for older Pelican versions.
  * Escape and strip tags in all title attributes.
  * Style ampersands for those using typogrify.

* **0.2** (2013-07-09)
  * Make theme fully generic through the use of variables.
  * Replace custom navigation with Pelican's neighbors plugin.
  * Add screenshot.
  * Update documentation.

* **0.1** (2013-07-07)
  * Theme has now a name: Plumage.
  * Move the theme out of my [blog repository](https://github.com/kdeldycke/kevin-deldycke-blog) to its own repository.
  * Theme is now generic enough. Update TODO-list accordingly.

* **0.0** (2012-12-23)
  * First commit.


Pushing Plumage to Pelican project
----------------------------------

This is just a note to myself on how to submit new stable releases of Plumage to [Pelican's theme repository](https://github.com/getpelican/pelican-themes).

    $ git clone --recursive https://github.com/kdeldycke/pelican-themes
    $ cd pelican-themes/plumage/
    $ git checkout 0.X
    $ cd ..
    $ git add ./plumage
    $ git commit -m "Update Plumage to version 0.X"
    $ git push
    $ cd ..
    $ rm -rf ./pelican-themes

Now [create a Pull Request](https://github.com/kdeldycke/pelican-themes/compare/getpelican:master...master) from GitHub web interface, and submit it for merging to the original repository.


License
-------

The content of this repository is copyrighted (c) 2012-2013 Kevin Deldycke.

This code is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, version 2, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

For full details, please see the file named COPYING in the top directory of the
source tree. You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.


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
