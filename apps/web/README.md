# apps/web

`apps/web` now serves a flattened local copy of [transitions.dev](https://transitions.dev/) as the active web root for this repo.

## Current structure

- `index.html` — main transitions.dev homepage.
- `demo2.html`, `prototypes.html` — additional upstream showcase pages.
- `assets/` — icons, favicons, and OG image used by the site.
- `legacy-kami-showcase/` — archived previous static Kami showcase pages moved out of the active root.
- `plugins` — symlink to the repo-level `plugins/` directory so the archived Kami pages can still resolve their original assets when served from `apps/web/`.

## Legacy pages

The old Kami landing page files were preserved instead of deleted:

- `legacy-kami-showcase/index.html`
- `legacy-kami-showcase/index-en.html`
- `legacy-kami-showcase/styles.css`

Their internal asset paths were updated so they still work from the archive location.

## Run locally

```bash
python3 -m http.server 8765
```

Then open [http://127.0.0.1:8765/](http://127.0.0.1:8765/).
