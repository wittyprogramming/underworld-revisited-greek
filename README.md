# Underworld Revisited — Greek Game Strings (`el`)

Modern Greek (Ελληνικά) fan translation of the original game texts (`STRINGS.PAK`) for **[Underworld Revisited](https://github.com/PQMarine/UnderworldRevisited)** (v0.26.0), covering both **Ultima Underworld: The Stygian Abyss** (1992) and **Ultima Underworld II: Labyrinth of Worlds** (1993).

> **Note:** Underworld Revisited's own UI and Greek grammar rules (`Languages/el.tsv`) are maintained upstream in [PQMarine/UnderworldRevisited](https://github.com/PQMarine/UnderworldRevisited/pull/43) and are not duplicated here. Because the `*.strings.tsv` files contain translated texts derived from the original Origin Systems games, this repository is kept **private**.

## What's Included

```
├── Languages/
│   ├── el.strings.tsv          # Ultima Underworld I strings (7,091 entries; blocks 1–10, cutscenes, all conversations)
│   ├── UW2/
│   │   └── el.strings.tsv      # Ultima Underworld II strings (9,773 entries; blocks 1–10, cutscenes, all conversations)
│   ├── NotoSans-Regular.ttf    # Greek fallback font (classic pixel fonts lack Greek glyphs)
│   └── NotoSans-OFL.txt        # SIL Open Font License for Noto Sans
├── docs/
│   ├── glossary.md             # Frozen Greek RPG/lore terminology, Tier 1 names/titles & grammar conventions
│   └── HANDOFF.md              # Translation progress log, block inventory, and technical notes
└── scripts/
    └── patch_*.py              # Python helper scripts used to build and patch the TSV files
```

## Coverage

- **Underworld Revisited UI (`el.tsv`):** Included upstream in [PQMarine/UnderworldRevisited](https://github.com/PQMarine/UnderworldRevisited/blob/main/Languages/el.tsv) (merged in PR #43).
- **Ultima Underworld I (`Languages/el.strings.tsv`):** Complete (**6,714** Greek entries / 377 English as-is; blocks 1–10, books, plaques, 122 cutscene subtitles, all 5,090 conversation strings, plus Tier 1 titles, epithets, and descriptive names such as *Χρυσοδίψης*, *Ματομεζές*, *Γλειψοκόκαλη*, *Δρ. Κουκουβάγιας*, and *Σερ Cabirus*). Debug block 24, Tier 2 proper names, mantras, rune words, typed keywords, and lizard tokens are intentionally kept in English. Validated with `uwdump validate-tsv` (**0 errors**).
- **Ultima Underworld II (`Languages/UW2/el.strings.tsv`):** Complete (**9,288** Greek entries / 485 English as-is; blocks 1–10, 74 books, plaques, 45 cutscene subtitles, all 7,397 conversation strings across blocks 3584–3752, plus Tier 1 titles, roles, epithets, and descriptive names/places such as *Ο Φύλακας*, *Λόρδος British*, *Λαίδη Tory*, Talorid roles like *Ιστορικός* / *Μελλοντολόγος* / *Ελεημονητής*, *Κάστρο British*, and *Φρούριο Killorn*). Debug block 24, Tier 2 proper names, mantras, and typed keywords are kept in English. Validated with `uwdump validate-tsv --game uw2` (**0 errors, 0 warnings**).

## Installation

1. Locate your **Underworld Revisited** installation folder (the folder containing `UR.exe`).
   - If you are on a release prior to `el.tsv` being bundled (e.g., v0.26.0), also download [`Languages/el.tsv`](https://github.com/PQMarine/UnderworldRevisited/blob/main/Languages/el.tsv) from the upstream repository into your `Languages/` folder.
2. Copy the `Languages/` directory from this repository into your Underworld Revisited folder so that:
   - `Languages/el.strings.tsv`
   - `Languages/UW2/el.strings.tsv`
   - `Languages/NotoSans-Regular.ttf`
   sit alongside `UR.exe` (and `Languages/el.tsv`).
3. Launch Underworld Revisited and set **Language** to **Ελληνικά**.

> **Save / Latin-1 note:** Save-game names, character names, and map notes remain Latin-1 (as in the original 1992/1993 engine).

## Font Setup (Classic & Modern Modes)

Classic pixel fonts (`FONT*.SYS`) do not contain Greek glyphs. Out of the box, upstream `Languages/el.tsv` configures:

```tsv
grammar.rule.font	NotoSans-Regular.ttf, os:Segoe UI, os:Tahoma
```

which uses the bundled `NotoSans-Regular.ttf` in Classic mode and `Segoe UI` / `Tahoma` in Modern mode.

### Recommended Setup: Tahoma (Classic) + Syne Medium (Modern)

Classic and Modern modes load fonts differently:
- **Classic mode** (1-bit 6px pixel boxes such as the message scroll and stats panel) reads `.ttf` files from `Languages/` first.
- **Modern mode** (`F` key, conversations and menus) ignores `.ttf` files in `Languages/` and falls back only to system-installed OS fonts (`os:`).

For the cleanest look in both modes:

- **Classic mode (6px 1-bit pixel boxes):** **Tahoma** (`tahoma.ttf`)
  - Tahoma was hinted specifically for 1-bit monochrome rendering at tiny sizes and stays crisp in the 6-row message scroll without lines colliding.
  - **Windows:** Copy `C:\Windows\Fonts\tahoma.ttf` into your `Languages/` folder (placing the file there lets Classic mode use `tahoma.ttf` while Modern mode skips `.ttf` files and picks `os:Syne Medium`).
  - **Linux / other systems:** Without `tahoma.ttf`, Classic mode automatically falls back to the bundled `NotoSans-Regular.ttf`.
- **Modern mode (`F`, matches Lexend Exa):** **Syne Medium** (static weight 500, [Google Fonts — Syne](https://fonts.google.com/specimen/Syne), SIL OFL 1.1)
  - **Why Medium (500) instead of Regular (400):** Underworld Revisited's built-in `Lexend Exa` lacks Greek *except* for `μ` (`U+03BC`) and `π` (`U+03C0`). With a Regular (400) fallback, every `μ` and `π` renders noticeably bolder than the surrounding Greek letters. Static **Syne Medium** (`static/Syne-Medium.ttf` from the Google Fonts download) matches `Lexend Exa`'s stroke weight and geometric width seamlessly.
  - **Must be installed system-wide** (Modern mode cannot load `.ttf` files from `Languages/`):
    - **Windows:** Right-click `Syne-Medium.ttf` → **Show more options** (Windows 11) → **Install for all users** (so it installs into `C:\Windows\Fonts`, not the per-user folder).
    - **Linux:** Install into `/usr/share/fonts` (or `~/.local/share/fonts`).

Then set `grammar.rule.font` in `Languages/el.tsv` to:

```tsv
grammar.rule.font	tahoma.ttf, os:Syne Medium, os:Tahoma, NotoSans-Regular.ttf, os:Segoe UI
```

With this configuration, **Classic mode** uses `tahoma.ttf` and **Modern mode** (`F`) uses `Syne Medium`. Any missing entry is skipped automatically (falling back to `os:Tahoma`, `NotoSans-Regular.ttf`, and `os:Segoe UI`).

## Disclaimer

Ultima and Ultima Underworld are trademarks of their respective owners. This is a non-commercial fan translation for personal use with your own legally owned copies of the original games.
