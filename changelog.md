# Changelog

## [4.0.1 (unreleased)](https://github.com/kdeldycke/plumage/compare/v4.0.0...main)

> \[!IMPORTANT\]
> This version is not released yet and is under active development.

- Switch from Poetry to `uv`.

## [4.0.0 (2024-05-17)](https://github.com/kdeldycke/plumage/compare/v3.1.0...v4.0.0)

- Replace Font Awesome by Bootstrap Icons.
- Add support for MyST Markdown. Add new dependency on `pelican-myst-reader`.
- Remove support for `pymdownx` and dependency on `pymdown-extensions`.
- Remove direct dependency on `Markdown`, `pygments`.
- Auto-detect location of `closure.jar` file for `webassets`.
- Move `bump-my-version` configuration to `pyproject.toml`.
- Remove `bump2version` from dev dependencies, and let the external workflows install it.

## [3.1.0 (2023-06-03)](https://github.com/kdeldycke/plumage/compare/v3.0.0...v3.1.0)

- Replace Tipue Search with Stork. Closes #49.
- Replace remote cdnjs version of Bootstrap with local one. Add new NPM dependency on Bootstrap.
- Remove dedicated `search.html` template.
- Reintroduce the `extra_css` block in base template for local customizations.
- Relax Python requirements to `>=3.8`.

## [3.0.0 (2023-03-06)](https://github.com/kdeldycke/plumage/compare/v2.4.0...v3.0.0)

- Add `robots` directives to ignore search engine indexing of drafts & hidden articles and pages.
- Upgrade to Bootstrap 5.3.0-alpha1.
- Upgrade to Font Awesome 6.3.0.
- Upgrade to jQuery 3.6.3.
- Re-introduce dependency on Masonry 4.2.2.
- Remove `fitvids`. It's unmaintained and the modern web stack should not requires it.
- Update dependency to `pelican-webassets` 2.0.0.
- Let `autoprefixer` generates vendor prefixes in CSS.
- Add dependency on `postcss-cli` and `autoprefixer` Node package.
- Auto-install Node.js dependencies via `npm`.
- Auto-configure `webassets` plugins on theme load.
- Auto-format Jinja templates. Add dependency on `djlint`.
- Lint Jinja files with `djlint` instead of `curlylint`.
- Simplify project management: only use the `main` branch, delete `develop`.
- Runs workflows on latest `ubuntu-22.04` and Python `3.11`.
- Add minimal typing.
- Automate version management.
- Add a `.mailmap` file.

## [2.4.0 (2020-12-06)](https://github.com/kdeldycke/plumage/compare/v2.3.0...v2.4.0)

- Add new `CODE_STYLE` option to select code rendering among 30+ styles from
  Pygments.
