# Changelog

## [`5.0.1.dev0` (unreleased)](https://github.com/kdeldycke/plumage/compare/v5.0.0...main)

> [!WARNING]
> This version is **not released yet** and is under active development.

## [`5.0.0` (2026-08-09)](https://github.com/kdeldycke/plumage/compare/v4.0.0...v5.0.0)

> [!NOTE]
> `5.0.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/5.0.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v5.0.0).

- **Breaking:** Drop support for Python 3.9 and 3.10. The floor is now Python 3.11.
- **Breaking:** Remove jQuery, `magnific-popup` and `mglass`, and the image auto-zoom they powered.
- **Breaking:** Only support native Pygments syntax highlighting. The legacy `.codehilite` class is no longer styled.
- **Breaking:** Remove inlining and minification of JavaScript assets, and the unmaintained `closure` dependency they relied on.
- Add 14 Pygments styles, including `dracula`, `github-dark`, `gruvbox-dark` and `nord`. Remove the `stata` one.
- Wrap the header, navigation bar and footer of `base.html` in overridable `header`, `nav` and `footer` blocks, and give `page.html` a `page_content` block.
- Support Pelican's own `ANALYTICS` setting, holding whatever markup an analytics provider hands you. `GOOGLE_ANALYTICS` still emits its `gtag.js` snippet.
- Add a collapsible generation details block in the footer, listing the Pelican and Plumage versions. The latter is exposed as a new `PLUMAGE_VERSION` template variable.
- Add a meta description, taken from the entry's `Description:` metadata or its summary, with `SITESUBTITLE` standing in site-wide.
- Advertise translations to crawlers, with `hreflang` on the `<head>` links and the visible ones alike.
- Show when an article was last modified, next to the date it was published.
- Show a site's pages, or a short notice, on an index with no article to list.
- Serve every third-party asset from the site rather than from a CDN, declared in `plumage/package.json` so Dependabot bumps them. A new `sync-vendored-assets` job refreshes the copies, which had been frozen wherever they were first written.
- Require Pelican 4.11, and develop against 4.12. A 4.12 floor is uninstallable while `pelican-myst-reader` caps `myst-parser` below `5.0.0`, holding `docutils` under the `0.22` that 4.12 needs.
- Replace every `~=` requirement with `>=`, so no dependency carries an upper bound any more.
- Switch from Poetry to `uv`, and build with the `uv_build` backend. Dropping `node_modules` from the distribution shrinks the wheel from 17.4 MB to 0.4 MB.
- Declare the test dependencies as a PEP 735 group, so neither `plumage[test]` nor `plumage[djlint]` is published to PyPI.
- Declare the license as an SPDX expression, and ship the license file in the package.
- Update the webassets pipeline's Node dependencies: Bootstrap to `5.3.8`, PostCSS to `8.5.25`, Autoprefixer to `10.5.4` and `postcss-cli` to `11.0.1`. The PostCSS `8.5` series closes an XSS through an unescaped `</style>`.
- Move analytics code just below the `<head>` element, and all other JavaScript to the bottom of the page.
- Mark up dates with `<time datetime>` instead of `<abbr title>`. `title` still carries the timestamp, so the hover tooltip is unchanged.
- Announce the current navigation entry with `aria-current`, in place of a visually-hidden label.
- Follow the color scheme in the page surround, the footer, heading shadows and the avatar, instead of the light-mode values they hard-coded.
- Fix syntax highlighting silently not applying to code blocks. The MyST reader's docutils renderer omits the `.highlight` container every Pygments stylesheet selects through, so highlighting no longer depends on whether a page happens to carry an intra-site link.
- Fix the build crashing on an article with no category, which Pelican 4.12.0 made reachable by binding the name to `None` instead of leaving it out.
- Fix every page of a multilingual site being labelled with `DEFAULT_LANG`. The `lang` attribute now sits in an `html_lang` block the content templates override.
- Fix the navigation bar never highlighting the current category.
- Fix the paginator emitting a whitespace-only `rel` attribute on pages carrying no link relation.
- Fix the `full-width` layout: the main content now spans all 12 columns, and the block above it lines up with it instead of being capped at half width.
- Fix the search box icon, left behind by the Font Awesome to Bootstrap Icons migration.
- Fix the search reset button rendering as a blank disc under a dark color scheme.
- Fix three declarations in `code.scss` naming CSS variables Bootstrap 5 moved behind a `--bs-` prefix: a code block's filename label, the line-number gutter border, and highlighted line-number backgrounds.
- Fix the avatar's flip rendering flat. Its `perspective` was set to a bare `600`, and a number with no unit is not a length.
- Take the code block's line-number gutter background from whichever stylesheet `CODE_STYLE` selects, instead of a hard-coded Monokai color.
- Stop badges extending `.btn` and `.btn-light`, which drew a border in a fixed light gray around every one of them.
- Style the search reset button and the search progress bar through the `--bs-btn-close-filter` and `--bs-progress-height` custom properties Bootstrap `5.3.4` introduced.
- Replace the deprecated `text-muted` and the hard-coded `text-dark` in the footer with color scheme aware utilities.
- Add the missing `alt` text on the site thumbnail.
- Ignore anything that is not a stylesheet when collecting `ALL_CODE_STYLES`.
- Drop the stale Python 3.10 classifier, left over from the move to a 3.11 floor.
- Remove the `pelican-image-process` external-images workaround, the never-read `plumage/postcss.config.js`, and the `box-sizing: content-box !important` override on code blocks.
- Collapse the seven rules revealing a heading's anchor link into one, using `:is()`, and drop the `!important` they carried.
- Add a test suite covering settings validation, the HTML transforms, the favicon assets and the rendered templates, across both of the MyST reader's renderers. Run it with `uv run --group test -- pytest`. Closes [#85](https://github.com/kdeldycke/plumage/issues/85).
- Run the test suite on Python 3.11 to 3.14 through a new `tests.yaml` workflow.
- Document code highlighting, admonitions, the `LAYOUT` setting, and every block the theme exposes.
- Document theme development, recommend [Jampack](https://jampack.divriots.com) for asset optimization, and rewrite the installation instructions around `uv`.
- Manage the repository with `repomatic`, and run the theme's own CI jobs on `ubuntu-24.04`.
- Pin every tool invoked from a workflow to an exact version, and declare the Node version every job running `npm` uses.
- Give Dependabot a cooldown, and configure stylelint and djlint to report only findings that apply to the theme.
- Generate the Pygments stylesheets through the library's own API, in a job split from CSS formatting.
- Lint and autofix all stylesheets in a single stylelint call each, instead of one per file extension.
- Stop spell-checking the vendored minified bundles.
- Declare the PyYAML stubs alongside PyYAML itself, so type-checking the test suite's workflow parsing no longer fails on the import.

## [`4.0.0` (2024-05-18)](https://github.com/kdeldycke/plumage/compare/v3.1.0...v4.0.0)

> [!NOTE]
> `4.0.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/4.0.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v4.0.0).

