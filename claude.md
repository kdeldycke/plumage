# Development guide

Plumage is a theme for [Pelican](https://getpelican.com), distributed as a Python package. It ships Jinja templates, SCSS/CSS, and JavaScript, and compiles its assets through an npm-backed webassets pipeline at site-generation time.

## Repository management

The repository is managed by [repomatic](https://github.com/kdeldycke/repomatic). Workflow files under `.github/workflows/` are generated, and `pyproject.toml` carries several tool sections repomatic owns.

### Managed versus downstream-owned workflow content

Each workflow file has two parts:

- The first job is the managed thin caller, delegating to a reusable upstream workflow via a SHA-pinned `uses:`. Regenerate it, never hand-edit it.
- Every job declared *after* that caller is downstream-owned. `repomatic init` preserves them across a re-sync, so this is where theme-specific jobs live.

`autofix.yaml` and `lint.yaml` are the only two files carrying downstream jobs. They cover Pygments, SCSS/CSS, and Jinja, none of which repomatic handles.

### Bumping the repomatic pin

Regenerate rather than search-and-replace, so codegen changes (new job permissions, reshaped triggers) come along:

```shell-session
$ uvx --no-progress 'repomatic==X.Y.Z' init \
    workflows/autofix.yaml workflows/autolock.yaml workflows/cancel-runs.yaml \
    workflows/changelog.yaml workflows/debug.yaml workflows/docs.yaml \
    workflows/labels.yaml workflows/lint.yaml workflows/release.yaml \
    publish-pypi-action
```

Naming the workflow files individually is deliberate: a bare `repomatic init` also materializes labels config and a changelog, and an unqualified `workflows` selector bypasses scope gating.

`init` does not reach into downstream-owned jobs. After it runs, update by hand in `autofix.yaml` and `lint.yaml`:

- the `uvx --no-progress 'repomatic==X.Y.Z' pr-body` version strings (three occurrences)
- action pins that upstream moved, like `astral-sh/setup-uv`

Check the release notes for breaking changes needing manual follow-up, like a renamed autofix job whose old PR branch must be closed.

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
- **djlint**: `[tool.djlint]` in `pyproject.toml`, which repomatic does not manage.
- **zizmor**: inline `# zizmor: ignore[adhoc-packages]` comments, which it accepts on the
  line above the finding.

Each ignored rule is commented with the reason it does not apply. The recurring theme is that
the theme styles and templates markup it does not emit (Bootstrap, Pygments, Stork), so rules
assuming ownership of every class name and every nesting level cannot be satisfied.

`stylelint --fix` cannot repair either rule the Pygments stylesheets trip, so formatting them
was never going to make `lint-css` pass: skipping them is the only route to green.

### Known lint warning: top-level workflow permissions

`repomatic lint-repo` warns that `autofix.yaml`, `lint.yaml`, and `release.yaml` define custom job steps but carry no top-level `permissions` key. Leave it that way. The check has a second arm that fires in the opposite direction: under a top-level `permissions: {}`, a job calling a reusable workflow without its own `permissions:` block is handed an empty scope set, and GitHub aborts the run at startup.

The managed caller job in each of these files is exactly such a job, and `generate_thin_caller` rebuilds it from scratch with no `permissions:` key. Adding the top-level key would satisfy the lint today and break the workflow on the next re-sync. There is no `[tool.repomatic]` setting to grant scopes to a generated caller job.

The warning is advisory: `lint-repo` exits 0. Least privilege is instead declared per job on the downstream-owned jobs, which survive a re-sync.

### Configuration repomatic reads

`[tool.repomatic]` in `pyproject.toml`. Two entries are load-bearing here:

- `gitignore.extra-categories = ["node"]` keeps Node entries when `sync-gitignore` regenerates `.gitignore`, since the webassets pipeline installs `node_modules` into the package directory.
- `workflow.ignore-paths = ["citation.cff"]` strips a canonical trigger path this project does not carry.

`[tool.uv]`, `[tool.typos]`, `[tool.mypy]`, and `[tool.bumpversion]` are synced from repomatic's bundled templates. Local edits to them are re-applied on the next sync, so put deviations behind a `[tool.repomatic]` setting instead.

`[tool.typos]` merges rather than overwrites: local additions to `extend-words` and `extend-identifiers` survive a re-sync, but the merge reorders keys (bundled first, local appended) and discards any comment written inside the section. Document why a word is allowlisted here, not there. Currently allowlisted on top of the bundled defaults:

- `ges`: Pygments' CSS class for the `Generic.EmphStrong` token, present in every generated stylesheet under `plumage/static/css/pygments/`.
- `certifi`: the PyPI package, named in the generated `docs/assets/dependencies.mmd` graph.

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

## YAML in workflows

- Single-line commands use plain inline `run:`. Multi-line commands use the folded scalar (`>`), which joins lines with spaces and needs no backslash continuations. Reserve the literal scalar (`|`) for preserved newlines: multi-statement scripts and heredocs.
- Lines may run to 120 characters, not Python's 88. `yamllint` is configured with `line-length: max: 120`.
- Jobs default to `ubuntu-slim`. Move a job to a fuller image only when a failure proves a tool is missing, and record the reason in a comment above `runs-on:`. All five downstream jobs sit on `ubuntu-24.04` for that reason: three build the project, two install linters from npm.

## Theme architecture

### Asset pipeline

`plumage/package.json` declares the npm side of the pipeline: Bootstrap, PostCSS, and autoprefixer. `plumage/webassets.py` drives it through `pynpm`, and `pelican-webassets` wires the result into Pelican's build.

Consequences worth remembering:

- `node_modules` lands *inside* the package directory at build time. Both `source-exclude` and `wheel-exclude` in `[tool.uv.build-backend]` must keep it (and `package-lock.json`) out of the distribution. `uv_build` does not read `.gitignore`, so those exclusions are repeated there on purpose.
- The package uses a flat layout, so `[tool.uv.build-backend] module-root = ""`. The package sits at the repo root, not under `src/`.

### Python modules

Five modules under `plumage/`, all small:

- `config.py`: settings validation and defaults. `CODE_STYLE` selects the Pygments stylesheet and is validated against `ALL_CODE_STYLES`.
- `dom_transforms.py`: post-generation HTML rewriting via `pyquery`.
- `favicon.py`: favicon link generation.
- `webassets.py`: npm and webassets setup.
- `__init__.py`: version and paths.

When adding or renaming a user-facing setting, update the settings table in `readme.md` in the same change. That table and the PR body templates under `.github/` both name settings directly, and both have drifted from the code before.

### Python version pins in CI

Three downstream jobs pin `python-version: "3.12"`, and the `tests.yaml` matrix stops at the same version instead of covering the full 3.10-3.14 range the classifiers advertise. This is a workaround, not a policy: `uv.lock` holds watchfiles 0.24.0, a transitive Pelican dependency shipping no wheel past 3.12, which otherwise falls back to a Rust build. Drop the pins and extend the matrix once `sync-uv-lock` has moved the lock past it.

## Python compatibility

The floor is Python 3.10 (`requires-python = ">= 3.10"`). Unavailable syntax:

- multi-line f-string expressions (3.12+): split into concatenated strings
- exception groups and `except*` (3.11+)
- the `Self` type hint (3.11+): use `typing_extensions.Self`

`mypy` passing locally on a newer interpreter does not mean it passes in CI. Check against the minimum when touching type-sensitive code.

## Testing

The suite lives in `tests/` and runs with `uv run --extra test -- pytest`. It is deliberately high-level: templates are rendered through Jinja directly, so it needs neither a Pelican build nor the npm toolchain, and the whole thing finishes in seconds.

Two pieces in `tests/conftest.py` make that possible:

- `StubAssetsExtension` stands in for the `{% assets %}` tag of `pelican-webassets`, whose real implementation compiles SCSS through libsass and PostCSS.
- `BASE_CONTEXT` is the smallest Pelican context that renders `base.html` end to end. Anything the templates iterate over has to be listed there: Jinja's default undefined renders as an empty string, but raises as soon as it is looped on.

`favicon.py` and `webassets.py` sit well below the other modules in coverage. Both are driven by Pelican's generator objects and the npm toolchain, and neither repays the mocking a unit test would need. `tests/test_favicon.py` covers what matters there without any of it: that every favicon `base.html` links by absolute path is actually shipped.

### Known repomatic bug: the pytest table name

`repomatic init pytest` (7.4.1) writes the table as `[tool.pytest]`, which pytest ignores outright. The section it reads is `[tool.pytest.ini_options]`. The rename is applied by hand in `pyproject.toml`, and the next `repomatic init pytest` will undo it, so re-check the table name after any sync.

The regression is silent. Symptom: `pytest` still passes, but prints no coverage summary and no durations table, because none of the generated `addopts` reach it.

The generated `addopts` also assume dependencies the bare `pytest` pin does not bring in. `pytest-cov` and `pytest-xdist[psutil]` are in the `test` extra for that reason, and `--cov=.` was narrowed to `--cov=plumage` so coverage measures the theme rather than the suite.

### `tests.yaml` is fully downstream-owned

This workflow is the exception to the managed-caller rule described above. Repomatic ships no reusable tests workflow: its own `.github/workflows/tests.yaml` carries no `workflow_call:` trigger, so it cannot be called. `repomatic init workflows/tests.yaml` maintains only the header (name, triggers, `permissions: {}`, concurrency) and leaves every job alone.

It also will not create the file. Seed a stub carrying a `jobs:` key first, then run the init to have the header generated.

Because no job here calls a reusable workflow, the top-level `permissions: {}` is safe, unlike in `autofix.yaml`, `lint.yaml` and `release.yaml`. The `tests` job declares `contents: read` for itself.
