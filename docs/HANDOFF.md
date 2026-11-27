# Handoff: Greek translation of Underworld Revisited 0.26.0

UW1 Origin strings are complete except debug block 24 (leave English unless tiny). Next is UW2. Do not rewrite `el.tsv` or re-gender UW1 block 4 unless a look sentence is wrong.

## What this is

Natural Modern Greek for UR 0.26.0. Ground in existing CRPG/D&D/fan terms (D&D 3.5 official Greek, GTC for BG3/Skyrim). There is no official Greek Ultima Underworld. Keep person names, mantras, rune letters, and lizard tokens in English unless `uwdump typed-words` later forces a consistent Greek mantra.

Voice: UI and system messages use **εσύ**. NPC speech follows the speaker. **κάτω κόσμος** for underworld, never υπόκοσμος. Title: **Ultima Underworld** + subtitle **Η Στυγιανή Άβυσσος**.

## Files (already beside `UR.exe`)

| Path | Role |
|---|---|
| `C:\Games\UnderworldRevisited\UR.exe` | Game |
| `C:\Games\UnderworldRevisited\Languages\el.tsv` | UR UI + grammar. **Done** (1181 ids). May PR to GitHub. |
| `C:\Games\UnderworldRevisited\Languages\el.strings.tsv` | UW1 Origin strings (~7091). **Done** except debug 24. Never commit to the UR repo. |
| `C:\Games\UnderworldRevisited\Languages\UW2\el.strings.tsv` | UW2 Origin strings (9773). **Blocks 1–10 done** (except 24). |
| `C:\Games\UnderworldRevisited\Languages\glossary.md` | Frozen terms. Extend it; do not invent a second form. |
| `C:\Games\UnderworldRevisited\Languages\NotoSans-Regular.ttf` | Greek fallback font |
| Kit | `C:\Games\UnderworldRevisited\UnderworldRevisited-0.26.0-TranslationKit-win64\` (`TRANSLATING.md`, `uwdump.exe`, `en.tsv`, `de.tsv`) |
| UW1 DATA | `C:\Users\kzagoris\AppData\LocalLow\Underworld Revisited\Underworld Revisited\GameData\UW1\DATA` |
| UW2 DATA | `...\GameData\UW2` |
| GitHub | https://github.com/PQMarine/UnderworldRevisited |

In-game: Language row → **Ελληνικά**. Classic pixel fonts cannot draw Greek; `grammar.rule.font` already points at NotoSans + Segoe UI + Tahoma. Save names / map notes stay Latin-1.

## Done

- Full `el.tsv` UI (menus, settings, pictures, lizard *glosses*, grammar).
- UW1 **block 4** object/creature names in name format (gender + article + cases).
- UW1 **block 5** 1–100 condition/attitude adjectives as `{0,select,...}`.
- UW1 **block 7** lowercase kinds that replace the type (`golem`, `prisoner`, `guard`, void names 257–265). Proper names left English, no prefix. Indices 1–17 (cannot talk / barter deal fragments) Done.
- UW1 **block 1** system messages, detect kinds 371–399, ordinals 412–512.
- UW1 **block 6** spell / enchantment labels (213). No name-format prefix.
- UW1 **block 2** character creation (49 prompts/classes/skills; mantras 52–77 stay English).
- UW1 **block 10** wall / scenery names in name format (264).
- UW1 **block 5** key flavor 102–128 (15 paragraphs). Quoted `Key to Courage` → «Κλειδί του Θάρρους»; letters `E`/`W` kept.
- Typed-word policy confirmed: mantras and compare/contains keywords stay English.
- `uwdump validate-tsv`: 0 errors (warnings: Greek in classic pixel boxes — expected).

Look sentences already work, e.g. `Βλέπεις έναν ήρεμο σαπιοσκώληκα ονόματι Corby.` / `Επιδιόρθωσες εν μέρει το τσεκούρι.`

## Counts (UW1 `el.strings.tsv`)

About **6714** lines contain Greek; **`validate-tsv` 0 errors**, 377 English as-is (2026-11-27 after Tier 1 names/titles/roles pass). Conversations: **all 5090** (3585–3898; keywords/lizard tokens/`Other...` etc. left English). Cutscenes: **122**.

| Block | What | Status |
|---|---|---|
| 1 | Messages / pieces | Done (only `.\n` and `...` left English on purpose) |
| 2 | Character creation prompts | Done (mantras English) |
| 3 | Books, scrolls, mantras in text | **Done** (70; mantras/runes/`Folanae Fanlo` English) |
| 4 | Object names | Done (`Lotus Turbo Esprit` and debug `special tmap obj` kept) |
| 5 | Adjectives + key flavor 102+ | **Done** (15 key look paragraphs; empty slots stay empty) |
| 6 | Spell names | Done |
| 7 | Conv UI + NPC names | **Done** (kinds + deal/barter 1–17; proper names English) |
| 8 | Gravestones, plaques, signs | **Done** (116; names/mantras English; damaged `Thost the Fi t` kept) |
| 9 | Misc events / visions | **Done** (14) |
| 10 | Wall / scenery names | Done (name format; unique banners `d`) |
| 24 | Debug dungeon report | Leave English unless tiny |
| 3072–3105 | Cutscene subtitles | **Done** (122; names English; Auto subtitles on) |
| 3585–3898 | Conversations | **Done** (5090; keywords/lizard tokens/`Sir`/`Madam`/`Other...` English) |

UW2 pack: 9773 strings; **~9288 Greek** (blocks 1–10 except 24; 74 books; **45 cutscenes**; **all conversations 3584–3752**; Tier 1 names/titles/roles done); rest English. `validate-tsv --game uw2`: 0 errors (2026-11-27).

## Next step (this handoff)

**UW2 conversations complete** (chunks 1–16, all 7397 strings in blocks 3584–3752). Names/mantras/keywords English. Keep `@SS1` `\m`. Same voice: εσύ, **κάτω κόσμος**.

UW2 DATA = `C:\Users\kzagoris\AppData\LocalLow\Underworld Revisited\Underworld Revisited\GameData\UW2\DATA` (folder that contains `LEV.ARK`). Always pass `--game uw2` to uwdump.

### UW2 chunk plan

Same order as UW1, one block at a time, `validate-tsv --game uw2` after each.

| Order | Block | n | Plan |
|---|---|---:|---|
| 1 | **4** object names | 448 | **Done.** 316 copied from UW1 by checksum; 132 UW2-only. Lotus Turbo Esprit / special tmap / Talorid / trilkhun / delgnigzator English or unprefixed names as noted. |
| 2 | 7 kinds / NPC names | 124 | **Done.** Deal 1–17 copied from UW1; lowercase kinds prefixed; proper names English; void 257–264 copied. |
| 3 | 10 wall / scenery | 469 | **Done.** Name format; unique banners `d`; UW1 copy by English. |
| 4 | 5 adjectives | 115 | **Done.** `{0,select,...}` like UW1; UW2-only 85–90 + 22 key looks. |
| 5 | 6 spells | 262 | **Done.** 192 copied from UW1 by checksum; 70 UW2-only labels; no name-format prefix; `Altara` English. |
| 6 | 1 system messages | 489 | **Done.** Pieces; `\n` kept; repair prefixes like UW1 (no `{1}` in frames). |
| 7 | 2 character creation | 76 | **Done.** Skills from glossary; mantras 52–77 English; Skill Pt → Βαθμ. δεξ. |
| 8 | 3 books / 8 plaques / 9 events | 74 / 118 / 29 | **Blocks 3+8+9 Done.** Names/mantras/runes English; spell names from block 6. |
| 9 | 24 debug | 127 | Skip / leave English. |
| 10 | Cutscenes 3072–3115 | 45 | **Done.** Existing indices only (no 3073/3075/3080–95/3103/3105–11). Names English (`Guardian`, `Lord British`, `Britain`, `Cove`, `Draxinusom`). Auto subtitles on. |
| 11 | Conversations 3584–3752 | 7397 | **Done.** Chunks 1–16 complete. Keep `@SS1` `\m`; keywords English. |

**First UW2 session: block 4 only** (448). Diff against UW1 block 4, reuse identical English rows, then invent Greek for new items. Do not move `{1}` into `el.tsv` repair/shrine frames until UW2 pieces also name `{1}`.

### UW2 conversation inventory (`Languages/UW2/el.strings.tsv`, 107 blocks, **7397** strings)

Gaps unused (no 3604–3607, 3620–3623, 3645–3646, 3649–3655, 3660–3663, 3671, 3673–3679, 3690–3711, 3729, 3732, 3734–3735, 3745–3751). First chunk **3584–3589** (~548).

| Chunk | Blocks | n | Status |
|---|---|---:|---|
| 1 | 3584–3589 | 548 | **Done** |
| 2 | 3590–3599 | 472 | **Done** |
| 3 | 3600–3614 | 470 | **Done** |
| 4 | 3615–3626 | 467 | **Done** |
| 5 | 3627–3629 | 480 | **Done** |
| 6 | 3630–3637 | 490 | **Done** |
| 7 | 3638–3659 | 462 | **Done** |
| 8 | 3664–3680 | 453 | **Done** |
| 9 | 3681–3685 | 437 | **Done** |
| 10 | 3686–3689 | 486 | **Done** |
| 11 | 3712–3714 | 421 | **Done** |
| 12 | 3715–3718 | 445 | **Done** |
| 13 | 3719–3722 | 409 | **Done** |
| 14 | 3723–3726 | 410 | **Done** |
| 15 | 3727–3739 | 473 | **Done** |
| 16 | 3740–3752 | 474 | **Done** |

| Block | n | Block | n | Block | n | Block | n |
|---|---:|---|---:|---|---:|---|---:|
| 3584 | 112 | 3614 | 54 | 3656 | 117 | 3715 | 119 |
| 3585 | 112 | 3615 | 40 | 3657 | 92 | 3716 | 124 |
| 3586 | 2 | 3616 | 62 | 3658 | 17 | 3717 | 94 |
| 3587 | 109 | 3617 | 42 | 3659 | 23 | 3718 | 108 |
| 3588 | 100 | 3618 | 61 | 3664 | 75 | 3719 | 87 |
| 3589 | 113 | 3619 | 1 | 3665 | 35 | 3720 | 117 |
| 3590 | 94 | 3624 | 43 | 3666 | 9 | 3721 | 134 |
| 3591 | 2 | 3625 | 150 | 3667 | 2 | 3722 | 71 |
| 3592 | 108 | 3626 | 68 | 3668 | 34 | 3723 | 110 |
| 3593 | 60 | 3627 | 89 | 3669 | 63 | 3724 | 101 |
| 3594 | 45 | 3628 | 113 | 3670 | 28 | 3725 | 84 |
| 3595 | 70 | 3629 | 278 | 3672 | 97 | 3726 | 115 |
| 3596 | 8 | 3630 | 37 | 3680 | 110 | 3727 | 73 |
| 3597 | 9 | 3631 | 98 | 3681 | 77 | 3728 | 75 |
| 3598 | 15 | 3632 | 47 | 3682 | 67 | 3730 | 42 |
| 3599 | 61 | 3633 | 51 | 3683 | 70 | 3731 | 56 |
| 3600 | 32 | 3634 | 56 | 3684 | 61 | 3733 | 21 |
| 3601 | 93 | 3635 | 96 | 3685 | 162 | 3736 | 61 |
| 3602 | 24 | 3636 | 58 | 3686 | 163 | 3737 | 51 |
| 3603 | 61 | 3637 | 47 | 3687 | 78 | 3738 | 29 |
| 3608 | 36 | 3638 | 51 | 3688 | 98 | 3739 | 65 |
| 3609 | 74 | 3639 | 27 | 3689 | 147 | 3740 | 91 |
| 3610 | 32 | 3640 | 38 | 3712 | 151 | 3741 | 95 |
| 3611 | 19 | 3641 | 44 | 3713 | 19 | 3742 | 38 |
| 3612 | 12 | 3642 | 2 | 3714 | 251 | 3743 | 113 |
| 3613 | 33 | 3643 | 4 | | | 3744 | 43 |
| | | 3644 | 13 | | | 3752 | 94 |
| | | 3647 | 1 | | | | |
| | | 3648 | 33 | | | | |

### UW1 conversation block inventory (`el.strings.tsv`, 97 blocks, 5090 strings)

| Block | n | Block | n | Block | n | Block | n |
|---|---:|---|---:|---|---:|---|---:|
| 3585 | 46 | 3607 | 69 | 3725 | 59 | 3798 | 46 |
| 3586 | 163 | 3608 | 97 | 3726 | 11 | 3799 | 45 |
| 3587 | 97 | 3609 | 52 | 3727 | 75 | 3800 | 45 |
| 3588 | 136 | 3610 | 48 | 3728 | 54 | 3801 | 38 |
| 3589 | 64 | 3611 | 51 | 3730 | 84 | 3802 | 52 |
| 3590 | 79 | 3612 | 69 | 3731 | 84 | 3803 | 43 |
| 3591 | 60 | 3648 | 26 | 3732 | 84 | 3804 | 42 |
| 3592 | 15 | 3649 | 36 | 3733 | 84 | 3805 | 81 |
| 3593 | 54 | 3650 | 11 | 3745 | 90 | 3806 | 40 |
| 3594 | 53 | 3651 | 49 | 3746 | 53 | 3815 | 12 |
| 3595 | 30 | 3672 | 30 | 3768 | 29 | 3816 | 51 |
| 3596 | 139 | 3673 | 43 | 3769 | 38 | 3846 | 32 |
| 3597 | 99 | 3674 | 41 | 3770 | 40 | 3847 | 32 |
| 3598 | 74 | 3696 | 49 | 3771 | 74 | 3852 | 34 |
| 3599 | 98 | 3697 | 67 | 3772 | 40 | 3856 | 34 |
| 3600 | 67 | 3698 | 30 | 3773 | 48 | 3860 | 46 |
| 3601 | 35 | 3699 | 18 | 3774 | 41 | 3861 | 66 |
| 3602 | 40 | 3720 | 84 | 3775 | 61 | 3862 | 46 |
| 3603 | 64 | 3721 | 54 | 3776 | 17 | 3864 | 66 |
| 3604 | 85 | 3722 | 33 | 3777 | 26 | 3865 | 49 |
| 3605 | 21 | 3723 | 81 | 3778 | 57 | 3866 | 41 |
| 3606 | 21 | 3724 | 37 | 3792 | 44 | 3872 | 35 |
| | | | | 3793 | 42 | 3875 | 7 |
| | | | | 3794 | 41 | 3879 | 24 |
| | | | | 3795 | 64 | 3881 | 7 |
| | | | | 3796 | 79 | 3898 | 19 |
| | | | | 3797 | 23 | | |

Gaps are unused (no 3613–3647, no 3729, etc.). Do **not** start 3585+ in the same session as leftover block 7 work.

`UW_DATA` = `C:\Users\kzagoris\AppData\LocalLow\Underworld Revisited\Underworld Revisited\GameData\UW1\DATA` (the folder that *contains* `LEV.ARK`). Capture uwdump as UTF-8 via Python `subprocess`.

### 1. Plaques / graves — block 8 — **Done**

Keep Garamon, Korianous, Cabirus, mantras.

### 2. Events — block 9 — **Done** (14)

### 3. Books / scrolls — block 3 — **Done** (70)

Mantras and typed answers kept English (RA, LU, UN, HUNN, SAHF, FAL, ONO, AAM, MUL, ROMM, LAHN, IMU, SOL, Folanae Fanlo, rune strings). Skill names match glossary.

### 4. Then, still UW1

- Conversations (3585–3898): **Done**. Keep `@SS1`, `@GI3C2`, `\m`, `\p`, `\0`. Names stay English. Compare/contains keywords in those slots stay the English token.
- Cutscenes **3072–3105**: **Done** (122). Auto subtitles on for those scenes.

### 5. UW2 last

Copy the same name-format genders from UW1 where the object is the same. `Languages/UW2/el.strings.tsv`. Frames in `el.tsv` serve both games: **do not** move `{1}` into repair/shrine *frames* until UW2 pieces also name `{1}`. UW1 pieces currently stay prefixes (`Επιδιόρθωσες εν μέρει ` + name), which is grammatical.

## Name format (already in force)

```
<gender>[article]:<singular>[|acc=...][|gen=...][&plural][&acc=...][&gen=...]
```

- Gender: `m` `f` `n` (`p` allowed in header; avoid `p` for paired armour — use `n:ζευγάρι …`).
- Article: empty = indefinite, `d` = definite, `o` = none (mass: `no:αίμα`).
- Look case is **acc**. Masculine -ος → acc drop ς (`μάγος` → `μάγο`). Feminine -ος (`ράβδος`) → `acc=ράβδο|gen=ράβδου`.
- `_` in a name is a space; use real spaces in Greek.
- Block 7: **lowercase** kind replaces the type and **must** have a prefix. **Uppercase** proper name stays unprefixed and uses `grammar.look.named`.
- Empty English slots stay empty.

Adjective pattern (block 5):

```
{0,select,m.acc{σπασμένο}m.gen{σπασμένου}f.gen{σπασμένης}n.gen{σπασμένου}f{σπασμένη}n{σπασμένο}other{σπασμένος}}
```

Stress belongs on the ending when the stem is unstressed (`γερός`, not `γερος`).

## Grammar already in `el.tsv` (do not break)

```
grammar.rule.genders          m f n p
grammar.rule.cases            nom gen acc
grammar.rule.case.look        acc
grammar.article.indefinite    m.acc{έναν {0}} … f{μια {0}} n{ένα {0}} other{ένας {0}}
grammar.look.you_see          Βλέπεις {0}.
grammar.look.named            {0} ονόματι {1}
hud.item.cursed               {0} ({0,select,f{καταραμένη}n{καταραμένο}other{καταραμένος}})
prompt.use_on_what            Να χρησιμοποιηθεί {0} σε τι;
```

`{0}` on a name already carries the article. Do not write `το {0}` in a frame.

## How to patch strings

UTF-8 TSV: `block TAB index TAB text`. A `#@ checksum` line **immediately before** each entry must stay; it is the English checksum, not the translation. Keep trailing `\n` as the two characters `\` `n`. Keep leading/trailing spaces on pieces.

