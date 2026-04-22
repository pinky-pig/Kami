# Design System

## Intent

This theme turns Kami into a **Republican-era Chinese newspaper / special issue** system:

**cream newsprint, black letterpress ink, vertical mastheads, dense columns, clipping frames, grayscale photos, postal marks, and one restrained red seal.**

It should feel like a credible old newspaper special issue, not a retro poster.

Reference images are in `assets/reference-images/style-2-*`.

## Scope

- Official: Chinese `one-pager`, `long-doc`, `letter`, `slides`
- Legacy: English templates, resume, portfolio
- No heavy torn-paper effects, colorful magazine treatment, or modern web UI cards

## Core Rules

1. Use newsprint `#E8DFC9`, not pure white and not an archive-blue frame
2. Use black ink `#161411` plus warm grays
3. The only strong accent is seal red `#B7352A`
4. Serif leads mastheads, headlines, and vertical titles
5. Dense columns are allowed, but line-height stays `1.35+`
6. Borders are solid black/warm gray; no `rgba()`
7. Photos are grayscale, low-contrast, evidence-like
8. Decoration is limited to mastheads, datelines, reverse labels, clipping frames, postal marks, and one red seal

## Palette

```css
--newsprint:   #E8DFC9;
--paper-light: #F8F1DD;
--paper-deep:  #DED4BD;
--panel-fill:  #F5EBD3;
--rule-warm:   #B9AA91;

--ink:         #161411;
--near-black:  #1F1B16;
--dark-warm:   #3E382E;
--charcoal:    #514A3F;
--olive:       #6A6257;
--stone:       #8A8173;

--seal-red:    #B7352A;
```

## Typography

| Role | Size | Weight | Line-height |
|---|---:|---:|---:|
| Masthead | 36-54 pt | 500 | 1.05 |
| Vertical Title | 26-40 pt | 500 | 1.10 |
| Headline | 18-28 pt | 500 | 1.12 |
| Section Banner | 10-13 pt | 500 | 1.25 |
| Body | 9.2-10.2 pt | 400 | 1.42-1.50 |
| Dense Body | 8.4-9.2 pt | 400 | 1.35-1.42 |
| Caption | 7.5-8.5 pt | 400 | 1.35 |

Use `KingHwa_OldSong` for Chinese serif display and headline roles.

## Layout Patterns

| Document | Newspaper reading |
|---|---|
| One-Pager | front page / extra edition |
| Long Doc | multi-page special issue |
| Letter | correspondence clipping / family-letter special |
| Slides | editorial board deck |

Use 2-3 columns, narrow sidebars, datelines, and clipping frames. Do not make every element decorative.

## Components

- **Masthead**: large serif title with a black rule
- **Dateline**: date, issue, place, and identity
- **Reverse label**: black background with light text
- **Vertical title**: `writing-mode: vertical-rl` for titles and side labels
- **Clipping frame**: square paper block with thin black border
- **News photo**: grayscale image with thin border
- **Seal**: one red mark per page or section group

## Delivery Check

- [ ] Looks like a newspaper special issue at first glance
- [ ] No archive blue remains
- [ ] Only one red accent role
- [ ] Dense but readable
- [ ] Solid rules, no `rgba()`
- [ ] Grayscale images
- [ ] Credible document, not retro poster
