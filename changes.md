Changelog
=========

* [**1.0.dev**
  (unreleased)](https://github.com/kdeldycke/plumage/compare/0.9...master)
  * Fix issue with Pelican 4.x.
  * Update to Font Awesome 5.
  * Add new `MANUAL_LINKS` setting.
  * Add proper support of `PAGINATION_PATTERNS` setting.
  * Replace dead `better-idea.org` service by [Google favicons service
    ](https://www.google.com/s2/favicons).
  * Add support for Twitter icon in links.

* [**0.9**
  (2017-03-22)](https://github.com/kdeldycke/plumage/compare/0.8...0.9)
  * Upgrade Bootstrap from v2.3.2 to v3.3.7.
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
    ](https://icons.better-idea.org) web service.
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
