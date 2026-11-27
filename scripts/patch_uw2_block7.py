# -*- coding: utf-8 -*-
from pathlib import Path

path = Path(r"C:\Games\UnderworldRevisited\Languages\UW2\el.strings.tsv")
lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

GUARD = "m:φρουρός|acc=φρουρό|gen=φρουρού"
GOB_GUARD = "m:γκόμπλιν φρουρός|acc=γκόμπλιν φρουρό|gen=γκόμπλιν φρουρού"
SOLDIER = "m:στρατιώτης|acc=στρατιώτη|gen=στρατιώτη"

repl = {
    1: "Δεν μπορείς να μιλήσεις σ' αυτό!\\n",
    2: "Δεν παίρνεις απάντηση.\\n",
    3: " ότι παίρνω ",
    4: "...υποθέτω",
    5: "...ίσως νομίζω",
    6: "...νομίζω",
    7: "...είμαι σίγουρος",
    8: "...ξέρω",
    9: "μια φρικτή συμφωνία...",
    10: "μια πολύ κακή συμφωνία...",
    11: "μια κακή συμφωνία...",
    12: "μια φτωχή συμφωνία...",
    13: "μια ίση συμφωνία...",
    14: "μια καλή συμφωνία...",
    15: "μια πολύ καλή συμφωνία...",
    16: "μια σπουδαία συμφωνία...",
    17: "μια εξαιρετική συμφωνία...",
    18: GOB_GUARD,
    19: "m:γκόμπλιν",
    22: "m:γκόμπλιν οπλουργός|acc=γκόμπλιν οπλουργό|gen=γκόμπλιν οπλουργού",
    26: GOB_GUARD,
    27: GOB_GUARD,
    29: GOB_GUARD,
    30: GOB_GUARD,
    31: GOB_GUARD,
    32: GOB_GUARD,
    57: GUARD,
    65: "n:φωτάκι|gen=φωτακιού",
    68: SOLDIER,
    77: GUARD,
    92: GUARD,
    119: "m:πολεμιστής|acc=πολεμιστή|gen=πολεμιστή",
    121: SOLDIER,
    146: GUARD,
    166: GUARD,
    257: "m:κεραυνός|acc=κεραυνό|gen=κεραυνού",
    258: "m:βολβός ματιού|acc=βολβό ματιού|gen=βολβού ματιού",
    259: "f:φρικτή νυχτερίδα|gen=φρικτής νυχτερίδας",
    260: "n:παράξενο ψάρι|gen=παράξενου ψαριού",
    261: "f:σπείρα|gen=σπείρας",
    262: "m:κολασμένος σκύλος|acc=κολασμένο σκύλο|gen=κολασμένου σκύλου",
    263: "n:κρανίο|gen=κρανίου",
    264: "n:στόμα|gen=στόματος",
}

out = []
i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith("7\t"):
        parts = line.split("\t", 2)
        idx = int(parts[1])
        if idx in repl:
            nl = "\n" if line.endswith("\n") else ""
            line = f"7\t{idx}\t{repl[idx]}{nl}"
    out.append(line)
    i += 1

path.write_text("".join(out), encoding="utf-8")
print("patched", len(repl), "rows")
