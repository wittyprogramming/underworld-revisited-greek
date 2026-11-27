# Underworld Revisited — Greek Translation (`el`)

Modern Greek (Ελληνικά) fan translation for **[Underworld Revisited](https://github.com/PQMarine/UnderworldRevisited)** (v0.26.0), covering both **Ultima Underworld: The Stygian Abyss** (1992) and **Ultima Underworld II: Labyrinth of Worlds** (1993).

> **Note:** Because the `*.strings.tsv` files contain translated texts derived from the original Origin Systems games, this repository is kept **private** and should not be committed upstream to the main Underworld Revisited repository (only `Languages/el.tsv` is eligible for upstream contribution).

## What's Included

```
├── Languages/
│   ├── el.tsv                  # Underworld Revisited UI, menus, settings & Greek grammar rules (1,181 entries)
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

- **Underworld Revisited UI (`Languages/el.tsv`):** Complete (menus, settings, help/lizard glosses, Greek grammatical gender/case/article rules).
- **Ultima Underworld I (`Languages/el.strings.tsv`):** Complete (~6,655 Greek entries; blocks 1–10, books, plaques, 122 cutscene subtitles, and all 5,090 conversation strings). Debug block 24, proper names, mantras, rune words, and lizard tokens are intentionally kept in English. Validated with `uwdump validate-tsv` (0 errors).
- **Ultima Underworld II (`Languages/UW2/el.strings.tsv`):** Complete (~9,252 Greek entries; blocks 1–10, 74 books, plaques, 45 cutscene subtitles, and all 7,397 conversation strings across blocks 3584–3752). Debug block 24, proper names, mantras, and typed keywords are kept in English. Validated with `uwdump validate-tsv --game uw2` (0 errors).

## Installation

1. Locate your **Underworld Revisited** installation folder (the folder containing `UR.exe`).
2. Copy the `Languages/` directory from this repository into your Underworld Revisited folder so that:
   - `Languages/el.tsv`
   - `Languages/el.strings.tsv`
   - `Languages/UW2/el.strings.tsv`
   - `Languages/NotoSans-Regular.ttf`
   sit alongside `UR.exe`.
3. Launch Underworld Revisited and set **Language** to **Ελληνικά**.

> **Font note:** Classic pixel fonts do not contain Greek glyphs. `el.tsv` configures `grammar.rule.font` to fall back to `NotoSans-Regular.ttf` (with `Segoe UI` and `Tahoma` as system fallbacks). Save-game names and map notes remain Latin-1.

## Disclaimer

Ultima and Ultima Underworld are trademarks of their respective owners. This is a non-commercial fan translation for personal use with your own legally owned copies of the original games.
