---
title: Sync vendored assets
footer: false
labels: [🔗 dependencies]
---

> [!TIP]
> The three files browsers are served straight out of npm packages, copied from the releases pinned in `plumage/package.json`: the Bootstrap Icons font, Bootstrap's JavaScript bundle, and Masonry. `node_modules` is excluded from the distribution, so these have to be committed, and they have to move whenever Dependabot bumps a pin.
