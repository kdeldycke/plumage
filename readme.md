<p align="center">
  <a href="https://github.com/kdeldycke/plumage/">
    <img src="https://github.com/kdeldycke/plumage/raw/main/docs/assets/plumage-header-logo.jpeg" alt="Plumage, a Pelican theme">
  </a>
</p>

Plumage is a clean and tidy theme for [Pelican](https://getpelican.com), a
static site generator.

I initially created this theme for [my blog](https://kevin.deldycke.com), but
it is now generic enough to be used by anyone.

## Features

- Standard Pelican views:

  |      ![Plumage article view](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/article.jpeg)      | ![Plumage categories view](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/categories.jpeg) | ![Plumage tiered tag list view](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/tiered-tags.jpeg) |
  | :------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------: |
  |                                                       Article                                                        |                                                    Categories                                                    |                                                    Tiered tag list                                                     |
  |     ![Plumage archive view](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/archives.jpeg)      |        ![Plumage tag view](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/tag.jpeg)        |       ![Plumage authors view](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/authors.jpeg)       |
  |                                             Collapsible yearly archives                                              |                                                 Tagged articles                                                  |                                                        Authors                                                         |
  | ![Plumage archive view](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/browse-content-by.jpeg) |                                                                                                                  |                                                                                                                        |
  |                                               Faceted article browsing                                               |                                                                                                                  |                                                                                                                        |

- Projects template:

  |             ![Plumage projects: code showcase](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/projects-code.jpeg)              |             ![Plumage projects: videos showcase](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/projects-videos.jpeg)              |             ![Plumage projects: themes showcase](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/projects-themes.jpeg)              |
  | :--------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: |
  | Code showcase ([source](https://github.com/kdeldycke/kevin-deldycke-blog/blob/ebe0d17a59730457c3016dff77fdfa799a80d756/content/templates/code.html)) | Videos showcase ([source](https://github.com/kdeldycke/kevin-deldycke-blog/blob/f778998376fa5c68f1a02129884b89592b641777/content/templates/videos.html)) | Themes showcase ([source](https://github.com/kdeldycke/kevin-deldycke-blog/blob/f778998376fa5c68f1a02129884b89592b641777/content/templates/themes.html)) |

- Based on [Bootstrap v5](https://getbootstrap.com).

- [Code syntax highlighting](#code-syntax-highlighting) with [30+ styles](https://github.com/kdeldycke/plumage/tree/main/plumage/static/css/pygments).

- Site-wide static search via [Stork](https://stork-search.net).

- Bare YouTube links in articles gets rendered as embedded videos:

  ![Plumage YouTube link](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/youtube-link.jpeg)

- Direct link to edit articles on GitHub:

  ![Plumage GitHub edit link](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/github-edit-link.jpeg)

- Magnifying glass overlays on images and zoom:

  ![Plumage image magnifying glass](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/magnifying-glass.jpeg)
  ![Plumage image zoom](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/zoom.jpeg)

- External assets (Bootstrap, …) relies on [CDNjs](https://cdnjs.com/about).

- Disqus integration:

  ![Plumage disqus comments](https://raw.githubusercontent.com/kdeldycke/plumage/main/docs/assets/disqus.jpeg)

## Plugins

Plumage has built-in support for the following plugins and extensions:

| Plugin name                                                                                     | Type               | Status   | Notes                                                                                                         |
| :---------------------------------------------------------------------------------------------- | :----------------- | :------- | :------------------------------------------------------------------------------------------------------------ |
| [`pelican-neighbors`](https://github.com/pelican-plugins/neighbors)                             | Pelican plugin     | Optional |                                                                                                               |
| [`pelican-related-posts`](https://github.com/pelican-plugins/related-posts)                     | Pelican plugin     | Optional |                                                                                                               |
| [`pelican-similar-posts`](https://github.com/pelican-plugins/similar-posts)                     | Pelican plugin     | Optional |                                                                                                               |
| [`pelican-search`](https://github.com/pelican-plugins/search)                                   | Pelican plugin     | Optional |                                                                                                               |
| [`pelican-webassets`](https://github.com/pelican-plugins/webassets)                             | Pelican plugin     | Required |                                                                                                               |
| [`markdown.extensions.admonition`](https://python-markdown.github.io/extensions/admonition/)    | Markdown extension | Optional | Re-style admonitions into [alerts](https://getbootstrap.com/docs/4.5/components/alerts/).                     |
| [`markdown.extensions.toc`](https://python-markdown.github.io/extensions/toc/#usage)            | Markdown extension | Optional | Adds permalink anchors to article's subtitles.                                                                |
| [`typogrify`](https://pypi.python.org/pypi/typogrify)                                           | Pelican builtin    | Optional | Style ampersands.                                                                                             |

## Installation

```shell-session
$ python -m pip install uv
$ uv venv
$ source .venv/bin/activate
$ uv pip install .
```

Then, once you're done installing the `plumage` module, update your `pelicanconf.py` file to reference the module:

```python
import plumage

THEME = plumage.get_path()
```

On first run, Plumage will try to install [Node.js package dependencies](https://github.com/kdeldycke/plumage/blob/main/plumage/package.json) via the `npm` CLI:

```shell-session
$ uv run -- pelican --verbose ./content
(…)
WARNING: postcss CLI not found.
-> Install Plumage's Node.js dependencies from (…)/plumage/package.json:
  |   {
  |     "name": "plumage-webassets-pipeline",
  |     "description": "Plumage dependencies for the webassets compilation pipeline.",
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

Plumage can be customized by adding these optional parameters to your
`pelicanconf.py` file:

| Setting name                                                                                  | Default value | Description                                                                                                                                                    |
| :-------------------------------------------------------------------------------------------- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ARTICLE_EDIT_LINK`                                                                           |               | Generate an edit link besides each article. Can use `%(slug)s` to include dynamic article's slug in the link.                                                  |
| `CODE_STYLE`                                                                                  | `"monokai"`   | Pygments' style ID. Choose one from `uv run -- pygmentize -L styles`.                                                                                         |
| `COPYRIGHT`                                                                                   |               | Additional copyright statement to add in the third column of the footer.                                                                                       |
| `DISCLAIMER`                                                                                  |               | Override the disclaimer notice that gets displayed at the fourth column of the footer.                                                                         |
| [`DISQUS_SITENAME`](http://docs.getpelican.com/en/stable/settings.html#DISQUS_SITENAME)       |               | Pelican can handle Disqus comments. Specify the Disqus sitename identifier here.                                                                               |
| `FAVICON_LINKS`                                                                               | `True`        | Fetch link's icons from [Google's favicons webservice](https://www.google.com/s2/favicons).                                                                    |
| [`GOOGLE_ANALYTICS`](http://docs.getpelican.com/en/stable/settings.html#GOOGLE_ANALYTICS)     |               | Set to `UA-XXXXXX-Y` Property's tracking ID to activate Google Analytics.                                                                                      |
| `LEFT_SIDEBAR`                                                                                |               | HTML content to put as-is in the left sidebar.                                                                                                                 |
| [`LINKS_WIDGET_NAME`](http://docs.getpelican.com/en/stable/settings.html#LINKS_WIDGET_NAME)   | `"Links"`     | Allows override of the name of the links widget.                                                                                                               |
| [`LINKS`](http://docs.getpelican.com/en/stable/settings.html#LINKS)                           |               | A list of tuples (Title, URL) for links to appear in the second column of the footer.                                                                          |
| [`MANUAL_LINKS`](http://docs.getpelican.com/en/stable/settings.html#MANUAL_LINKS)             |               | When enabling this, you must pass the links (in LINKS & SOCIAL settings) not as tuples anymore, but as list, where every entry is formatted as you like        |
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

Syntax highlighting is produced by [Pygments](https://pygments.org).

See [MyST Markdown code syntax](https://mystmd.org/guide/code) for more details.

## CSS customization

TODO: document all kind customization below

### Python code transforms at generation via `pyquery`

### Use of `extra_css`

### Custom `main.scss`

## Performances

The theme does not try to implements tricks and optimization beyond reasonable efforts.

This was attempted in the past which limited success. That's because it is hard to find up-to-date and maintained projects in the Python ecosystem.

Instead, I advise relying on external all-in-one optimization tools like [Jampack](https://jampack.divriots.com).

After a build, just call it on the generated static content like so:
```shell-session
$ npx @divriots/jampack ./output
```

## FAQ

### Why is the search not working?

The [official Pelican's `search` plugin](https://github.com/pelican-plugins/search) needs to
be installed.

TODO: Activate search field automaticcaly if the plugin is present.

## Development

If you need to work both on the content of your website and the theme, you need to:

- Get a local copy of the theme outside your website virtualenv:

  ```shell-session
  $ cd ..
  $ git clone https://github.com/kdeldycke/plumage.git
  $ cd ./my-pelican-website
  ```

- Change the `plumage` dependency in you website's `pyproject.toml` from:

  ```toml
  dependencies = [
      ...
      "plumage <anything>",
      ...
  ]
  ```

  To:

  ```toml
  dependencies = [
      ...
      "plumage",
      ...
  ]
  ```

- Also add this new section in the same `pyproject.toml`, to [force `uv` to pick up the latest local copy](https://github.com/astral-sh/uv/issues/2844#issuecomment-2241196371):

  ```toml
  [tool.uv.sources]
  plumage = { path = "../plumage", editable = true }
  ```

## License

This software is licensed under the [GNU General Public License v2 or later
(GPLv2+)](https://github.com/kdeldycke/plumage/blob/main/LICENSE).

Copyright © 2012-2024 [Kevin Deldycke](https://kevin.deldycke.com) and
[contributors](https://github.com/kdeldycke/plumage/graphs/contributors).

## Third-party assets

The theme embed copies of some external software, scripts, libraries and
artworks:

```text
Fabric (Plaid)
Copyright © 2012 James Basoo
Distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license
Source: https://subtlepatterns.com/fabric-plaid/
```

```text
Cream paper
Copyright © 2012 Devin Holmes
Distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license
Source: https://subtlepatterns.com/cream-paper/
```

```text
Feather-alt icon v5.1.0
Copyright © 2020 Font Awesome project
Distributed under a Creative Commons Attribution 4.0 International license
Source: https://fontawesome.com/icons/feather-alt?style=solid
```

```text
Macro shot of White Feather
Source: https://unsplash.com/photos/Sw7f58YJbc0
```