- Replace Font Awesome by Bootstrap Icons.
- Add support for MyST Markdown. Add new dependency on `pelican-myst-reader`.
- Rework right sidebar, tags and categories.
- Rework header permalinks.
- Remove support for `pymdownx` and dependency on `pymdown-extensions`.
- Remove direct dependency on `Markdown` and `pygments`.
- Auto-detect location of `closure.jar` file for `webassets`.
- Move `bump-my-version` configuration to `pyproject.toml`.
- Remove `bump2version` from dev dependencies, and let the external workflows install it.
- Drop support of Python 3.8.

## [`3.1.0` (2023-06-03)](https://github.com/kdeldycke/plumage/compare/v3.0.0...v3.1.0)

> [!NOTE]
> `3.1.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/3.1.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v3.1.0).

- Replace Tipue Search with Stork. Closes #49.
- Replace remote cdnjs version of Bootstrap with local one. Add new NPM dependency on Bootstrap.
- Remove dedicated `search.html` template.
- Reintroduce the `extra_css` block in base template for local customizations.
- Relax Python requirements to `>=3.8`.

## [`3.0.0` (2023-03-08)](https://github.com/kdeldycke/plumage/compare/v2.4.0...v3.0.0)

> [!NOTE]
> `3.0.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/3.0.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v3.0.0).