Do not replace a line by deleting the checksum. Prefer a small Python dict keyed by `(block, index)`.

## Check after each block

```
uwdump validate-tsv "<UW1 DATA>" Languages\el.strings.tsv --language el
uwdump looks "<UW1 DATA>" --strings Languages\el.strings.tsv
uwdump fit "<UW1 DATA>" --strings Languages\el.strings.tsv --over
```

Capture uwdump as UTF-8 (Python `subprocess`, not PowerShell `Out-File`). Expect `?` on `fit` for Greek in pixel boxes. 0 errors required.

In-game smoke: Language → Ελληνικά, look at a goblin, a door, a rune, open the spell list after block 6.

## Publish

- `el.tsv` may go to the UR GitHub by PR.
- `el.strings.tsv` / UW2 strings are Origin text: **do not** put them in that repo.

## Known nits (fix only if you touch that area)

- Counts of stacked items may keep a singular adjective (`2 κατεστραμμένο γιλέκο`). Wrap adjectives in `{0,plural,one{…}other{…}}` if you start seeing it in play.
- `grammar.look.of` is now ` (μαγεία: {0})`, following upstream `de.tsv` (`(Zauber: {0})`): `{0}` is a nominative block 6 label of mixed gender, so `του`/`της` would be wrong and no case is applied.
- Hunger/fatigue adjectives in block 1 are masculine-only (`πεινασμένος`); fine for the Avatar as m (confirmed intended).
- Block 1 ordinals are neuter (`πρώτο`) so they fit `επίπεδο` and `εικοσιτετράωρο`.
- Repair estimate is two lines in-game (`Να γίνει απόπειρα;` after `\n`).

## Scratch from the last session (optional)

`C:\Users\kzagoris\AppData\Local\Temp\patch_el_names.py`  
`C:\Users\kzagoris\AppData\Local\Temp\patch_el_block1.py`  
`C:\Users\kzagoris\AppData\Local\Temp\patch_el_block6.py`  
`C:\Users\kzagoris\AppData\Local\Temp\patch_el_block2.py`  
`C:\Users\kzagoris\AppData\Local\Temp\patch_el_block10.py`  
`C:\Users\kzagoris\AppData\Local\Temp\patch_el_block5_keys.py`  
`C:\Users\kzagoris\AppData\Local\Temp\patch_el_block9.py`  
`C:\Users\kzagoris\AppData\Local\Temp\run_uwdump.py`  
Reuse the `nm()` / `adj()` helpers if you extend names. Do not re-run them blindly; they replace whole blocks.
