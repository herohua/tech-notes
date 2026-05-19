# tech-notes

Personal tech notes. Raw markdown lives in `notes/`; images in `images/`.

On push to `main`, a GitHub Action transforms each note with `publish: true` into a Jekyll post and pushes it to [herohua/herohua.github.io](https://github.com/herohua/herohua.github.io), which renders at <https://herohua.github.io>.

## Writing a note

Create `notes/<slug>.md` (slug can be anything, e.g. `kafka-rebalancing.md`) with this front matter:

```yaml
---
title: "Kafka rebalancing in depth"
date: 2026-05-19
tags: [kafka, distributed-systems]
publish: true
---

Your markdown here.

![diagram](../images/kafka-rebalance.png)
```

- `title` — required. Used as the post title.
- `date` — required. `YYYY-MM-DD`. Becomes the post date and the filename prefix.
- `tags` — optional.
- `publish` — set to `true` to publish. Anything else (or missing) stays as draft.

Image links should be relative (`../images/foo.png`) so they render correctly when previewed locally on GitHub. The publish script rewrites them to `/assets/notes/foo.png` for the live site.

## Publishing

Just commit and push to `main`. The Action handles the rest. See `.github/workflows/publish.yml`.