- Add `robots` directives to ignore search engine indexing of drafts & hidden articles and pages.
- Upgrade to Bootstrap 5.3.0-alpha1.
- Upgrade to Font Awesome 6.3.0.
- Upgrade to jQuery 3.6.3.
- Re-introduce dependency on Masonry 4.2.2.
- Remove `fitvids`. It's unmaintained and the modern web stack should not require it.
- Remove default underline on links.
- Strip tags from article summaries.
- Update dependency to `pelican-webassets` 2.0.0.
- Let `autoprefixer` generate vendor prefixes in CSS.
- Add dependency on `postcss-cli` and `autoprefixer` Node packages.
- Auto-install Node.js dependencies via `npm`.
- Auto-configure `webassets` plugins on theme load.
- Auto-format Jinja templates. Add dependency on `djlint`.
- Lint Jinja files with `djlint` instead of `curlylint`.
- Simplify project management: only use the `main` branch, delete `develop`.
- Runs workflows on latest `ubuntu-22.04` and Python `3.11`.
- Add minimal typing.
- Automate version management.
- Add a `.mailmap` file.

## [`2.4.0` (2020-12-06)](https://github.com/kdeldycke/plumage/compare/v2.3.0...v2.4.0)

> [!NOTE]
> `2.4.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/2.4.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v2.4.0).

- Add new `CODE_STYLE` option to select code rendering among 30+ styles from
  Pygments.
- Add default favicon.
- Embed and auto-generate all Pygments styles.
- Improve styling of code blocks.
- Remove all custom default and code fonts. Rely on [Bootstrap's native font stack](https://getbootstrap.com/docs/4.1/content/reboot/#native-font-stack).
- Add Pelican version in HTML headers.
- Add hack fixing external images bug from `pelican-image-process` plugin.

## [`2.3.0` (2020-11-26)](https://github.com/kdeldycke/plumage/compare/v2.2.0...v2.3.0)

> [!NOTE]
> `2.3.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/2.3.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v2.3.0).

- Replace client-side jQuery calls by server-side Python post-processing to
  apply Bootstrap's CSS utility classes.
- Add dependency on `pyquery`.
- Lint all SCSS and SASS files.
- Lint all YAML files. Add dependency on `yamllint` package.
- Align minimal Python version to 3.6, the one Pelican depends on.
- Add dependency on `black`.
- Keep images optimized.
- Style TOC permalinks produced by Python's `markdown.extensions.toc`.
- Fix blockquote border rendering.
- Test publishing to PyPI in dry-run mode by the way of Poetry.

## [`2.2.0` (2020-11-20)](https://github.com/kdeldycke/plumage/compare/v2.1.0...v2.2.0)

> [!NOTE]
> `2.2.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/2.2.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v2.2.0).

- Upgrade to Bootstrap 4.5.3.
- Upgrade to Font Awesome 5.15.1.
- Reduce image size by converting most assets from PNG to JPEG.
- Add support for line numbers and highlights in code samples.
- Support both CodeHilite and Highlight Markdown extensions for code rendering.
- Add keywords meta tag in articles' header.
- Add generator meta tag to promote Pelican.
- Compile all local CSS and JS files into a single minified file.
- Add support for `.scss` style files. Add dependency on `libsass`.
- Add dependency on `pelican-webassets`, `cssmin` and `closure` packages.
- Remove `extra_css` block in base template.
- Add project header image and logo.
- Remove special font only used for titles, headers and Typogrify ampersands.

## [`2.1.0` (2020-10-17)](https://github.com/kdeldycke/plumage/compare/v2.0.0...v2.1.0)

> [!NOTE]
> `2.1.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/2.1.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v2.1.0).

- Add `period_archives.html` template.
- Add support for `similar_posts` plugin.
- Upgrade to `pygments >= 2.7`.
- Fix code block color that made them unreadable.
- Add Monokai style to render code block to increase contrast and
  readability. Set as new default instead of Solarized dark.
- Rename `master` branch to `main`.
- Upgrade to `Poetry >= 1.1.0`.

## [`2.0.0` (2020-08-26)](https://github.com/kdeldycke/plumage/compare/v1.1.0...v2.0.0)

