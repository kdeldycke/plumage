# Development guide

Plumage is a theme for [Pelican](https://getpelican.com), distributed as a Python package. It ships Jinja templates, SCSS/CSS, and JavaScript, and compiles its assets through an npm-backed webassets pipeline at site-generation time.

## Repository management

The repository is managed by [repomatic](https://github.com/kdeldycke/repomatic). Workflow files under `.github/workflows/` are generated, and `pyproject.toml` carries several tool sections repomatic owns.

### Managed versus downstream-owned workflow content

Each workflow file has two parts:

- The first job is the managed thin caller, delegating to a reusable upstream workflow via a SHA-pinned `uses:`. Regenerate it, never hand-edit it.
- Every job declared *after* that caller is downstream-owned. `repomatic init` preserves them across a re-sync, so this is where theme-specific jobs live.

`autofix.yaml` and `lint.yaml` are the only two files pairing a managed caller with downstream jobs. They cover Pygments, SCSS/CSS, and Jinja, none of which repomatic handles. `tests.yaml` is downstream-owned end to end, carrying no managed caller at all: see below.

Position alone does not settle ownership, though. `release.yaml` declares `publish-pypi` and `release` after its `build` caller, and both are canonical: the first runs repomatic's own `publish-pypi` composite action, the second is another thin caller. Go by the comment instead. The three files holding downstream jobs say so in as many words, right above the first one; `release.yaml` carries no such marker, so nothing in it is yours to hand-edit.

### Bumping the repomatic pin

Regenerate rather than search-and-replace, so codegen changes (new job permissions, reshaped triggers) come along:

```shell-session
$ uvx --no-progress 'repomatic==X.Y.Z' init \
    workflows/autofix.yaml workflows/autolock.yaml workflows/cancel-runs.yaml \
    workflows/changelog.yaml workflows/debug.yaml workflows/docs.yaml \
    workflows/labels.yaml workflows/lint.yaml workflows/release.yaml \
    workflows/tests.yaml publish-pypi-action
```

Naming the workflow files individually is deliberate: a bare `repomatic init` also materializes labels config and a changelog, and an unqualified `workflows` selector bypasses scope gating.

`init` does not reach into downstream-owned jobs. After it runs, update by hand in `autofix.yaml`, which is the only file left carrying either:

- the `uvx --no-progress 'repomatic==X.Y.Z' pr-sync` version strings, one per PR-opening job, so four of them today. Count them rather than trusting this number: a new `sync-` or `format-` job adds one, which is how the count went from three to four. `repomatic lint-repo` catches a stale one as an *error* and exits non-zero, so a missed occurrence reddens the Lint workflow rather than lurking. `repomatic init` realigns them on its own since 7.9.0, so the hand edit is now a check rather than a chore
- action pins that upstream moved, like `astral-sh/setup-uv`

Only for the bump you are performing, though: `sync-workflow-pins` bumps those same literals on its own schedule, once a release clears the cooldown. The hand edit is what makes them match the `uses:` ref you just moved, in the same commit.

Check the release notes for breaking changes needing manual follow-up, like a renamed autofix job whose old PR branch must be closed.

### Tools called from workflows are version-pinned

Every external tool a workflow invokes carries an exact version literal, in one of the two shapes `sync-workflow-pins` recognizes: `uvx '<pkg>==X.Y.Z'` for PyPI, and `npm install pkg@X.Y.Z` for npm. That job resolves each to the newest release past the shared `minimum-release-age` cooldown (default `"8 days"`, so no explicit `[tool.repomatic]` entry is needed) and opens a pull request. Anything invoked unpinned silently floats to the newest release on every run, outside that cooldown.

This is why djlint is *not* a `[project.optional-dependencies]` extra. As a locked dependency its version moved through `sync-uv-lock`, which works, but it also published a meaningless `plumage[djlint]` extra to PyPI. As a pinned `uvx` call it stays on the same footing as every other CI-only linter. Run it locally the way CI does, with `uvx 'djlint==X.Y.Z' --lint plumage/templates/*.html`.

The stylelint pins are repeated in `lint.yaml` and `autofix.yaml` rather than factored into a composite action. `sync-workflow-pins` rewrites every literal it finds in one pass, so the two copies move together on their own and there is nothing for an extra layer of indirection to protect.

### Linter configuration lives in files, not in the workflow calls

Three linters carry per-project deviations. All of them are declared in configuration the
workflows pick up implicitly, rather than as flags on the `run:` lines, so that `lint.yaml`
and `autofix.yaml` cannot drift apart and a local run behaves like CI:

- **stylelint**: `.stylelintrc.yaml`. It selects the shareable config per file type through
  `overrides`, so the workflows must *not* pass `--config`: that flag replaces the file
  wholesale. Its `ignoreFiles` skips the generated Pygments stylesheets. There is no CLI flag
  for individual rules, and `--config` only accepts a path, never inline JSON, so the file is
  not optional. The empty root `rules: {}` is required: stylelint rejects a configuration
  whose rules all come from `overrides`.

  Because those `overrides` discriminate by file type, each job needs a single call over
  `plumage/static/**/*.{css,scss}`. The separate CSS and SCSS steps this replaced existed only
  to pass a different `--config` to each.

- **djlint**: `[tool.djlint]` in `pyproject.toml`, which repomatic does not manage. `H025` is
  scoped through `[tool.djlint.per-file-ignores]` instead of joining the flat `ignore` list,
  because it also reports real nesting errors: it caught a `<ul>` inside a `<p>` in
  `projects.html` that the blanket ignore had been hiding for as long as it was listed there.

- **zizmor**: inline `# zizmor: ignore[adhoc-packages]` comments, which it accepts on the
  line above the finding.

Each ignored rule is commented with the reason it does not apply. The recurring theme is that
the theme styles and templates markup it does not emit (Bootstrap, Pygments, Stork), so rules
assuming ownership of every class name and every nesting level cannot be satisfied.

`stylelint --fix` cannot repair either rule the Pygments stylesheets trip, so formatting them
was never going to make `lint-css` pass: skipping them is the only route to green.

`djlint --reformat` cannot indent a tag whose opening and closing halves sit in different
`{% if %}` blocks. It dedents everything downstream instead, silently and far past the construct
that confused it. Two templates use that idiom, the conditional `<a>` wrapping the thumbnail in
`projects.html` and the month-boundary `<dl>` in `archives.html`, and both are fenced with
`{# djlint:off #}` / `{# djlint:on #}`. Guard the smallest region holding the unbalanced tag: with
the rest of the file still visible, the formatter indents everything around it correctly.

### Facts a workflow restates, and what reconciles them

Three things are declared in more than one place, and nothing in GitHub reconciles the copies. Two of the three are not specific to this theme, so they live upstream where every managed repository gets them; the third is npm-shaped and stays here.

`repomatic lint-repo` carries these, in `check_python_version_consistency` and `check_runner_images`:

- **The supported Python range**, spread across `requires-python`, the classifiers, and the `tests.yaml` matrix. The upstream check requires the matrix to reach *both ends* of the advertised range rather than cover every version in it: skipping intermediate releases is a legitimate way to cut CI load, advertising a boundary nothing tests is not.
- **The runner image.** Neither `sync-workflow-pins` nor Dependabot bumps a `runs-on:` literal, the first only rewriting `uses:` refs and the second only the `uvx '<pkg>==X.Y.Z'` and `npm install pkg@X.Y.Z` shapes. So a runner is the one dependency in a workflow nothing moves. Upstream flags `-latest` aliases, and images outside the curated axes in `repomatic.matrix_axes`, whose Linux entries are `ubuntu-26.04` and `ubuntu-26.04-arm` since repomatic 7.10.0 retired `ubuntu-slim`.

`tests/test_vendored_assets.py` keeps the third, since repomatic has no model of a job that runs npm and deliberately leaves the pipeline downstream:

- **Node.** Every job running `npm` sets it up explicitly, rather than inheriting whatever the runner image shipped. Held to a major (`node-version: "22"`) rather than an exact version, precisely because `sync-workflow-pins` cannot read that input: an exact pin there would be the one literal in the repository nothing ever bumps.

#### The actionlint runner-label config

`.github/actionlint.yaml` declares `ubuntu-26.04` and `ubuntu-26.04-arm` to actionlint, which validates `runs-on:` against a label list baked into the binary at build time. The pinned 1.7.12 predates both, so without that file the Lint workflow fails on `release.yaml`'s generated `publish-pypi` job, which carries `ubuntu-26.04` with no downstream say in the matter.

Delete the file once a repomatic release carrying its own bundled actionlint config is adopted: merged upstream, unreleased as of 7.11.0. A native config replaces the bundled one rather than layering over it, so leaving it in place would shadow it and silently miss a label added upstream later.

#### Open question: x86 versus ARM

The seven downstream jobs sit on `ubuntu-26.04`, moved there from `ubuntu-24.04` when repomatic 7.10.0 retired `ubuntu-slim` and moved its curated Linux axes to the 26.04 pair. x86 was the low-risk half of that pair, not a measured choice: repomatic's own measurements put ARM two to three times faster on its suite, and the reasons these jobs once needed a fuller image (npm, a project build, djlint's sdist-only dependencies) say nothing about architecture. Worth re-testing on `ubuntu-26.04-arm` rather than left as an accident. `.github/actionlint.yaml` already declares that label, so the move is a `runs-on:` edit and a live CI run.

### Tools the runner provides are avoided, not pinned

`sync-pygments-styles` used to read the style list with `jq`, which is whatever the runner image ships and which nothing pins or bumps. It now calls Pygments' own API through `uv run --frozen`, so the version comes from `uv.lock` like every other Python dependency. The output is unchanged: `get_style_defs()` is what `pygmentize -S` calls underneath, and the CLI only adds the trailing newline the script restores.

Prefer that move generally. A runner-provided tool has no version anywhere in the repository, so reaching for the pinned dependency that already does the job beats finding a way to pin the tool.

### Known lint warning: top-level workflow permissions

`repomatic lint-repo` warns that `autofix.yaml`, `lint.yaml`, and `release.yaml` define custom job steps but carry no top-level `permissions` key. Leave it that way. The check has a second arm that fires in the opposite direction: under a top-level `permissions: {}`, a job calling a reusable workflow without its own `permissions:` block is handed an empty scope set, and GitHub aborts the run at startup.

The managed caller job in each of these files is exactly such a job, and `generate_thin_caller` rebuilds it from scratch with no `permissions:` key. Adding the top-level key would satisfy the lint today and break the workflow on the next re-sync. There is no `[tool.repomatic]` setting to grant scopes to a generated caller job.

The warning is advisory: `lint-repo` exits 0. Least privilege is instead declared per job on the downstream-owned jobs, which survive a re-sync.

### `REPOMATIC_PAT` needs `Administration: Read-only`

Since repomatic 7.9.0 the `lint-repo` job *fails* without that scope rather than skipping the checks that need it, so the Lint workflow stays red until the token is regenerated. The error is explicit: `Token lacks 'Administration: Read-only' permission`. The setup guide issue carries a pre-filled link for the regeneration. Nothing in the repository can fix this: the token is a GitHub account setting.

### Configuration repomatic reads

`[tool.repomatic]` in `pyproject.toml`. Two entries are load-bearing here:

- `gitignore.extra-categories = ["node"]` keeps Node entries when `sync-gitignore` regenerates `.gitignore`, since the webassets pipeline installs `node_modules` into the package directory.
- `workflow.ignore-paths = ["citation.cff"]` strips a canonical trigger path this project does not carry.

`[tool.uv]`, `[tool.typos]`, `[tool.mypy]`, and `[tool.bumpversion]` are synced from repomatic's bundled templates. Local edits to them are re-applied on the next sync, so put deviations behind a `[tool.repomatic]` setting instead.

`[tool.typos]` merges rather than overwrites: local additions to `extend-words` and `extend-identifiers` survive a re-sync, but the merge reorders keys (bundled first, local appended) and discards any comment written inside the section. Document why a word is allowlisted here, not there. Currently allowlisted on top of the bundled defaults:

- `ges`: Pygments' CSS class for the `Generic.EmphStrong` token, present in every generated stylesheet under `plumage/static/css/pygments/`.
- `certifi`: the PyPI package, named in the generated `docs/assets/dependencies.mmd` graph.

`files.extend-exclude` carries `*.min.js` for the same reason, and survives a re-sync the same way: the merge grafts local-only keys onto the bundled template. Minified bundles are mangled identifiers end to end and read as one long typo, `bootstrap.bundle.min.js` alone reporting 23, every one a two-letter identifier the minifier produced. Spelling those fragments out here would trip the checker again, since it reads this file too; the `<!-- typos:off -->` markers are the way out when one has to be quoted. None of it is fixable anyway, since `sync-vendored-assets` overwrites those files from `node_modules` on every refresh. The glob splits the tree exactly where it should: every script vendored out of an npm package is minified, and the theme's own `main.js` deliberately is not, so it stays covered. Same shape as stylelint's `ignoreFiles` skipping the generated Pygments stylesheets.

`[tool.uv]`'s `exclude-newer` must stay in `pyproject.toml`, not only in a personal `~/.config/uv/uv.toml`: CI runners have no user-level uv config, so a locally-declared cooldown silently does not apply to `sync-uv-lock`.

## Naming automated operations

A file-modifying job uses one `verb-noun` across all of its dimensions: job ID, PR branch, and PR body template filename. Pick the verb from the data source:

| Prefix     | Semantics                                       | Example                |
| :--------- | :---------------------------------------------- | :--------------------- |
| `sync-X`   | Regenerate from an external or canonical source | `sync-pygments-styles` |
| `update-X` | Compute from project state                      | `update-dep-graph`     |
| `format-X` | Rewrite to enforce canonical style              | `format-css`           |
| `fix-X`    | Correct content                                 | `fix-typos`            |
| `lint-X`   | Check without modifying                         | `lint-jinja`           |

`sync-pygments-styles` regenerates stylesheets from whatever Pygments release `pyproject.toml` pins, so it syncs from an external source. `format-css` and `format-jinja` reformat files already in the tree. Read-only jobs (`lint-css`, `lint-jinja`) use only a job ID, since they open no pull request.

Since the four PR-opening jobs moved to `pr-sync` (repomatic 7.11.0), that convention is enforced rather than merely observed: the branch defaults to the template file's stem, so a template named for something other than its job silently opens the wrong branch.

### `pr-sync` replaced `create-pull-request`

Each PR-opening job ends in one `repomatic pr-sync --template-file` call, where it used to run a `pr-body` step feeding a `peter-evans/create-pull-request` action. Everything the action took as an input now comes off the template: title and body from its content, labels from its frontmatter, branch from its filename, assignee from the ambient `GITHUB_ACTOR`. It also retires a stale pull request once the drift it reported is gone, which an action step could never do from behind a gate that skipped it.

The one input with no equivalent is `add-paths`. `pr-sync` stages the whole tree, so a job leaving anything else dirty commits it. That is why `format-css` installs stylelint with `--no-package-lock` on top of `--no-save`: the latter only holds npm off `package.json`, and the `package-lock.json` npm would otherwise write at the repository root is not gitignored. `sync-vendored-assets` needs no such flag, since `npm ci` fails rather than rewrite the lock file it installs from. Check this whenever a step is added to one of these jobs.

## YAML in workflows

- Single-line commands use plain inline `run:`. Multi-line commands use the folded scalar (`>`), which joins lines with spaces and needs no backslash continuations. Reserve the literal scalar (`|`) for preserved newlines: multi-statement scripts and heredocs.
- Lines may run to 120 characters, not Python's 88. `yamllint` is configured with `line-length: max: 120`.
- Every job sits on `ubuntu-26.04`, the x86 half of the curated Linux pair. There is no slimmer tier to opt out of any more, so a `runs-on:` needs no justifying comment: repomatic 7.10.0 retired `ubuntu-slim` and made every job run on a test-matrix runner. A job moving off that image does need one.

## Theme architecture

### Asset pipeline

`plumage/package.json` declares the npm side of the pipeline: Bootstrap, Bootstrap Icons, Masonry, PostCSS, `postcss-cli` and autoprefixer. `plumage/webassets.py` drives it through `pynpm`, and `pelican-webassets` wires the result into Pelican's build.

Consequences worth remembering:

- `node_modules` lands *inside* the package directory at build time. Both `source-exclude` and `wheel-exclude` in `[tool.uv.build-backend]` must keep it (and `package-lock.json`) out of the distribution. `uv_build` does not read `.gitignore`, so those exclusions are repeated there on purpose.
- The package uses a flat layout, so `[tool.uv.build-backend] module-root = ""`. The package sits at the repo root, not under `src/`.

#### Assets served to browsers are vendored, not installed

Three files under `static/` are copies of files inside npm packages, committed so the wheel is self-contained: `node_modules` is excluded from the distribution, so a site could not otherwise reach them.

| Vendored copy                        | npm package       |
| :----------------------------------- | :---------------- |
| `static/fonts/bootstrap-icons.woff2` | `bootstrap-icons` |
| `static/js/bootstrap.bundle.min.js`  | `bootstrap`       |
| `static/js/masonry.pkgd.min.js`      | `masonry-layout`  |

`sync-vendored-assets` in `autofix.yaml` refreshes all three from whatever releases the lock file pins, the same shape as `sync-pygments-styles` regenerating the stylesheets.

The reason they are here at all, rather than on a CDN: nothing reads a version out of a URL in a template. Dependabot only sees manifests, and `sync-workflow-pins` only sees workflows, so a `<script src>` pinned to a release stays on it forever. Bootstrap's bundle had drifted five patch releases behind the stylesheets built from the same package before this moved.

Two halves therefore have to move together, and different things move them. Dependabot bumps the version in `package.json`; the sync job replaces the file. `tests/test_vendored_assets.py` guards the seam, and compares bytes only when `node_modules` happens to be installed, since the suite otherwise runs without the npm toolchain. It also fails on `cdnjs.cloudflare.com`, `cdn.jsdelivr.net` or `unpkg.com` reappearing in a template: that list is hand-maintained, so a fourth CDN has to be added to it to be caught.

Bootstrap's *bundle* is the one to copy: it carries Popper, which the dropdowns need. The theme's own `static/js/main.js` sits in the same directory as two of the three copies and is deliberately not minified; the job names each file it copies, so nothing it does can reach `main.js`. That used to be enforced by an `add-paths` glob matching only `*.min.js`, which went with `create-pull-request`.

`main.scss` overrides `$bootstrap-icons-font-dir` to the absolute `/theme/fonts`, because the upstream default is relative to the stylesheet and this one gets bundled into `css/main.min.css`. Only `woff2` is declared: the `woff` beside it is another 180 KB for browsers that no longer need it. The `@import` spells out the `.scss` extension, against a stylelint rule disabled inline right above it, because the package ships a `bootstrap-icons.css` next to it and Sass refuses to pick.

#### Bumping the npm dependencies by hand

Repomatic covers no npm ecosystem, so `.github/dependabot.yaml` is what keeps `package.json` moving, under a `cooldown.default-days: 7` matching `[tool.uv] exclude-newer`. With no `semver-*-days` alongside it, that one value governs major, minor and patch alike.

Updating by hand has to reproduce that cooldown, and npm has its own spelling of `exclude-newer`:

```shell-session
$ npm install --before=$(date -v-7d +%Y-%m-%d)
```

`--before` applies to the whole tree, not just the six direct dependencies, so it is the only invocation that keeps a transitive package from landing inside the cooldown window.

`npm install` alone will not lift a transitive dependency that still satisfies its parent's range, however stale or vulnerable it is: it only touches what `package.json` forced to move. Reach for `npm update --before=…` to sweep those, then `npm audit` to confirm.

A cooldown and a security fix pull in opposite directions, and the cooldown wins here: `--before` will hold back a fix that has not aged yet, so expect `npm audit` to keep reporting one. Leave it. Dependabot's `cooldown` covers version updates only and never gates a security update, so it opens that pull request on its own, ahead of the window.

### Python modules

Five modules under `plumage/`, all small:

- `config.py`: settings validation and defaults. `CODE_STYLE` selects the Pygments stylesheet and is validated against `ALL_CODE_STYLES`.
- `dom_transforms.py`: post-generation HTML rewriting via `pyquery`.
- `favicon.py`: favicon link generation.
- `webassets.py`: npm and webassets setup.
- `__init__.py`: version and paths.

When adding or renaming a user-facing setting, update the settings table in `readme.md` in the same change. That table and the PR body templates under `.github/pr-templates/` both name settings directly, and both have drifted from the code before.

### Python version coverage in CI

The `tests.yaml` matrix covers the full 3.11-3.14 range the classifiers advertise, and no downstream job pins `python-version`.

Both used to stop at 3.12, to keep `uv.lock`'s watchfiles 0.24.0 from falling back to a Rust build. That floor was the binding constraint but the cap was set one version too low: 0.24.0 does publish a cp313 wheel, and 3.14 was the first version it left uncovered. watchfiles 1.2.0 publishes cp310 through cp315, so the whole range installs from wheels. If a future resolution walks watchfiles back, 3.14 is the job that fails first.

Only jobs that install the project were ever affected. The two Jinja jobs used to carry the same pin, and lost it when djlint moved to a `uvx` call that never touches `uv.lock`.

## Python compatibility

The floor is Python 3.11 (`requires-python = ">= 3.11"`). Unavailable syntax:

- multi-line f-string expressions (3.12+): split into concatenated strings

The floor was originally set by Pelican rather than the theme: 4.12.0 is the first release requiring 3.11, so 3.11 could not be reached while 3.10 was still supported. It is now the theme's own choice, since the published `pelican` floor had to drop back to 4.11 (see the comment above that dependency): 4.11 still installs on 3.9, so nothing outside this repository forces 3.11 any more. Keeping it there is deliberate, and Exception groups, `except*` and the `Self` type hint came along with the original move and no longer need a `typing_extensions` fallback.

`mypy` passing locally on a newer interpreter does not mean it passes in CI. Check against the minimum when touching type-sensitive code.

### Content is parsed by the MyST reader, through two renderers

`pelican-myst-reader` is a runtime dependency, for the directive syntax: ```` ```{note} ```` fences and friends. It registers for `md`, `markdown`, `mkd`, `mdown`, `mkdn`, `mdwn`, `Rmd` and `myst`, and registers late enough to take every one of them from Pelican's own `MarkdownReader`, so Python Markdown never sees a file and the `markdown` extra is not worth carrying. Both this plugin and `pelican-webassets` are namespace plugins, so they autoload as long as a site does not set `PLUGINS` explicitly.

The part that surprises: the reader picks a renderer **per document**, and the two disagree on code block markup.

| Renderer | Chosen when                                                                                                                    | Code block markup                      |
| :------- | :----------------------------------------------------------------------------------------------------------------------------- | :------------------------------------- |
| Sphinx   | the document holds `{filename}`, `{static}` or `{attach}`, a bibliography, `dollarmath` or `amsmath`, or `force_sphinx` is set | `<div class="highlight"><pre>`         |
| docutils | everything else                                                                                                                | `<pre class="code ... literal-block">` |

Every stylesheet under `static/css/pygments/` is generated with `-a ".highlight"`, and `code.scss` is scoped the same way, so only the first shape gets any syntax colors. `dom_transforms.py` wraps the second one to match, which is why highlighting works without configuration. Remove that wrap and half a site's code blocks silently lose their colors while still emitting every Pygments token span. `tests/test_markdown.py` covers both renderers for exactly this reason.

The same selector has to keep its hands off plain docutils literal blocks, which `.rst` content produces from `::` and which carry no lexer output. That is what the `code` class in `pre.code.literal-block` discriminates.

### The myst-parser override

`pelican-myst-reader` 1.4.0 caps `myst-parser` below 5.0.0, which holds `docutils` below the 0.22 Pelican 4.12.0 requires, so the two cannot resolve together. `[tool.uv] override-dependencies` forces `myst-parser` 5 to break the deadlock. The evidence that the cap is stale rather than real, and the reason the override carries no upper bound, are both recorded in the comment above the entry.

The override only reaches this repository, though, and that is the part to keep in mind. `override-dependencies` is workspace-scoped: uv applies it while resolving *this* project, and no consumer installing the theme ever sees it. So a `pelican>=4.12` floor published to PyPI is unsatisfiable for everyone, by `pip` and `uv` alike, even though it resolves cleanly here. That is why the declared floor sits at 4.11 while `uv.lock` still pins 4.12.0, and why the configuration users actually resolve (4.11 with `myst-parser` 4 and `docutils` 0.21) is not the one CI exercises. The whole suite was run against that set by hand when the floor moved, and all 197 tests passed, so the relaxed floor is sound rather than merely installable. Nothing holds it there, though: the honest fix is a matrix cell that resolves without the override.

Verify a floor change against a *fresh* resolution from outside the repository, never from a working tree: `uv --directory <elsewhere> pip install <built wheel>` reproduces what a user gets, while the same command run from the repo root silently picks the override up and passes. That trap is easy to fall into and reads as a clean bill of health.

Both halves come back together once the reader ships a release carrying [ashwinvis/myst-reader#49](https://github.com/ashwinvis/myst-reader/pull/49), which uncaps every one of its dependencies, so the dance does not have to be repeated a fourth time. It was merged on 2026-08-11, but no release carries it: PyPI still serves `1.4.0` from 2024-09-19 with the cap intact, and a resolver reads the published metadata, so nothing has moved for anyone installing the theme.

The merge is not what this repository resolves, though. A `[tool.uv.sources]` git pin at the merge commit works mechanically: the deadlock clears, `myst-parser` 5.1.0 and Pelican 4.12.0 resolve to exactly what `override-dependencies` used to force, and the built wheel still advertises a plain `pelican-myst-reader>=1.4` with no direct URL, since uv strips its sources at build time. What sinks `main` is everything else on it. [ashwinvis/myst-reader#36](https://github.com/ashwinvis/myst-reader/pull/36) merged on 2025-10-14 and never shipped either, and it makes MDIT the default renderer: the branch routing `{filename}`, `{static}`, `{attach}` and maths to Sphinx sits commented out directly above the `else` that returns MDIT. Eight tests in `test_markdown.py` go red on it, none of them from this side of the seam. Directives stop becoming admonitions, code blocks arrive with no Pygments token spans for `dom_transforms.py` to wrap, and a `:::` fence that is not `{image}` raises `RuntimeError: super(): __class__ cell not found` out of a module-level function in `_mdit_renderer.py`. Only `MYST_FORCE_SPHINX` restores the old output: `MYST_FORCE_DOCUTILS` on its own raises on any document holding a `{filename}` link, which is what the commented-out routing existed to avoid.

Upstream CI will not catch that, which is worth knowing before reading a green check as coverage: the reader's `nox` session installs through `uv sync`, so it resolves the `myst-parser` 4 its own lock file pins and never exercises 5 at all.

So the pin points at [ashwinvis/myst-reader#50](https://github.com/ashwinvis/myst-reader/pull/50) instead, which restores Docutils as the default, reinstates the commented-out routing, and makes the colon fence handler a `Renderer` method. Against that branch the whole suite passes, including all eight tests `main` reddens. It is pinned by commit on the `kdeldycke` fork rather than by branch name, so nothing moves this repository onto different code without the `rev` changing first, and the branch cannot be deleted out from under CI by anyone else.

A release is still the trigger for undoing any of this, and it has to be read rather than assumed to be `1.4.0` plus the uncap. The renderer table above describes `1.4.0`, which is what PyPI still serves and what every claim in this section rests on, so it is the first thing to re-check against whatever ships. If that pull request is reworked or rejected instead, `override-dependencies = [ "myst-parser>=5" ]` is what comes back, and the eight reds come back with it.

#### The `[tool.uv.sources]` pin blocks the next release

`repomatic lint-deps`, added in 7.10.0, refuses to publish a project whose dependencies do not all resolve from the index its users install from, and a git source is the first thing on its list. Run it and this repository reports `pelican-myst-reader | git | tool.uv.sources | blocks release`.

Nothing is broken until a release is cut. The job is fatal only on a release commit, so ordinary pushes stay green; what it stops is `build-package`, and with it the PyPI upload, the tag, and the GitHub release. It also replaces the release PR checklist's opener with a `[!CAUTION]` block naming the dependency, which is the layer that actually reaches a maintainer in time.

Three ways out, none of them chosen yet:

- `[tool.repomatic] lint-deps.allow = { pelican-myst-reader = "<reason>" }`. The reason renders in the report and the PR banner, so the exemption stays visible. Defensible here specifically because the published wheel advertises a plain `pelican-myst-reader>=1.4` and that resolution was run against the full suite by hand, but it does assert that a source override is safe to ship, which is exactly what the gate exists to doubt.
- Revert to `override-dependencies = [ "myst-parser>=5" ]`, which `lint-deps` downgrades to a warning since it names a published version. Costs the fork's renderer fixes, so the eight `test_markdown.py` reds come back.
- Wait for the reader's release, which drops the pin and the problem together.

The documented `sync-dep-sources` idiom (pair the git source with a `.dev` floor naming the awaited release, let the swap PR open on its own) does not apply: the fork branch still declares `1.4.0`, so there is no awaited version to name, and a `.dev` floor would in any case make the published wheel unsatisfiable.

## Testing

The suite lives in `tests/` and runs with `uv run --group test -- pytest`. It is deliberately high-level: templates are rendered through Jinja directly, so it needs neither a Pelican build nor the npm toolchain, and the whole thing finishes in seconds.

Its dependencies sit in a PEP 735 `[dependency-groups]` table, like repomatic, and no longer in an extra. Groups stay out of the published metadata, so there is no installable `plumage[test]` for a theme consumer to reach for, and the suite is not shipped in the distribution anyway. With djlint gone too, `[project.optional-dependencies]` was empty and was removed. The upstream `lint-types` job already syncs with `--all-extras --all-groups`, so it picks the group up unchanged.

Four pieces in `tests/conftest.py` make that possible:

- `StubAssetsExtension` stands in for the `{% assets %}` tag of `pelican-webassets`, whose real implementation compiles SCSS through libsass and PostCSS.
- `BASE_CONTEXT` is the smallest Pelican context that renders `base.html` end to end. Anything the templates iterate over has to be listed there: Jinja's default undefined renders as an empty string, but raises as soon as it is looped on.
- `render_source` returns the markup unparsed, where `render` hands back a `pyquery` document. Reach for it to assert on tag balance: a parser silently repairs an unclosed tag, so the rendered tree of a template missing one looks exactly like the tree of a template that has it.
- `render_override` renders a template through a generated child that replaces one of its blocks, which is the only thing a named block is worth anything for. What the block exposes is only covered if an override reaches the output *and* the default content it displaces does not, so assert both.

`test_archives.py` and `test_projects.py` cover the two regions fenced off with `{# djlint:off #}`, since no linter reads inside a fence. Both hold a tag whose halves live in different `{% if %}` blocks, so the failure they guard against is a missing half: an unclosed `<a>` re-parents the entire card body into the thumbnail link, and an unclosed `<dl>` swallows the next month's entries.

`favicon.py` and `webassets.py` sit well below the other modules in coverage. Both are driven by Pelican's generator objects and the npm toolchain, and neither repays the mocking a unit test would need. `tests/test_favicon.py` covers what matters there without any of it: that every favicon `base.html` links by absolute path is actually shipped.

### Known repomatic bug: the pytest table name

`repomatic init pytest` (7.4.1) writes the table as `[tool.pytest]`, which pytest ignores outright: the section it reads is `[tool.pytest.ini_options]`. The fix applied by hand in `pyproject.toml` leaves that generated header alone and qualifies each key instead, as `ini_options.testpaths` and `ini_options.addopts`, which TOML resolves to the path pytest looks for. The next `repomatic init pytest` will flatten those keys back, so re-check them after any sync rather than the header, which reads `[tool.pytest]` whether the fix is in place or not.

The regression is silent. Symptom: `pytest` still passes, but prints no coverage summary and no durations table, because none of the generated `addopts` reach it.

The generated `addopts` also assume dependencies the bare `pytest` pin does not bring in. `pytest-cov` and `pytest-xdist[psutil]` are in the `test` dependency group for that reason, and `--cov=.` was narrowed to `--cov=plumage` so coverage measures the theme rather than the suite.

### `tests.yaml` is fully downstream-owned

This workflow is the exception to the managed-caller rule described above. Repomatic ships no reusable tests workflow: its own `.github/workflows/tests.yaml` carries no `workflow_call:` trigger, so it cannot be called. `repomatic init workflows/tests.yaml` maintains only the header (name, triggers, `permissions: {}`, concurrency) and leaves every job alone.

It also will not create the file. Seed a stub carrying a `jobs:` key first, then run the init to have the header generated.

Because no job here calls a reusable workflow, the top-level `permissions: {}` is safe, unlike in `autofix.yaml`, `lint.yaml` and `release.yaml`. The `tests` job declares `contents: read` for itself.
