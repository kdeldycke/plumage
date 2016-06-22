Plumage
=======

Plumage is a theme for [Pelican](http://getpelican.com), a static site
generator written in Python.

I initially created this theme for [my blog](http://kevin.deldycke.com), but
now the theme is supposed to be generic enough to have its own repository.

![Plumage article view
](https://raw.githubusercontent.com/kdeldycke/plumage/master/plumage-article-screenshot.png)


Features
--------

  * Based on [Bootstrap v2](http://getbootstrap.com/2.3.2/).
  * [Solarized](http://ethanschoonover.com/solarized) code snippets via
    [Pygments](http://pygments.org/) for syntax highlighting.
  * Site-wide static search via [Tipue-search](http://www.tipue.com/search/).
  * Project template.
  * Tags grouped by tiers.
  * External assets (Bootstrap, Jquery, etc...) uses [CDNjs
  ](https://cdnjs.com/about).
  * YouTube links.
  * Direct link to edit articles on Github.


Plugins
-------

Plumage has built-in support for the following plugins:

  * [`tipue_search`
  ](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search)
  * [`neighbors`
  ](https://github.com/getpelican/pelican-plugins/tree/master/neighbors)
  * [`related_posts`
  ](https://github.com/getpelican/pelican-plugins/tree/master/related_posts)
  * [`typogrify`](https://pypi.python.org/pypi/typogrify)


Settings
--------

Plumage can be customized by adding these optionnal parameters to your
`pelicanconf.py` file:

Setting name | Default value | Description
:--- |:--- |:---
`ARTICLE_EDIT_LINK` | | Generate an edit link besides each article. Can use `%(slug)s` to include dynamic article's slug in the link.
`COPYRIGHT` | | Additional copyright statement to add in the third column of the footer.
`DISCLAIMER` | | Overide the Disclaimer notice that gets displayed at the fourth column of the footer.
`DISQUS_SITENAME` | | Pelican can handle Disqus comments. Specify the Disqus sitename identifier here.
`FAVICON_LINKS` | `True` | Fetch link's icons from the free [Favicon Finder](http://icons.better-idea.org) web service.
`GOOGLE_ANALYTICS` | | Set to `UA-XXXXXXXX-Y` to activate Google Analytics.
`GOOGLE_ANALYTICS_PROPERTY` | `"auto"` | Set to property to fine-tune Google Analytics tracking code.
`GOOGLE_SEARCH` | | [Google's Custom Search Engine](https://www.google.com/cse/) ID (e.g. `partner-pub-0123456789098765:0123456789`) to activate blog specific search.
`LEFT_SIDEBAR` | | HTML content to put as-is in the left sidebar.
`LINKS_WIDGET_NAME` | `"Links"` | Allows override of the name of the links widget.
`LINKS` | | A list of tuples (Title, URL) for links to appear in the second column of the footer.
`MENUITEMS`| | A list of tuples (Title, URL) for additional menu items to appear at the beginning of the main menu.
`PIWIK_SITE_ID` | | ID for the monitored website. You can find the ID in the Piwik admin interface > Settings > Websites.
`PIWIK_SSL_URL` | | If the SSL-URL differs from the normal Piwik-URL you have to include this setting too. (optional)
`PIWIK_URL` | | URL to your [Piwik](http://piwik.org) server - without `http://` at the beginning.
`RIGHT_SIDEBAR` | | HTML content to put as-is in the right sidebar.
`SITESUBTITLE` | | A subtitle to appear in the header.
`SITE_THUMBNAIL_TEXT` | | Text displayed behind site's thumbnail.
`SITE_THUMBNAIL` | | Site's thumbnail URL as displayed in the header. Should be a square image of at least 80x80 pixels.
`SOCIAL_WIDGET_NAME` | `"Social"` | Allows override of the name of the “social” widget.
`SOCIAL` | | A list of tuples (Title, URL) to appear in the first columns of the footer.
`TIPUE_SEARCH` | `False` | Activate [Tipue Search](http://www.tipue.com/search) (javascript search engine) into the site. Requires the [`tipue_search`](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search) plugin.

Most of these [parameters are similar to `notmyidea`'s
](http://docs.getpelican.com/en/latest/settings.html#themes) (Pelican's default
theme). For usage example, please have a look into [my own `pelicanconf.py`
](https://github.com/kdeldycke/kevin-deldycke-blog/blob/master/pelicanconf.py).

The theme is also sensible to this list of [standard Pelican parameters
](http://docs.getpelican.com/en/latest/settings.html):

  * `ARCHIVES_SAVE_AS`
  * `AUTHOR_SAVE_AS`
  * `CATEGORIES_SAVE_AS`
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
  * `SITENAME`
  * `SITEURL`
  * `TAG_FEED_ATOM`
  * `TAG_FEED_RSS`
  * `TAGS_SAVE_AS`


FAQ
---

**How can I disable the zoom on images?**

All images of an article are zoomable by default. You can deactivate the
magnifying glass per-image by adding a `noZoom` CSS class. So instead of the
following Markdown code:

    ![Image title](/folder/image.png)

You have to use the following template to deactivate the zoom of an image:

    ![Image title](/folder/image.png){: .noZoom}


Contributors
------------

  * [Kevin Deldycke](https://github.com/kdeldycke)
  * [Cedric Bosdonnat](https://github.com/cbosdo)
  * [Jeff Smith](https://github.com/jeffreyksmithjr)
  * [Stratos Gerakakis](https://github.com/stratosgear)
  * [Renato Cunha](https://github.com/trovao)
  * [Florian Wilhelm](https://github.com/FlorianWilhelm)


Changelog
---------

* [**0.8**
  (2016-06-22)](https://github.com/kdeldycke/plumage/compare/0.7...0.8)
  * Remove legacy Google Analytics tracking code.
  * Rename `GOOGLE_ANALYTICS_UNIVERSAL` option by `GOOGLE_ANALYTICS` and
  `GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY` by `GOOGLE_ANALYTICS_PROPERTY`.
  * Set default `GOOGLE_ANALYTICS_PROPERTY` value to `"auto"`.
  * Allow deactivation of zoom on article's images.
  * Upgrade to Font Awesome 4.6.3.
  * Upgrade to ImagesLoaded 4.1.0.
  * Upgrade to Masonry 4.1.0.
  * Upgrade to Magnific Popup 1.1.0.
  * Upgrade to jQuery 2.2.4.
  * Ditch `grabicon.com` in favor of the free [Favicon Finder
  ](http://icons.better-idea.org) web service.
  * Rename `GRAB_ICONS` option to `FAVICON_LINKS`.
  * Enable favicon fetching by default.
  * Fallback on default external link icon if none found.
  * Remove local copy of Tipue Search assets. Rely on CDNjs instead.

* [**0.7**
  (2015-12-28)](https://github.com/kdeldycke/plumage/compare/0.6...0.7)
  * Add option to bypass grabicon.com web service.
  * Add static search based on Tipue Search.
  * Add new `LINKS_WIDGET_NAME` and `SOCIAL_WIDGET_NAME` options to mirror
    upcoming Pelican 3.7.
  * Align Piwik and Google Analytics code to Pelican's `notmyidea` theme.
  * Add support for newer Google Analytics Universal embed code, via new
    `GOOGLE_ANALYTICS_UNIVERSAL` and `GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY`
    options.
  * Upgrade to jQuery 2.1.4.
  * Upgrade to Masonry 3.3.2.
  * Remove `PDF_PROCESSOR` option now that plugin is out of core.

* [**0.6**
  (2015-05-30)](https://github.com/kdeldycke/plumage/compare/0.5...0.6)
  * Fix favicon rendering.

* [**0.5**
  (2015-05-25)](https://github.com/kdeldycke/plumage/compare/0.4...0.5)
  * Add support for piwik.
  * Upgrade to jQuery 2.1.3.
  * Upgrade to Masonry 3.3.0.
  * Upgrade to fitvids 1.1.0.
  * Upgrade to Magnific Popup 1.0.0.

* [**0.4**
  (2014-02-15)](https://github.com/kdeldycke/plumage/compare/0.3...0.4)
  * Allow grouping of projects.
  * Add option to overide disclaimer notice.
  * Generate tags, categories and archives URLs depending on site
    configuration.
  * Sort out inactive projects to the bottom of the project list.
  * Drop support of old browsers.
  * Move from jQuery 1.x to 2.x.
  * Use [latest Google Analytics
  ](https://developers.google.com/analytics/devguides/collection/upgrade/)
  tracking code.
  * Upgrade to Font Awesome 4.0.3.
  * Upgrade to Masonry 3.1.2.
  * Upgrade to ImagesLoaded 3.0.4.
  * Upgrade to Magnific Popup 0.9.9.

* [**0.3**
  (2013-08-16)](https://github.com/kdeldycke/plumage/compare/0.2...0.3)
  * Add auto-zoom of images based on Magnific Popup.
  * Let the content take the available width if there is no right or left
  sidebars.
  * Add an dynamic feed link in footer.
  * Do not wrap code in code blocks.
  * Fix code highlight for older Pelican versions.
  * Escape and strip tags in all title attributes.
  * Style ampersands for those using typogrify.

* [**0.2**
  (2013-07-09)](https://github.com/kdeldycke/plumage/compare/0.1...0.2)
  * Make theme fully generic through the use of variables.
  * Replace custom navigation with Pelican's neighbors plugin.
  * Add screenshot.
  * Update documentation.

* [**0.1**
  (2013-07-07)](https://github.com/kdeldycke/plumage/compare/0.0...0.1)
  * Theme has now a name: Plumage.
  * Move the theme out of my [blog repository
  ](https://github.com/kdeldycke/kevin-deldycke-blog) to its own repository.
  * Theme is now generic enough. Update TODO-list accordingly.

* [**0.0**
  (2012-12-23)](https://github.com/kdeldycke/plumage/commit/70df9b)
  * First commit.


License
-------

The content of this repository is copyrighted (c) 2012-2016 Kevin Deldycke.

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