- Add default favicon.
- Embed and auto-generate all Pygments styles.
- Improve styling of code blocks.
- Remove all custom default and code fonts. Rely on [Bootstrap's native font stack](https://getbootstrap.com/docs/4.1/content/reboot/#native-font-stack).
- Add Pelican version in HTML headers.

## [2.3.0 (2020-11-26)](https://github.com/kdeldycke/plumage/compare/v2.2.0...v2.3.0)

- Replace client-side jQuery calls by server-side Python post-processing to
  apply Bootstrap's CSS utility classes.
- Add dependency on `pyquery`.
- Lint all SCSS and SASS files.
- Lint all YAML files. Add dependency on `yamllint` package.
- Aligns minimal Python version to 3.6, i.e. the one Pelican depends on.
- Add dependency on `black`.
- Keep images optimized.
- Style TOC permalinks produced by Python's `markdown.extensions.toc`.
- Fix blockquote border rendering.
- Test publishing to PyPi in dry-run mode by the way of Poetry.

## [2.2.0 (2020-11-20)](https://github.com/kdeldycke/plumage/compare/v2.1.0...v2.2.0)

- Upgrade to Bootstrap 4.5.3.
- Upgrade to Font Awesome 5.15.1.
- Reduce image size by converting most assets from PNG to JPEG.
- Add support for line numbers and highlights in code samples.
- Add keywords meta tag in articles' header.
- Compile all local CSS and JS files into a single minified file.
- Add support for `.scss` style files. Add dependency on `libsass`.
- Add dependency on `pelican-webassets`, `cssmin` and `closure` packages.
- Remove `extra_css` block in base template.
- Add project header image and logo.
- Remove special font only used for titles, headers and Typogrify ampersands.

## [2.1.0 (2020-10-17)](https://github.com/kdeldycke/plumage/compare/v2.0.0...v2.1.0)

- Add `period_archives.html` template.
- Add support for `similar_posts` plugin.
- Upgrade to `pygment >= 2.7`.
- Fix code block color that made them unreadable.
- Add Monokai style to render code block to increase contrast and
  readability. Set as new default instead of Solarized dark.
- Rename `master` branch to `main`.
- Upgrade to `Poetry >= 1.1.0`.

## [2.0.0 (2020-08-26)](https://github.com/kdeldycke/plumage/compare/v1.1.0...v2.0.0)

- Upgrade to Bootstrap 4.5.2 with bundled popper.js.
- Upgrade to jQuery 3.5.1.
- Upgrade to Tipue Search v7.1.
- Reintroduce local copy of Tipue Search since the project has been
  abandoned.
- Remove dependency on Masonry.
- Remove dependency on ImagesLoaded.
- Remove `FLAT_DESIGN` option.
- Use list group to renders related content at the bottom of articles.
- Move badges above description in project cards.
- Use latest Disqus reference code.
- Do not display Disqus comments for draft articles.
- Sort tags, categories and authors by frequency first, then alphabeticcaly.
- Ignore empty years in archive page.
- Display number of articles per year in archive page.
- Upgrade to latest Google Analytics code snippet.
- Remove `GA_COOKIE_DOMAIN` option.
- Remove support for Google Search and `GOOGLE_SEARCH` option.
- Add style support for `pymdownx.emoji`.
- Add style support for `markdown.extensions.admonition`.
- Add direct dependency on pygments.
- Auto upgrade pygment styles.

## [1.1.0 (2020-08-12)](https://github.com/kdeldycke/plumage/compare/v1.0.0...v1.1.0)

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

## [1.0.0 (2020-08-01)](https://github.com/kdeldycke/plumage/compare/v0.9.0...v1.0.0)

- Package Plumage in a python module.
- Distribute Plumage on PyPi.
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

## [0.9.0 (2017-03-22)](https://github.com/kdeldycke/plumage/compare/v0.8.0...v0.9.0)

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

## [0.8.0 (2016-06-22)](https://github.com/kdeldycke/plumage/compare/v0.7.0...v0.8.0)

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

## [0.7.0 (2015-12-28)](https://github.com/kdeldycke/plumage/compare/v0.6.0...v0.7.0)

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

## [0.6.0 (2015-05-30)](https://github.com/kdeldycke/plumage/compare/v0.5.0...v0.6.0)

- Fix favicon rendering.

## [0.5.0 (2015-05-25)](https://github.com/kdeldycke/plumage/compare/v0.4.0...v0.5.0)

- Add support for piwik.
- Upgrade to jQuery 2.1.3.
- Upgrade to Masonry 3.3.0.
- Upgrade to fitvids 1.1.0.
- Upgrade to Magnific Popup 1.0.0.

## [0.4.0 (2014-02-15)](https://github.com/kdeldycke/plumage/compare/v0.3.0...v0.4.0)

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

## [0.3.0 (2013-08-16)](https://github.com/kdeldycke/plumage/compare/v0.2.0...v0.3.0)

- Add auto-zoom of images based on Magnific Popup.
- Let the content take the available width if there is no right or left
  sidebars.
- Add an dynamic feed link in footer.
- Do not wrap code in code blocks.
- Fix code highlight for older Pelican versions.
- Escape and strip tags in all title attributes.
- Style ampersands for those using typogrify.

## [0.2.0 (2013-07-09)](https://github.com/kdeldycke/plumage/compare/v0.1.0...v0.2.0)

- Make theme fully generic through the use of variables.
- Replace custom navigation with Pelican's neighbors plugin.
- Add screenshot.
- Update documentation.

## [0.1.0 (2013-07-07)](https://github.com/kdeldycke/plumage/compare/v0.0.0...v0.1.0)

- Theme has now a name: Plumage.
- Move the theme out of my [blog repository](https://github.com/kdeldycke/kevin-deldycke-blog) to its own repository.
- Theme is now generic enough. Update TODO-list accordingly.

## [0.0.0 (2012-12-23)](https://github.com/kdeldycke/plumage/commit/70df9b)

- First commit.
