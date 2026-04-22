# Kami

Kami is now organized as a multi-theme skill repository.

## Structure

```text
kami/
  apps/
    web/                         # Theme showcase page
  plugins/
    kami-themes/
      plugin.json
      skills/
        republican-manuscript/   # 民国文稿主题
        republican-newspaper/    # 民国报纸主题
```

## Current Plugin

### `kami-themes`

- `republican-manuscript`
  - Chinese-first document theme for one-pagers, long docs, letters, and slides
  - Deep archive-blue frame, old-paper sheet, and blue title plaques
  - Original skill docs, templates, references, demos, fonts, and build script live inside the skill directory
- `republican-newspaper`
  - Chinese-first document theme for newspaper specials, extra editions, reports, letters, and slides
  - Cream newsprint, black letterpress ink, vertical mastheads, dense columns, clipping frames, grayscale photos, and a red seal accent
  - Includes copied Style 2 reference images under `assets/reference-images/`

## Add A New Theme

Create a new sibling skill under `plugins/kami-themes/skills/`:

```text
plugins/kami-themes/skills/<theme-name>/
  SKILL.md
  README.md
  CHEATSHEET.md
  assets/
  references/
  scripts/
```

Then add the theme to `apps/web` so the showcase can display it alongside the existing one.

## Local Preview

Open `apps/web/index.html` in a browser.

## Build Current Theme

```bash
python3 plugins/kami-themes/skills/republican-manuscript/scripts/build.py --verify long-doc
python3 plugins/kami-themes/skills/republican-manuscript/scripts/build.py --check
python3 plugins/kami-themes/skills/republican-newspaper/scripts/build.py --check
```

## Install

Install the plugin collection locally:

```bash
npx plugins add /Users/wangwenbo/Desktop/demo/kami/plugins/kami-themes
```

Or install the current theme skill directly:

```bash
npx skills add /Users/wangwenbo/Desktop/demo/kami/plugins/kami-themes/skills/republican-manuscript
```

Or install the newspaper theme directly:

```bash
npx skills add /Users/wangwenbo/Desktop/demo/kami/plugins/kami-themes/skills/republican-newspaper
```
