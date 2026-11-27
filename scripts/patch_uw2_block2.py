# -*- coding: utf-8 -*-
from pathlib import Path

UW1 = Path(r"C:\Games\UnderworldRevisited\Languages\el.strings.tsv")
UW2 = Path(r"C:\Games\UnderworldRevisited\Languages\UW2\el.strings.tsv")


def parse_block(path: Path, block: int):
    bychk = {}
    byidx = {}
    chk = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#@ "):
            chk = line[3:].strip()
            continue
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t", 2)
        if len(parts) < 3:
            continue
        b, i, t = int(parts[0]), int(parts[1]), parts[2]
        if b == block and chk:
            bychk[chk] = t
            byidx[i] = (chk, t)
        chk = None
    return bychk, byidx


uw1_chk, uw1_idx = parse_block(UW1, 2)

# UW2-only (or different English) — skills follow glossary Unarmed/Sneak/Charm
NEW = {
    7: "Διάλεξε δυσκολία:",  # same EN as UW1, different checksum
    34: "Άοπλη μάχη",  # Barehand
    45: "Λαθροκίνηση",  # Stealth
    47: "Γοητεία",  # Charisma
    132: "Βαθμ. δεξ.",  # Skill Pt (HUD-short)
}

# Mantras 52–77 stay English (ATTACK…SWIMMING, INSAHN, FANLO, NO, SUMM RA, MU AHM, OM CAH)

lines = UW2.read_text(encoding="utf-8").splitlines(keepends=True)
out = []
chk = None
n = 0
for line in lines:
    if line.startswith("#@ "):
        chk = line[3:].strip()
        out.append(line)
        continue
    parts = line.rstrip("\n").split("\t", 2)
    if chk and len(parts) == 3 and int(parts[0]) == 2:
        b, i, t = int(parts[0]), int(parts[1]), parts[2]
        new = None
        if i in NEW:
            new = NEW[i]
        elif chk in uw1_chk:
            new = uw1_chk[chk]
        # mantras / unmatched English stay
        if new is not None and new != t:
            nl = "\n" if line.endswith("\n") else ""
            out.append(f"{b}\t{i}\t{new}{nl}")
            n += 1
        else:
            out.append(line)
        chk = None
        continue
    out.append(line)
    chk = None

UW2.write_text("".join(out), encoding="utf-8")
print(f"patched {n} UW2 block 2 rows")
