# Plumage

Plumage is a clean and tidy theme for [Pelican](https://getpelican.com) (a
static site generator).

I initially created this theme for [my blog](https://kevin.deldycke.com), but
it is now generic enough to be used by anyone.


## Features

* Standard Pelican views:

  ![Plumage article view](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/article.png) | ![Plumage categories view](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/categories.png) | ![Plumage tiered tag list view](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/tiered-tags.png)
  :-:|:-:|:-:
  Article | Categories | Tiered tag list

  ![Plumage archive view](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/archives.png) | ![Plumage tag view](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/tag.png) | ![Plumage authors view](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/authors.png)
  :-:|:-:|:-:
  Collapsable yearly archives | Tagged articles | Authors

* Projects template:

  ![Plumage projects: code showcase](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/projects-code.png) | ![Plumage projects: videos showcase](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/projects-videos.png) | ![Plumage projects: themes showcase](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/projects-themes.png)
  :-:|:-:|:-:
  Code showcase ([source](https://github.com/kdeldycke/kevin-deldycke-blog/blob/ebe0d17a59730457c3016dff77fdfa799a80d756/content/templates/code.html)) | Videos showcase ([source](https://github.com/kdeldycke/kevin-deldycke-blog/blob/f778998376fa5c68f1a02129884b89592b641777/content/templates/videos.html)) | Themes showcase ([source](https://github.com/kdeldycke/kevin-deldycke-blog/blob/f778998376fa5c68f1a02129884b89592b641777/content/templates/themes.html))

* Based on [Bootstrap v4](https://getbootstrap.com).

* [Solarized](https://ethanschoonover.com/solarized) code snippets via
  [Pygments](https://pygments.org/) for syntax highlighting:

  ![Plumage Solarized syntax highlight](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/syntax-highlight.png)

* Site-wide static search via [Tipue-search](https://www.tipue.com/search/).

* Bare YouTube links in articles gets rendered as embedded videos:

  ![Plumage YouTube link](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/youtube-link.png)

* Direct link to edit articles on GitHub:

  ![Plumage GitHub edit link](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/github-edit-link.png)

* Magnifying glass overlays on images and zoom:

  ![Plumage image magnifying glass](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/magnifying-glass.png)
  ![Plumage image zoom](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/zoom.png)

* External assets (Bootstrap, Jquery, etc...) uses [CDNjs
](https://cdnjs.com/about).

* Disqus integration:

  ![Plumage disqus comments](https://raw.githubusercontent.com/kdeldycke/plumage/develop/screenshots/disqus.png)


## Plugins

Plumage has built-in support for the following plugins and extensions:

* Pelican builtins:
    * [`typogrify`](https://pypi.python.org/pypi/typogrify): style ampersands.

* Pelican third-party plugins:
    * [`tipue_search`
      ](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search)
    * [`neighbors`
      ](https://github.com/getpelican/pelican-plugins/tree/master/neighbors)
    * [`related_posts`
      ](https://github.com/getpelican/pelican-plugins/tree/master/related_posts)

* Markdown extensions:
    * [`markdown.extensions.admonition`](https://python-markdown.github.io/extensions/admonition/):
      re-style admonitions into [alerts](https://getbootstrap.com/docs/4.5/components/alerts/).
    * [`markdown.extensions.codehilite`](https://python-markdown.github.io/extensions/code_hilite/):
      style highlighted code with Pygment style.
    * [`markdown.extensions.toc`](https://python-markdown.github.io/extensions/toc/#usage),
      adds permalink anchors to article's subtitles.
    * [`pymdownx.emoji`](https://facelessuser.github.io/pymdown-extensions/extensions/emoji/#default-emoji-generators):
      style `emojione` set for proper integration into text.
    * [`pymdownx.highlight`](https://facelessuser.github.io/pymdown-extensions/extensions/highlight/):
      style highlighted code with Pygment style.


## Installation

This package is [available on PyPi](https://pypi.python.org/pypi/plumage), so
you can install the latest stable release and its dependencies with a simple
``pip`` call:

```python
$ pip install plumage
```

Then, update your `pelicanconf.py` file, with the module:

```python
import plumage

THEME = plumage.get_path()
```


## Settings

Plumage can be customized by adding these optionnal parameters to your
`pelicanconf.py` file:

Setting name | Default value | Description
:--- |:--- |:---
`ARTICLE_EDIT_LINK` | | Generate an edit link besides each article. Can use `%(slug)s` to include dynamic article's slug in the link.
`COPYRIGHT` | | Additional copyright statement to add in the third column of the footer.
`DISCLAIMER` | | Overide the Disclaimer notice that gets displayed at the fourth column of the footer.
[`DISQUS_SITENAME`](http://docs.getpelican.com/en/stable/settings.html#DISQUS_SITENAME) | | Pelican can handle Disqus comments. Specify the Disqus sitename identifier here.
`FAVICON_LINKS` | `True` | Fetch link's icons from [Google's favicons webservice](https://www.google.com/s2/favicons).
[`GOOGLE_ANALYTICS`](http://docs.getpelican.com/en/stable/settings.html#GOOGLE_ANALYTICS) | | Set to `UA-XXXXXX-Y` Property's tracking ID to activate Google Analytics.
`LEFT_SIDEBAR` | | HTML content to put as-is in the left sidebar.
[`LINKS_WIDGET_NAME`](http://docs.getpelican.com/en/stable/settings.html#LINKS_WIDGET_NAME) | `"Links"` | Allows override of the name of the links widget.
[`LINKS`](http://docs.getpelican.com/en/stable/settings.html#LINKS) | | A list of tuples (Title, URL) for links to appear in the second column of the footer.
[`MANUAL_LINKS`](http://docs.getpelican.com/en/stable/settings.html#MANUAL_LINKS) | | When enabling this, you must pass the links (in LINKS & SOCIAL settins) not as tuples anymore, but as list, where every entry is formatted as you like
[`MENUITEMS`](http://docs.getpelican.com/en/stable/settings.html#MENUITEMS) | | A list of tuples (Title, URL) for additional menu items to appear at the beginning of the main menu.
`RIGHT_SIDEBAR` | | HTML content to put as-is in the right sidebar.
[`SITESUBTITLE`](http://docs.getpelican.com/en/stable/settings.html#SITESUBTITLE) | | A subtitle to appear in the header.
`SITE_THUMBNAIL_TEXT` | | Text displayed behind site's thumbnail.
`SITE_THUMBNAIL` | | Site's thumbnail URL as displayed in the header. Should be a square image of at least 80x80 pixels.
[`SOCIAL_WIDGET_NAME`](http://docs.getpelican.com/en/stable/settings.html#SOCIAL_WIDGET_NAME) | `"Social"` | Allows override of the name of the “social” widget.
[`SOCIAL`](http://docs.getpelican.com/en/stable/settings.html#SOCIAL) | | A list of tuples (Title, URL) to appear in the first columns of the footer.
`TIPUE_SEARCH` | `False` | Activate [Tipue Search](https://www.tipue.com/search) (javascript search engine) into the site. Requires the [`tipue_search`](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search) plugin.

Most of these [parameters are similar to `notmyidea`'s
](https://docs.getpelican.com/en/latest/settings.html#themes) (Pelican's default
theme). For usage example, please have a look into [my own `pelicanconf.py`
](https://github.com/kdeldycke/kevin-deldycke-blog/blob/master/pelicanconf.py).

The theme is also sensible to this list of [standard Pelican parameters
](https://docs.getpelican.com/en/latest/settings.html):

  * `ARCHIVES_SAVE_AS`
  * `AUTHOR`
  * `AUTHOR_SAVE_AS`
  * `AUTHORS_SAVE_AS`
  * `CATEGORIES_SAVE_AS`
  * `CATEGORY_FEED_ATOM`
  * `CATEGORY_FEED_RSS`
  * `DEFAULT_LANG`
  * `DEFAULT_PAGINATION`
  * `DISPLAY_PAGES_ON_MENU`
  * `DISPLAY_CATEGORIES_ON_MENU`
  * `FEED_ALL_ATOM`
  * `FEED_ALL_RSS`
  * `FEED_ATOM`
  * `FEED_DOMAIN`
  * `FEED_RSS`
  * `PAGINATION_PATTERNS`
  * `SITENAME`
  * `SITEURL`
  * `TAG_FEED_ATOM`
  * `TAG_FEED_RSS`
  * `TAGS_SAVE_AS`
  * `TYPOGRIFY`


## FAQ

**How can I disable the zoom on images?**

All images of an article are zoomable by default. You can deactivate the
magnifying glass per-image by adding a `noZoom` CSS class. So instead of the
following Markdown code:

    ![Image title](/folder/image.png)

You have to use the following template to deactivate the zoom of an image:

    ![Image title](/folder/image.png){: .noZoom}

**Why is the search not working?**

Some plugins may need additional settings, for instance for **tipue_search**,
after applying the standard options:

```python
PLUGINS = ['tipue_search']
TIPUE_SEARCH = True
```

... you'll need to declare additional template file,
by either adding this line to your `pelicanconf.py`:

```python
TEMPLATE_PAGES = {
        'search.html': 'search.html',
        }
```

or using [this technique](https://github.com/kdeldycke/kevin-deldycke-blog/commit/cd4bf8d1f4c55d835d7bfe1d7233cffe48e67a8a).


## License

This software is licensed under the [GNU General Public License v2 or later
(GPLv2+)](https://github.com/kdeldycke/plumage/blob/master/LICENSE).

Copyright (C) 2012-2020 [Kevin Deldycke](https://kevin.deldycke.com) and
[contributors](https://github.com/kdeldycke/plumage/graphs/contributors). All
Rights Reserved.


## Third-party assets

The theme embed copies of some external softwares, scripts, libraries and
artworks:

    Tipue Search v7.1
    Copyright (c) 2019 Tipue
    Distributed under a MIT license
    Source: https://web.archive.org/web/20200703134724/https://www.tipue.com/search/tipuesearch.zip

    jQuery MGlass v1.1
    Copyright (c) 2012 Younès El Biache
    Distributed under a MIT license
    Source: https://github.com/younes0/jQuery-MGlass

    Fabric (Plaid)
    Copyright (c) 2012 James Basoo
    Distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license
    Source: https://subtlepatterns.com/fabric-plaid/

    Cream paper
    Copyright (c) 2012 Devin Holmes
    Distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license
    Source: https://subtlepatterns.com/cream-paper/
