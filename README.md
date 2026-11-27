# Underworld Revisited — Greek Game Strings (`el`)

Modern Greek (Ελληνικά) fan translation of the original game texts (`STRINGS.PAK`) for **[Underworld Revisited](https://github.com/PQMarine/UnderworldRevisited)** (v0.26.0), covering both **Ultima Underworld: The Stygian Abyss** (1992) and **Ultima Underworld II: Labyrinth of Worlds** (1993).

> **Note:** Underworld Revisited's own UI and Greek grammar rules (`Languages/el.tsv`) are maintained upstream in [PQMarine/UnderworldRevisited](https://github.com/PQMarine/UnderworldRevisited/pull/43) and are not duplicated here. Because the `*.strings.tsv` files contain translated texts derived from the original Origin Systems games, this repository is kept **private**.

## What's Included

```
├── Languages/
│   ├── el.strings.tsv          # Ultima Underworld I strings (~7,091 entries; blocks 1–10, cutscenes, all conversations)
│   ├── UW2/
│   │   └── el.strings.tsv      # Ultima Underworld II strings (9,773 entries; blocks 1–10, cutscenes, all conversations)
│   ├── NotoSans-Regular.ttf    # Greek fallback font (classic pixel fonts lack Greek glyphs)
│   └── NotoSans-OFL.txt        # SIL Open Font License for Noto Sans
├── docs/
│   ├── glossary.md             # Frozen Greek RPG/lore terminology & grammar conventions
│   └── HANDOFF.md              # Translation progress log, block inventory, and technical notes
└── scripts/
    └── patch_*.py              # Python helper scripts used to build and patch the TSV files
```

## Coverage

- **Underworld Revisited UI (`el.tsv`):** Included upstream in [PQMarine/UnderworldRevisited](https://github.com/PQMarine/UnderworldRevisited/blob/main/Languages/el.tsv).
- **Ultima Underworld I (`Languages/el.strings.tsv`):** Complete (~6,655 Greek entries; blocks 1–10, books, plaques, 122 cutscene subtitles, and all 5,090 conversation strings). Debug block 24, proper names, mantras, rune words, and lizard tokens are intentionally kept in English. Validated with `uwdump validate-tsv` (0 errors).
- **Ultima Underworld II (`Languages/UW2/el.strings.tsv`):** Complete (~9,252 Greek entries; blocks 1–10, 74 books, plaques, 45 cutscene subtitles, and all 7,397 conversation strings across blocks 3584–3752). Debug block 24, proper names, mantras, and typed keywords are kept in English. Validated with `uwdump validate-tsv --game uw2` (0 errors).

## Installation

1. Locate your **Underworld Revisited** installation folder (the folder containing `UR.exe`).
   - If you are on a release prior to `el.tsv` being bundled (e.g., v0.26.0), also download [`Languages/el.tsv`](https://github.com/PQMarine/UnderworldRevisited/blob/main/Languages/el.tsv) from the upstream repository into your `Languages/` folder.
2. Copy the `Languages/` directory from this repository into your Underworld Revisited folder so that:
   - `Languages/el.strings.tsv`
   - `Languages/UW2/el.strings.tsv`
   - `Languages/NotoSans-Regular.ttf`
   sit alongside `UR.exe` (and `Languages/el.tsv`).
3. Launch Underworld Revisited and set **Language** to **Ελληνικά**.

> **Font note:** Classic pixel fonts do not contain Greek glyphs. `NotoSans-Regular.ttf` is included as a fallback for Classic mode (with `Segoe UI` / `Tahoma` for Modern mode). Save-game names and map notes remain Latin-1.

### Optional Better-Matching Fonts (SIL OFL 1.1)

If you want Greek text to better match the game's original aesthetic, you can optionally add these free, open-source (**SIL OFL 1.1**) fonts. Classic and Modern modes load fonts differently:

- **Classic mode (DOS pixel look):** [Terminus TTF](https://files.ax86.net/terminus-ttf/)
  - Place the `.ttf` in `Languages/` renamed to `TerminusTTF.ttf` (Classic mode loads `.ttf` files directly from `Languages/`).
- **Modern mode (`F`, matches `Lexend Exa`):** [Syne](https://fonts.google.com/specimen/Syne) or [Jura](https://fonts.google.com/specimen/Jura)
  - **Must be installed system-wide** — Modern mode cannot load `.ttf` files from `Languages/` because Unity only falls back to installed OS fonts.
  - On Windows: right-click the `.ttf` file → **Show more options** (Windows 11) → **Install for all users** (so it installs to `C:\Windows\Fonts`, not the per-user folder).
  - On Linux: install into `/usr/share/fonts` (or `~/.local/share/fonts`).

To enable both with automatic fallback to `NotoSans-Regular.ttf` / `Segoe UI` / `Tahoma` when not installed, set `grammar.rule.font` in `Languages/el.tsv` to:

```tsv
grammar.rule.font	TerminusTTF.ttf, os:Syne, os:Jura, os:Terminus (TTF) for Windows, os:Terminus (TTF), NotoSans-Regular.ttf, os:Segoe UI, os:Tahoma
```

With this configuration, **Classic mode** uses `TerminusTTF.ttf` and pressing **`F`** for **Modern mode** switches to `Syne` (or `Jura`). Missing entries are skipped automatically.

## Disclaimer

Ultima and Ultima Underworld are trademarks of their respective owners. This is a non-commercial fan translation for personal use with your own legally owned copies of the original games.
