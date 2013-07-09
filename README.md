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


Plugins
-------

Plumage has built-in support for the following plugins:

  * [`neighbors`](https://github.com/getpelican/pelican-plugins/tree/master/neighbors)
  * [`related_posts`](https://github.com/getpelican/pelican-plugins/tree/master/related_posts)


Settings
--------

Plumage is sensible to this list of [standard Pelican parameters](http://docs.getpelican.com/en/latest/settings.html):

  * `ARCHIVES_SAVE_AS`
  * `AUTHOR_SAVE_AS`
  * `CATEGORY_FEED_ATOM`
  * `CATEGORY_FEED_RSS`
  * `CATEGORY_SAVE_AS`
  * `DEFAULT_LANG`
  * `DEFAULT_PAGINATION`
  * `DISPLAY_PAGES_ON_MENU`
  * `DISQUS_SITENAME`
  * `FEED_ALL_ATOM`
  * `FEED_ALL_RSS`
  * `FEED_ATOM`
  * `FEED_DOMAIN`
  * `FEED_RSS`
  * `GOOGLE_ANALYTICS`
  * `LINKS`
  * `MENUITEMS`
  * `PDF_PROCESSOR`
  * `SITENAME`
  * `SITESUBTITLE`
  * `SITEURL`
  * `TAG_FEED_ATOM`
  * `TAG_FEED_RSS`
  * `TAGS_SAVE_AS`

This theme also adds some new parameters:

  * `SOCIAL_TITLE`: Set the title of the block listing social links. Default value: `Social`.
  * `LINKS_TITLE`: Set the title of the block listing the misc links. Default value: `Links`.
  * `GOOGLE_ANALYTICS_DOMAIN`: Add the `_setDomainName` variable to Google Analytics' Javascript code.

All parameters mentionned here are optionnal.


TODO
----

  * Hack google search to integrate search result within theme design ?
  * Replace Google custom search by https://swiftype.com/ ? Or better, static search: http://ralsina.com.ar/weblog/posts/standalone-search-in-nikola.html
  * Fix embedded video aspect-ratio. Maybe the following may help:
      * https://github.com/toddmotto/fluidvids
      * https://github.com/chriscoyier/Fluid-Width-Video
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
  * Make a macro to generated iconized links
  * Remove hard-coded Ad
  * Remove hard-coded header avatar


Authors
-------

  * Kevin Deldycke <kevin@deldycke.com>


Changelog
---------

* **1.0.dev** (unreleased)
  * Make Disqus and Google Analytics code generic.
  * Remove GoSquared.
  * Replace custom navigation with Pelican's neighbors plugin.
  * Add screenshot.
  * Update documentation.

* **0.1** (2013-07-07)
  * Move out theme from my [blog repository](https://github.com/kdeldycke/kevin-deldycke-blog) to its own repository.
  * Theme has now a name: Plumage.
  * The theme should now be generic enough. Update TODO-list accordingly.

* **0.0** (2012-12-23)
  * First commit.


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
