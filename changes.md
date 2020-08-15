Changelog
=========

* [**v1.1.1**
  (unreleased)](https://github.com/kdeldycke/plumage/compare/v1.1.0...develop)
  * Upgrade to Bootstrap 4.5.2.
  * Upgrade to jQuery 3.5.1.
  * Add popper.js 2.4.4.
  * Remove `FLAT_DESIGN` option.

* [**v1.1.0**
  (2020-08-12)](https://github.com/kdeldycke/plumage/compare/v1.0.0...v1.1.0)
  * Replace Droid Sans Mono font by Source Code Pro.
  * Remove support for Piwik as Pelican does.
  * Upgrade to Bootstrap 3.4.1.
  * Upgrade to Font Awesome 5.14.0.
  * Upgrade to fitvids 1.2.0.
  * Upgrade to Masonry 4.2.2.
  * Upgrade to ImagesLoaded 4.1.4.
  * Bundle API calls to Google Fonts.
  * Add integrity checks for assets from CDNjs.
  * Fix Font Awesome 5 icon rendering.
  * Fix static search.
  * Document all features in the readme by the way of screenshots.
  * Lint Jinja templates.
  * Lint and autofix CSS files.
  * Use 3-parts semantic versionning.
  * Add Hacker News to the list of recognized links.
  * Add link to author list along tags, categories and dates.
  * Fix link icon alignment in footer.

* [**v1.0.0**
  (2020-08-01)](https://github.com/kdeldycke/plumage/compare/v0.9.0...v1.0.0)
  * Package Plumage in a python module.
  * Distribute Plumage on PyPi.
  * Fix issue with Pelican 4.x.
  * Update to Font Awesome 5.
  * Add new `MANUAL_LINKS` setting.
  * Add proper support of `PAGINATION_PATTERNS` setting.
  * Replace dead `better-idea.org` service by [Google favicons service
    ](https://www.google.com/s2/favicons).
  * Add support for Twitter icon in links.
  * Keep Python dependencies up to date thanks to dependabot.
  * Keep GitHub labels in sync.
  * Always test package builds on commit and PR events.
  * Automate parts of package release.

* [**v0.9.0**
  (2017-03-22)](https://github.com/kdeldycke/plumage/compare/v0.8.0...v0.9.0)
  * Upgrade Bootstrap to 3.3.7.
  * Add a new `FLAT_DESIGN` setting.
  * Upgrade to Font Awesome 4.7.0.
  * Upgrade to ImagesLoaded 4.1.1.
  * Upgrade to Masonry 4.1.1.
  * Replace unsupported vertical tabs by collapsible panels in date-based index
    page.
  * Fix display of pages in menu via the dedicated `DISPLAY_PAGES_ON_MENU`
    option.
  * Fix highlighting of current active item in navbar.
  * Rename `GOOGLE_ANALYTICS_PROPERTY` setting to `GA_COOKIE_DOMAIN`.
  * Prevent mixed content when using Google search.
  * Add support for `DISPLAY_CATEGORIES_ON_MENU` setting.
  * Update Atom and RSS link descriptions.
  * Add support for multiple authors.
  * Add support for `AUTHORS_SAVE_AS` setting.
  * List all available Atom and RSS feeds on each page in the footer.
  * Load external resources via HTTPS when available.
  * Support title anchor links as produced by [Markdown ToC
  extension](https://pythonhosted.org/Markdown/extensions/toc.html).

* [**v0.8.0**
  (2016-06-22)](https://github.com/kdeldycke/plumage/compare/v0.7.0...v0.8.0)
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
    ](https://icons.better-idea.org) web service.
  * Rename `GRAB_ICONS` option to `FAVICON_LINKS`.
  * Enable favicon fetching by default.
  * Fallback on default external link icon if none found.
  * Remove local copy of Tipue Search assets. Rely on CDNjs instead.

* [**v0.7.0**
  (2015-12-28)](https://github.com/kdeldycke/plumage/compare/v0.6.0...v0.7.0)
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

* [**v0.6.0**
  (2015-05-30)](https://github.com/kdeldycke/plumage/compare/v0.5.0...v0.6.0)
  * Fix favicon rendering.

* [**v0.5.0**
  (2015-05-25)](https://github.com/kdeldycke/plumage/compare/v0.4.0...v0.5.0)
  * Add support for piwik.
  * Upgrade to jQuery 2.1.3.
  * Upgrade to Masonry 3.3.0.
  * Upgrade to fitvids 1.1.0.
  * Upgrade to Magnific Popup 1.0.0.

* [**v0.4.0**
  (2014-02-15)](https://github.com/kdeldycke/plumage/compare/v0.3.0...v0.4.0)
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

* [**v0.3.0**
  (2013-08-16)](https://github.com/kdeldycke/plumage/compare/v0.2.0...v0.3.0)
  * Add auto-zoom of images based on Magnific Popup.
  * Let the content take the available width if there is no right or left
    sidebars.
  * Add an dynamic feed link in footer.
  * Do not wrap code in code blocks.
  * Fix code highlight for older Pelican versions.
  * Escape and strip tags in all title attributes.
  * Style ampersands for those using typogrify.

* [**v0.2.0**
  (2013-07-09)](https://github.com/kdeldycke/plumage/compare/v0.1.0...v0.2.0)
  * Make theme fully generic through the use of variables.
  * Replace custom navigation with Pelican's neighbors plugin.
  * Add screenshot.
  * Update documentation.

* [**v0.1.0**
  (2013-07-07)](https://github.com/kdeldycke/plumage/compare/v0.0.0...v0.1.0)
  * Theme has now a name: Plumage.
  * Move the theme out of my [blog repository
    ](https://github.com/kdeldycke/kevin-deldycke-blog) to its own repository.
  * Theme is now generic enough. Update TODO-list accordingly.

* [**v0.0.0**
  (2012-12-23)](https://github.com/kdeldycke/plumage/commit/70df9b)
  * First commit.
