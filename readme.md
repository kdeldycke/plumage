<p align="center">
  <a href="https://github.com/kdeldycke/plumage/">
    <img src="https://github.com/kdeldycke/plumage/raw/main/screenshots/plumage-header-logo.jpeg" alt="Plumage, a Pelican theme">
  </a>
</p>

Plumage is a clean and tidy theme for [Pelican](https://getpelican.com), a
static site generator.

I initially created this theme for [my blog](https://kevin.deldycke.com), but
it is now generic enough to be used by anyone.

## Features

- Standard Pelican views:

  |      ![Plumage article view](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/article.jpeg)      | ![Plumage categories view](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/categories.jpeg) | ![Plumage tiered tag list view](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/tiered-tags.jpeg) |
  | :------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------: |
  |                                                       Article                                                        |                                                    Categories                                                    |                                                    Tiered tag list                                                     |
  |     ![Plumage archive view](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/archives.jpeg)      |        ![Plumage tag view](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/tag.jpeg)        |       ![Plumage authors view](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/authors.jpeg)       |
  |                                             Collapsable yearly archives                                              |                                                 Tagged articles                                                  |                                                        Authors                                                         |
  | ![Plumage archive view](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/browse-content-by.jpeg) |                                                                                                                  |                                                                                                                        |
  |                                               Faceted article browsing                                               |                                                                                                                  |                                                                                                                        |

- Projects template:

  |             ![Plumage projects: code showcase](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/projects-code.jpeg)              |             ![Plumage projects: videos showcase](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/projects-videos.jpeg)              |             ![Plumage projects: themes showcase](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/projects-themes.jpeg)              |
  | :--------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: |
  | Code showcase ([source](https://github.com/kdeldycke/kevin-deldycke-blog/blob/ebe0d17a59730457c3016dff77fdfa799a80d756/content/templates/code.html)) | Videos showcase ([source](https://github.com/kdeldycke/kevin-deldycke-blog/blob/f778998376fa5c68f1a02129884b89592b641777/content/templates/videos.html)) | Themes showcase ([source](https://github.com/kdeldycke/kevin-deldycke-blog/blob/f778998376fa5c68f1a02129884b89592b641777/content/templates/themes.html)) |

- Based on [Bootstrap v5](https://getbootstrap.com).

- [Code syntax highlighting](#code-syntax-highlighting) with [30+ styles](https://github.com/pygments/pygments/tree/master/pygments/styles).

- Site-wide static search via [Stork](https://stork-search.net).

- Bare YouTube links in articles gets rendered as embedded videos:

  ![Plumage YouTube link](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/youtube-link.jpeg)

- Direct link to edit articles on GitHub:

  ![Plumage GitHub edit link](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/github-edit-link.jpeg)

- Magnifying glass overlays on images and zoom:

  ![Plumage image magnifying glass](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/magnifying-glass.jpeg)
  ![Plumage image zoom](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/zoom.jpeg)

- External assets (Bootstrap, Jquery, etc...) uses [CDNjs
  ](https://cdnjs.com/about).

- Disqus integration:

  ![Plumage disqus comments](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/disqus.jpeg)

## Plugins

Plumage has built-in support for the following plugins and extensions:

| Plugin name                                                                                                      | Type               | Status   | Notes                                                                                                         |
| :--------------------------------------------------------------------------------------------------------------- | :----------------- | :------- | :------------------------------------------------------------------------------------------------------------ |
| [`pelican-image-process`](https://github.com/pelican-plugins/image-process)                                      | Pelican plugin     | Optional | Embed a hack to [fix parsing of external images](https://github.com/pelican-plugins/image-process/issues/33). |
| [`pelican-neighbors`](https://github.com/pelican-plugins/neighbors)                                              | Pelican plugin     | Optional |                                                                                                               |
| [`pelican-related-posts`](https://github.com/pelican-plugins/related-posts)                                      | Pelican plugin     | Optional |                                                                                                               |
| [`pelican-similar-posts`](https://github.com/pelican-plugins/similar-posts)                                      | Pelican plugin     | Optional |                                                                                                               |
| [`pelican-search`](https://github.com/pelican-plugins/search)                                                    | Pelican plugin     | Optional |                                                                                                               |
| [`pelican-webassets`](https://github.com/pelican-plugins/webassets)                                              | Pelican plugin     | Required |                                                                                                               |
| [`markdown.extensions.admonition`](https://python-markdown.github.io/extensions/admonition/)                     | Markdown extension | Optional | Re-style admonitions into [alerts](https://getbootstrap.com/docs/4.5/components/alerts/).                     |
| [`markdown.extensions.codehilite`](https://python-markdown.github.io/extensions/code_hilite/)                    | Markdown extension | Optional | Style highlighted code with Pygment style.                                                                    |
| [`markdown.extensions.toc`](https://python-markdown.github.io/extensions/toc/#usage)                             | Markdown extension | Optional | Adds permalink anchors to article's subtitles.                                                                |
| [`pymdownx.highlight`](https://facelessuser.github.io/pymdown-extensions/extensions/highlight/)                  | Markdown extension | Optional | Style highlighted code with Pygment style.                                                                    |
| [`typogrify`](https://pypi.python.org/pypi/typogrify)                                                            | Pelican builtin    | Optional | Style ampersands.                                                                                             |

## Installation

Install this theme using the `main` branch of this Github repo.

If you're already using `poetry` to manage dependency of Pelican project, you need to run just

```shell-session
poetry add git+https://github.com/kdeldycke/plumage#main
```

Or, can manually add the following line in the  `[tool.poetry.dependencies]` section of the `pyproject.toml` file.

```
plumage = {git = "https://github.com/kdeldycke/plumage", rev = "main"}
```

Once added, run `poetry update` to reflect this new dependency.

**Note:** If you haven't used `poetry` in the project yet, you need to do so before adding `plumage`.
You can do that by first [installing `poetry`](https://python-poetry.org/docs/#installation) on your system and then running `poetry init` inside the project folder.

Then, once you're done installing the `plumage` module, update your `pelicanconf.py` file to reference the module:

```python
import plumage

THEME = plumage.get_path()
```

On first run, Plumage will try to install [Node.js package dependencies](https://github.com/kdeldycke/plumage/blob/main/plumage/package.json) via the `npm` CLI:

```shell-session
$ poetry run pelican --verbose ./content
(…)
WARNING: postcss CLI not found.
-> Install Plumage's Node.js dependencies from (…)/plumage/package.json:
  |   {
  |     "name": "plumage-webassets-pipeline",
  |     "description": "Plumage depdencies for the webassets compilation pipeline.",
  |     "dependencies": {
  |       "postcss-cli": "^8.3.1"
  |     }
  |   }
  |

up to date, audited 96 packages in 984ms

found 0 vulnerabilities
-> postcss CLI found at (…)/plumage/node_modules/.bin/postcss
(…)
```

## Settings

Plumage can be customized by adding these optionnal parameters to your
`pelicanconf.py` file:

| Setting name                                                                                  | Default value | Description                                                                                                                                                    |
| :-------------------------------------------------------------------------------------------- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ARTICLE_EDIT_LINK`                                                                           |               | Generate an edit link besides each article. Can use `%(slug)s` to include dynamic article's slug in the link.                                                  |
| `CODE_STYLE`                                                                                  | `"monokai"`   | Pygments' style ID. Choose one from `poetry run pygmentize -L styles`.                                                                                         |
| `COPYRIGHT`                                                                                   |               | Additional copyright statement to add in the third column of the footer.                                                                                       |
| `DISCLAIMER`                                                                                  |               | Overide the disclaimer notice that gets displayed at the fourth column of the footer.                                                                          |
| [`DISQUS_SITENAME`](http://docs.getpelican.com/en/stable/settings.html#DISQUS_SITENAME)       |               | Pelican can handle Disqus comments. Specify the Disqus sitename identifier here.                                                                               |
| `FAVICON_LINKS`                                                                               | `True`        | Fetch link's icons from [Google's favicons webservice](https://www.google.com/s2/favicons).                                                                    |
| [`GOOGLE_ANALYTICS`](http://docs.getpelican.com/en/stable/settings.html#GOOGLE_ANALYTICS)     |               | Set to `UA-XXXXXX-Y` Property's tracking ID to activate Google Analytics.                                                                                      |
| `LEFT_SIDEBAR`                                                                                |               | HTML content to put as-is in the left sidebar.                                                                                                                 |
| [`LINKS_WIDGET_NAME`](http://docs.getpelican.com/en/stable/settings.html#LINKS_WIDGET_NAME)   | `"Links"`     | Allows override of the name of the links widget.                                                                                                               |
| [`LINKS`](http://docs.getpelican.com/en/stable/settings.html#LINKS)                           |               | A list of tuples (Title, URL) for links to appear in the second column of the footer.                                                                          |
| [`MANUAL_LINKS`](http://docs.getpelican.com/en/stable/settings.html#MANUAL_LINKS)             |               | When enabling this, you must pass the links (in LINKS & SOCIAL settins) not as tuples anymore, but as list, where every entry is formatted as you like         |
| [`MENUITEMS`](http://docs.getpelican.com/en/stable/settings.html#MENUITEMS)                   |               | A list of tuples (Title, URL) for additional menu items to appear at the beginning of the main menu.                                                           |
| `RIGHT_SIDEBAR`                                                                               |               | HTML content to put as-is in the right sidebar.                                                                                                                |
| [`SITESUBTITLE`](http://docs.getpelican.com/en/stable/settings.html#SITESUBTITLE)             |               | A subtitle to appear in the header.                                                                                                                            |
| `SITE_THUMBNAIL_TEXT`                                                                         |               | Text displayed behind site's thumbnail.                                                                                                                        |
| `SITE_THUMBNAIL`                                                                              |               | Site's thumbnail URL as displayed in the header. Should be a square image of at least 80x80 pixels.                                                            |
| [`SOCIAL_WIDGET_NAME`](http://docs.getpelican.com/en/stable/settings.html#SOCIAL_WIDGET_NAME) | `"Social"`    | Allows override of the name of the “social” widget.                                                                                                            |
| [`SOCIAL`](http://docs.getpelican.com/en/stable/settings.html#SOCIAL)                         |               | A list of tuples (Title, URL) to appear in the first columns of the footer.                                                                                    |
| `STORK_SEARCH`                                                                                | `False`       | Activate [Stork](https://stork-search.net) static search engine. Requires the [official Pelican's `search` plugin](https://github.com/pelican-plugins/search). |

Most of these [parameters are similar to `notmyidea`'s
](https://docs.getpelican.com/en/latest/settings.html#themes) (Pelican's default
theme). For usage example, please have a look into [my own `pelicanconf.py`
](https://github.com/kdeldycke/kevin-deldycke-blog/blob/main/pelicanconf.py).

The theme is also sensible to this list of [standard Pelican parameters
](https://docs.getpelican.com/en/latest/settings.html):

- `ARCHIVES_SAVE_AS`
- `AUTHOR`
- `AUTHOR_SAVE_AS`
- `AUTHORS_SAVE_AS`
- `CATEGORIES_SAVE_AS`
- `CATEGORY_FEED_ATOM`
- `CATEGORY_FEED_RSS`
- `DEFAULT_LANG`
- `DEFAULT_PAGINATION`
- `DISPLAY_PAGES_ON_MENU`
- `DISPLAY_CATEGORIES_ON_MENU`
- `FEED_ALL_ATOM`
- `FEED_ALL_RSS`
- `FEED_ATOM`
- `FEED_DOMAIN`
- `FEED_RSS`
- `PAGINATION_PATTERNS`
- `SITENAME`
- `SITEURL`
- `TAG_FEED_ATOM`
- `TAG_FEED_RSS`
- `TAGS_SAVE_AS`

## Code Syntax Highlighting

There is two alternatives, all relying on [Pygments syntax
highlighter](https://pygments.org), sharing most features, with some
differences:

| Feature                        | [CodeHilite](https://python-markdown.github.io/extensions/code_hilite/) | [Highlight](https://facelessuser.github.io/pymdown-extensions/extensions/highlight/) |
| :----------------------------- | :---------------------------------------------------------------------: | :----------------------------------------------------------------------------------: |
| Clean copy and paste           |                                    ✅                                    |                                          ✅                                           |
| Line numbering                 |                                    ✅                                    |                                          ✅                                           |
| Right justified numbers        |                                    ✅                                    |                                          ✅                                           |
| Line start offset              |                                    ✅                                    |                                          ✅                                           |
| Multiple line highlight        |                                    ✅                                    |                                          ✅                                           |
| Nth line highlight             |                                    ✅                                    |                                          ✅                                           |
| Filename                       |                                    ✅                                    |                                          ❌                                           |
| Long line wraps                |                                    ✅                                    |                                          ❌                                           |
| Long line overflow (scrollbar) |                                    ❌                                    |                                          ✅                                           |
| Sticky left gutter             |                                    ❌                                    |                                          ✅                                           |
| Line anchors                   |    [WIP @ Pygments](https://github.com/pygments/pygments/pull/1591)     |                                          ❌                                           |

### [Python Markdown CodeHilite](https://python-markdown.github.io/extensions/code_hilite/)

Just add this configuration to `pelicanconf.py`, which allows us to pass
extra options to [Pygments' HTML formatter](https://pygments.org/docs/formatters/#HtmlFormatter):

```python
MARKDOWN = {
    "extension_configs": {
        (…)
        "markdown.extensions.codehilite": {
            "css_class": "codehilite",  # Default
            "linenums": True,
            "linenos": "inline",
            "linespans": "coderow",
            "lineanchors": "L",
            "anchorlinenos": True,
            "wrapcode": True,
        },
        "markdown.extensions.fenced_code": {},
        (…)
    },
}
```

This will render this:

````markdown
```{.shell-session hl_lines="8 11" linenostart="5" linenospecial="3" filename="~/code/foo.log"}
$ cat ./example.markdown
This is the content of the file:
→ java
→ rust
→ haskell
→ javascript

$ cat ./addendum.txt
This is extra content.

$ find ./ -iname "*.markdown" -print -exec bash -c 'cat ./addendum.txt >> "{}"' \;
./example.markdown
$ cat ./example.markdown
This is the content of the file:
→ java
→ rust
→ haskell
→ javascript

This is extra content.

```
````

Into this:

![Plumage Python Markdown CodeHilite rendering](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/codehilite-rendering.jpeg)

### [PyMdown Extensions' Highlight](https://facelessuser.github.io/pymdown-extensions/extensions/highlight/)

Just add this configuration to your `pelicanconf.py`:

```python
MARKDOWN = {
    "extension_configs": {
        (…)
        "pymdownx.highlight": {
            "linenums": True,
            "linenums_style": "pymdownx-inline",
        },
        "pymdownx.superfences": {},
        (…)
    },
}
```

This will render this:

````markdown
```{.shell-session hl_lines="8 11" linenums="5 1 3" filename="~/code/foo.log"}
$ cat ./example.markdown
This is the content of the file:
→ java
→ rust
→ haskell
→ javascript

$ cat ./addendum.txt
This is extra content.

$ find ./ -iname "*.markdown" -print -exec bash -c 'cat ./addendum.txt >> "{}"' \;
./example.markdown
$ cat ./example.markdown
This is the content of the file:
→ java
→ rust
→ haskell
→ javascript

This is extra content.

```
````

Into this:

![Plumage PyMdown Extensions' Highlight rendering](https://raw.githubusercontent.com/kdeldycke/plumage/main/screenshots/highlight-rendering.jpeg)


## CSS customization

TODO: document all kind customization below

### Python code transforms at generation via `pyquery`

### Use of `extra_css`

### Custom `main.scss`

## FAQ

### How can I disable the zoom on images?

All images of an article are zoomable by default. You can deactivate the
magnifying glass per-image by adding a `noZoom` CSS class. So instead of the
following Markdown code:

```markdown
![Image title](/folder/image.png)
```

You have to use the following template to deactivate the zoom of an image:

```markdown
![Image title](/folder/image.png){: .noZoom}
```

### Why is the search not working?

The [official Pelican's `search` plugin](https://github.com/pelican-plugins/search) needs to
be installed.

TODO: Activate search field automaticcaly if the plugin is present.

## License

This software is licensed under the [GNU General Public License v2 or later
(GPLv2+)](https://github.com/kdeldycke/plumage/blob/main/LICENSE).

Copyright (C) 2012-2020 [Kevin Deldycke](https://kevin.deldycke.com) and
[contributors](https://github.com/kdeldycke/plumage/graphs/contributors).

## Third-party assets

The theme embed copies of some external softwares, scripts, libraries and
artworks:

```text
jQuery MGlass v1.1
Copyright (c) 2012 Younès El Biache
Distributed under a MIT license
Source: https://github.com/younes0/jQuery-MGlass
```

```text
Fabric (Plaid)
Copyright (c) 2012 James Basoo
Distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license
Source: https://subtlepatterns.com/fabric-plaid/
```

```text
Cream paper
Copyright (c) 2012 Devin Holmes
Distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license
Source: https://subtlepatterns.com/cream-paper/
```

```text
Feather-alt icon v5.1.0
Copyright (c) 2020 Font Awesome project
Distributed under a Creative Commons Attribution 4.0 International license
Source: https://fontawesome.com/icons/feather-alt?style=solid
```

```text
Macro shot of White Feather
Source: https://unsplash.com/photos/Sw7f58YJbc0
```
