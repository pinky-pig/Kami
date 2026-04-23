# Kami · 民国报纸

**A Republican-era newspaper skin for AI document typesetting.**

## Why

这套主题从 `images/风格 2-*` 提炼而来：不是馆藏文稿，而是**铅印报纸、剪报拼版、特刊号外**。

核心气质是：奶油旧报纸、黑色铅字、竖排题名、密集分栏、细黑框线、灰度照片、邮戳和红印章。它适合把报告、白皮书、推荐信、项目方案包装成一份「报纸特刊」或「旧报刊剪报」。

## V1 Scope

- 正式支持：中文 `One-Pager`、`Long Doc`、`Letter`、`Slides`
- 视觉原则：旧报纸底 `#E8DFC9`、黑墨 `#161411`、细黑框线、竖排标题、反白小题、红印章点睛
- 暂不主推：英文模板、简历、作品集

## Style Summary

从参考图总结出的风格语言：

1. **报头优先**：大号宋体/老宋体标题，横排或竖排都可以，像 `家书特刊`、`燕京时报`
2. **分栏密排**：正文可更密，但不能牺牲可读性；多用窄栏、边栏、剪报框
3. **黑白高反差**：主视觉是黑墨和旧纸，不能再用档案蓝
4. **反白标题条**：黑底白字小栏用于栏目名、口号、报刊题签
5. **竖排题名**：大标题、日期栏、侧边标语可以竖排，正文仍以横排优先
6. **灰度照片**：照片只做新闻证据，不做现代 hero
7. **红印章唯一破色**：红色只用于印章/邮戳/发行标记，不用于普通高亮
8. **剪报拼贴感**：页面由几块报纸片、信封、邮票、边框组成，但不要做成杂乱海报

## Use Naturally

Just tell Claude what you need: "做成民国报纸风", "生成一份报纸特刊", "做一版号外", "把这份白皮书排成旧报纸", "写一封家书特刊", "做一套民国报纸风 slides".

The skill auto-triggers from the request, no slash command needed. Chinese v1 routes to newspaper-style templates and writing rules.

## Reference Images

Reference images live in `assets/reference-images/`:

- `style-2-1.jpg` - overview board
- `style-2-2.png` - letter / special issue layouts
- `style-2-4.png` - clipping grid with masthead and red seal
- `style-2-5.png` - dense front-page and vertical date layout

## Install

Install the whole Kami themes plugin:

```bash
npx plugins add /Users/wangwenbo/Desktop/demo/kami/plugins/kami-themes
```

Or install this theme directly:

```bash
npx skills add /Users/wangwenbo/Desktop/demo/kami/plugins/kami-themes/skills/republican-newspaper
```

## Build

Font roles are declared in `assets/fonts/fonts.json`; scripts read that file instead of carrying font names in code.

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py --check-fonts
python3 scripts/build.py --verify slides
python3 scripts/build.py --check
```

From repo root:

```bash
.venv/bin/python plugins/kami-themes/skills/republican-newspaper/scripts/build.py --check
```

## Notes

- 这不是现代新闻站，也不是彩色杂志，而是民国报纸/特刊式的印刷文档
- v1 允许旧纸纹理和灰度照片，但不做过度脏污、撕裂边缘、贴纸化装饰
- 若用户要更安静、档案感更强的主题，用 `republican-manuscript`
