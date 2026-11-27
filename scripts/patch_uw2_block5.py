# -*- coding: utf-8 -*-
from pathlib import Path

UW1 = Path(r"C:\Games\UnderworldRevisited\Languages\el.strings.tsv")
UW2 = Path(r"C:\Games\UnderworldRevisited\Languages\UW2\el.strings.tsv")


def parse(path):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    by_en = {}
    by_idx = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#@ ") and i + 1 < len(lines):
            nxt = lines[i + 1]
            parts = nxt.rstrip("\n").split("\t", 2)
            if len(parts) == 3 and parts[0] == "5":
                idx = int(parts[1])
                text = parts[2]
                by_idx[idx] = text
                by_en[text] = text  # placeholder
        i += 1
    return lines, by_idx


def parse_uw1_en_el():
    """Need English originals for UW1 — they are already Greek. Match UW2 English to UW1 Greek via checksum or known English list."""
    return None


# UW1 Greek by English (from UW1 block 5 + English originals)
EN_EL = {}

uw1_lines = UW1.read_text(encoding="utf-8").splitlines()
uw1_el = {}
i = 0
while i < len(uw1_lines):
    if uw1_lines[i].startswith("#@ ") and i + 1 < len(uw1_lines):
        parts = uw1_lines[i + 1].split("\t", 2)
        if len(parts) == 3 and parts[0] == "5":
            uw1_el[int(parts[1])] = parts[2]
    i += 1

# UW2 English by index
uw2_en = {}
uw2_lines = UW2.read_text(encoding="utf-8").splitlines()
i = 0
while i < len(uw2_lines):
    if uw2_lines[i].startswith("#@ ") and i + 1 < len(uw2_lines):
        parts = uw2_lines[i + 1].split("\t", 2)
        if len(parts) == 3 and parts[0] == "5":
            uw2_en[int(parts[1])] = parts[2]
    i += 1

# Map English -> UW1 Greek using same index when English matches original UW1 English
# Original UW1 English is implicit: UW2 1-84,97-100 English equals UW1 English for those indices.
COPY_IDX = list(range(1, 85)) + [97, 98, 99, 100]
by_english = {}
for idx in COPY_IDX:
    if idx in uw1_el and idx in uw2_en:
        by_english[uw2_en[idx]] = uw1_el[idx]

def adj_os(stem):
    """-ος -η -ο (άριστος, μικρός, ...) stem includes accent as in nom m."""
    # stem is masculine nom without ς? We pass full forms.
    raise NotImplementedError


NEW = {
    87: "{0,select,m.acc{πελεκημένο}m.gen{πελεκημένου}f.gen{πελεκημένης}n.gen{πελεκημένου}f{πελεκημένη}n{πελεκημένο}other{πελεκημένος}}",
    88: "{0,select,m.acc{γδαρμένο}m.gen{γδαρμένου}f.gen{γδαρμένης}n.gen{γδαρμένου}f{γδαρμένη}n{γδαρμένο}other{γδαρμένος}}",
    102: "Το κλειδί είναι φθαρμένο και θαμπό από την πολλή χρήση.\\n",
    103: "Το κλειδί νιώθει αφύσικα βαρύ.\\n",
    104: "Αυτό το κλειδί είναι ένθετο με αρκετούς φανταχτερούς πολύτιμους λίθους, που μοιάζουν ψεύτικοι.\\n",
    105: "Το κλειδί φέρει μια δυσανάγνωστη επιγραφή.\\n",
    106: "Το κλειδί είναι χαραγμένο με κυματιστές γραμμές και αδέξια ψάρια.\\n",
    107: "Η λαβή αυτού του κλειδιού είναι σκαλισμένη σε μορφή μιας έξαλλης δαιμονικής φιγούρας.\\n",
    108: "Τα αρχικά «A.S.G.» είναι χαραγμένα στη λαβή αυτού του κλειδιού.\\n",
    109: "Η λαβή του κλειδιού είναι ραβδωτή για εύκολο πιάσιμο.\\n",
    110: "Το κλειδί μοιάζει να έχει λερωθεί από ένα διαβρωτικό υγρό.\\n",
    111: "Το κλειδί είναι ελαφρώς λυγισμένο κοντά στη λαβή.\\n",
    112: "Υπάρχει μια λάμψη βλεννώδους υπολείμματος πάνω σε αυτό το κλειδί.\\n",
    118: "Η μεταλλική λαβή αυτού του κλειδιού φέρει αποτυπωμένο ένα χαμογελαστό πρόσωπο.\\n",
    119: "Το κλειδί νιώθει αφύσικα κρύο στην αφή.\\n",
    120: "Το κλειδί είναι χαραγμένο με ένα ασημένιο φίδι.",
    121: "Το κλειδί φέρει βαθιές γρατζουνιές, σαν κάποιος να προσπάθησε κάποτε να το καταστρέψει.\\n",
    122: "Το κλειδί είναι καλυμμένο με αλάτι.\\n",
    123: "Το κλειδί μοιάζει να έχει λιώσει εν μέρει.",
    124: "Αδέξιοι ρούνοι είναι σκαριφημένοι πάνω σε αυτό το κλειδί.\\n",
    126: "Αυτό το κλειδί έλκει μικρά μεταλλικά αντικείμενα προς τον εαυτό του.\\n",
    128: "Αυτό το κλειδί έχει επικαλυφθεί με μια παράξενη ρητίνη, που τώρα αρχίζει να ξεφλουδίζει.\\n",
    129: "Το κλειδί είναι φτιαγμένο από σκούρο μέταλλο διάστικτο με μικροσκοπικές κηλίδες χρυσού.\\n",
}

# 85 cracked = 74, 86 battered = 32, 89 smooth = 17, 90 perfect = 47
for src, dst in ((74, 85), (32, 86), (17, 89), (47, 90)):
    NEW[dst] = uw1_el[src]

patch = dict(NEW)
for idx, en in uw2_en.items():
    if idx in patch:
        continue
    if en in by_english:
        patch[idx] = by_english[en]
    elif idx in uw1_el and not en.startswith("{0"):
        # leftover: if same index used for keys with different English, skip
        pass

# Fix escaped newlines in NEW: file stores literal \n as two chars
# Python string "\\n" is backslash-n which is what TSV has.

missing = [idx for idx in uw2_en if idx not in patch]
print("missing", missing)
print("patched", len(patch))

text = UW2.read_text(encoding="utf-8")
out_lines = []
lines = text.splitlines(keepends=True)
i = 0
n = 0
while i < len(lines):
    line = lines[i]
    out_lines.append(line)
    if line.startswith("#@ ") and i + 1 < len(lines):
        nxt = lines[i + 1]
        parts = nxt.rstrip("\n").split("\t", 2)
        if len(parts) == 3 and parts[0] == "5":
            idx = int(parts[1])
            if idx in patch:
                nl = "\n" if nxt.endswith("\n") else ""
                out_lines.append(f"5\t{idx}\t{patch[idx]}{nl}")
                i += 2
                n += 1
                continue
    i += 1

UW2.write_text("".join(out_lines), encoding="utf-8")
print("wrote", n)