> [!NOTE]
> `2.0.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/2.0.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v2.0.0).

- Upgrade to Bootstrap 4.5.2 with bundled popper.js.
- Upgrade to jQuery 3.5.1.
- Upgrade to Tipue Search v7.1.
- Reintroduce local copy of Tipue Search since the project has been
  abandoned.
- Remove dependency on Masonry.
- Remove dependency on ImagesLoaded.
- Remove `FLAT_DESIGN` option.
- Use list group to render related content at the bottom of articles.
- Move badges above description in project cards.
- Use latest Disqus reference code.
- Do not display Disqus comments for draft articles.
- Sort tags, categories and authors by frequency first, then alphabetically.
- Ignore empty years in archive page.
- Display number of articles per year in archive page.
- Upgrade to latest Google Analytics code snippet.
- Remove `GA_COOKIE_DOMAIN` option.
- Remove support for Google Search and `GOOGLE_SEARCH` option.
- Add style support for `pymdownx.emoji`.
- Add style support for `markdown.extensions.admonition`.
- Support both `pymdownx` and `codehilite` code highlighters.
- Add direct dependency on Pygments.
- Auto upgrade Pygments styles.

## [`1.1.0` (2020-08-11)](https://github.com/kdeldycke/plumage/compare/v1.0.0...v1.1.0)

> [!NOTE]
> `1.1.0` is available on [🐍 PyPI](https://pypi.org/project/plumage/1.1.0/) and [🐙 GitHub](https://github.com/kdeldycke/plumage/releases/tag/v1.1.0).

- Replace Droid Sans Mono font by Source Code Pro.
- Remove support for Piwik as Pelican does.
- Upgrade to Bootstrap 3.4.1.
- Upgrade to Font Awesome 5.14.0.
- Upgrade to fitvids 1.2.0.
- Upgrade to Masonry 4.2.2.
- Upgrade to ImagesLoaded 4.1.4.
- Bundle API calls to Google Fonts.
- Add integrity checks for assets from CDNjs.
- Fix Font Awesome 5 icon rendering.
- Fix static search.
- Document all features in the readme by the way of screenshots.
- Lint Jinja templates.
- Lint and autofix CSS files.
- Use 3-parts semantic versioning.
- Add Hacker News to the list of recognized links.
- Add link to author list along tags, categories and dates.
- Fix link icon alignment in footer.

## [`1.0.0` (2020-08-01)](https://github.com/kdeldycke/plumage/compare/v0.9.0...v1.0.0)

> [!NOTE]
> `1.0.0` is the *first version* available on [🐍 PyPI](https://pypi.org/project/plumage/1.0.0/).

- Package Plumage in a python module.
- Distribute Plumage on PyPI.
- Fix issue with Pelican 4.x.
- Update to Font Awesome 5.
- Add new `MANUAL_LINKS` setting.
- Add proper support of `PAGINATION_PATTERNS` setting.
- Replace dead `better-idea.org` service by [Google favicons service](https://www.google.com/s2/favicons).
- Add support for Twitter icon in links.
- Keep Python dependencies up to date thanks to dependabot.
- Keep GitHub labels in sync.
- Always test package builds on commit and PR events.
- Automate parts of package release.

## [`0.9.0` (2017-03-22)](https://github.com/kdeldycke/plumage/compare/v0.8.0...v0.9.0)

- Upgrade Bootstrap to 3.3.7.
- Add a new `FLAT_DESIGN` setting.
- Upgrade to Font Awesome 4.7.0.
- Upgrade to ImagesLoaded 4.1.1.
- Upgrade to Masonry 4.1.1.
- Replace unsupported vertical tabs by collapsible panels in date-based index
  page.
- Fix display of pages in menu via the dedicated `DISPLAY_PAGES_ON_MENU`
  option.
- Fix highlighting of current active item in navbar.
- Rename `GOOGLE_ANALYTICS_PROPERTY` setting to `GA_COOKIE_DOMAIN`.
- Prevent mixed content when using Google search.
- Add support for `DISPLAY_CATEGORIES_ON_MENU` setting.
- Update Atom and RSS link descriptions.
- Add support for multiple authors.
- Add support for `AUTHORS_SAVE_AS` setting.
- List all available Atom and RSS feeds on each page in the footer.
- Load external resources via HTTPS when available.
- Support title anchor links as produced by [Markdown ToC extension](https://pythonhosted.org/Markdown/extensions/toc.html).

## [`0.8.0` (2016-06-22)](https://github.com/kdeldycke/plumage/compare/v0.7.0...v0.8.0)

- Remove legacy Google Analytics tracking code.
- Rename `GOOGLE_ANALYTICS_UNIVERSAL` option by `GOOGLE_ANALYTICS` and
  `GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY` by `GOOGLE_ANALYTICS_PROPERTY`.
- Set default `GOOGLE_ANALYTICS_PROPERTY` value to `"auto"`.
- Allow deactivation of zoom on article's images.
- Upgrade to Font Awesome 4.6.3.
- Upgrade to ImagesLoaded 4.1.0.
- Upgrade to Masonry 4.1.0.
- Upgrade to Magnific Popup 1.1.0.
- Upgrade to jQuery 2.2.4.
- Ditch `grabicon` in favor of the free [Favicon Finder
  ](https://icons.better-idea.org) web service.
- Rename `GRAB_ICONS` option to `FAVICON_LINKS`.
- Enable favicon fetching by default.
- Fallback on default external link icon if none found.
- Remove local copy of Tipue Search assets. Rely on CDNjs instead.

## [`0.7.0` (2015-12-28)](https://github.com/kdeldycke/plumage/compare/v0.6.0...v0.7.0)

- Add option to bypass grabicon.com web service.
- Add static search based on Tipue Search.
- Add new `LINKS_WIDGET_NAME` and `SOCIAL_WIDGET_NAME` options to mirror
  upcoming Pelican 3.7.
- Align Piwik and Google Analytics code to Pelican's `notmyidea` theme.
- Add support for newer Google Analytics Universal embed code, via new
  `GOOGLE_ANALYTICS_UNIVERSAL` and `GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY`
  options.
- Upgrade to jQuery 2.1.4.
- Upgrade to Masonry 3.3.2.
- Remove `PDF_PROCESSOR` option now that plugin is out of core.

## [`0.6.0` (2015-05-30)](https://github.com/kdeldycke/plumage/compare/v0.5.0...v0.6.0)

- Fix favicon rendering.

## [`0.5.0` (2015-05-25)](https://github.com/kdeldycke/plumage/compare/v0.4.0...v0.5.0)

- Add support for piwik.
- Upgrade to jQuery 2.1.3.
- Upgrade to Masonry 3.3.0.
- Upgrade to fitvids 1.1.0.
- Upgrade to Magnific Popup 1.0.0.

## [`0.4.0` (2014-02-15)](https://github.com/kdeldycke/plumage/compare/v0.3.0...v0.4.0)

- Allow grouping of projects.
- Add option to override disclaimer notice.
- Generate tags, categories and archives URLs depending on site
  configuration.
- Sort out inactive projects to the bottom of the project list.
- Drop support of old browsers.
- Move from jQuery 1.x to 2.x.
- Use [latest Google Analytics
  ](https://developers.google.com/analytics/devguides/collection/upgrade/)
  tracking code.
- Upgrade to Font Awesome 4.0.3.
- Upgrade to Masonry 3.1.2.
- Upgrade to ImagesLoaded 3.0.4.
- Upgrade to Magnific Popup 0.9.9.

## [`0.3.0` (2013-08-16)](https://github.com/kdeldycke/plumage/compare/v0.2.0...v0.3.0)

- Add auto-zoom of images based on Magnific Popup.
- Render external links with Font Awesome icons instead of fetched favicons.
- Let the content take the available width if there is no right or left
  sidebars.
- Add a dynamic feed link in footer.
- Do not wrap code in code blocks.
- Fix code highlight for older Pelican versions.
- Escape and strip tags in all title attributes.
- Style ampersands for those using typogrify.

## [`0.2.0` (2013-07-09)](https://github.com/kdeldycke/plumage/compare/v0.1.0...v0.2.0)

- Make theme fully generic through the use of variables.
- Replace custom navigation with Pelican's neighbors plugin.
- Remove support for GoSquared analytics.
- Add screenshot.
- Update documentation.

## [`0.1.0` (2013-07-07)](https://github.com/kdeldycke/plumage/compare/v0.0.0...v0.1.0)

- Theme has now a name: Plumage.
- Move the theme out of my [blog repository](https://github.com/kdeldycke/kevin-deldycke-blog) to its own repository.
- Theme is now generic enough. Update TODO-list accordingly.

## [`0.0.0` (2012-12-23)](https://github.com/kdeldycke/plumage/commit/70df9b)

- First commit.
