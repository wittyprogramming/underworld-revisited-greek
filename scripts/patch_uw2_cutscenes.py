# -*- coding: utf-8 -*-
from pathlib import Path

path = Path(r"C:\Games\UnderworldRevisited\Languages\UW2\el.strings.tsv")
lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

T = {
(3072, 1): "Αγαπητέ Άβαταρ,\\nΧαίρε, παλιέ μου φίλε!",
(3072, 2): "Ελπίζω η επιστολή αυτή να σε βρίσκει σε καλή υγεία",
(3072, 3): "Έχει περάσει σχεδόν ένας χρόνος από τότε που νίκησες τον Guardian.",
(3072, 4): "Σε αυτό το διάστημα αποκαταστήσαμε μεγάλο μέρος της ζημιάς από την επίθεση του Guardian.",
(3072, 5): "Αλλά αν και το έργο είναι μεγάλο,",
(3072, 6): "Ήρθε η ώρα να χαρούμε όσα έχουμε καταφέρει.",
(3072, 7): "Στην επέτειο του θριάμβου σου,",
(3072, 8): "Θα τελέσουμε τη Γιορτή της Ανοικοδόμησης στο κάστρο μου στη Britain.",
(3072, 9): "Εκεί θα τιμήσουμε τη νίκη σου και θα ξαναζήσουμε παλιές περιπέτειες.",
(3072, 10): "Θα τιμήσεις την πρόσκλησή μου αν έρθεις.",
(3072, 11): "Πάντα φίλος σου,\\nLord British",
(3072, 12): "Η Βρεταννία κοιμάται ειρηνικά.",
(3072, 13): "Αλλά το επόμενο πρωί_._._._.",
(3074, 1): "Για άλλη μια φορά νίκησες τον Guardian.",
(3074, 2): "Έσπασες \\nτην κατάρα του οψιδιανού κοσμήματος,",
(3074, 3): "με τη δύναμη των στιβαρών \\nχεριών σου και του γρήγορου νου σου,",
(3074, 4): "κι έφυγε από πάνω μας, \\nσαν πυρετώδες όνειρο.",
(3074, 5): "Είμαστε ξανά σε ειρήνη, Άβαταρ, \\nκαι πρέπει να επιστρέψουμε",
(3074, 6): "στο έργο της ανοικοδόμησης \\nτου έθνους μας.",
(3074, 7): "Έλα! Ήρθε η ώρα να αναπνεύσουμε ξανά",
(3074, 8): "τον γλυκό αέρα της Βρεταννίας.",
(3076, 1): "Ίσως βλέπεις εδώ\\nτο μέλλον σου.",
(3077, 1): "Ίσως ο κόσμος σου να βρει\\nτέτοια ειρήνη.",
(3078, 1): "Έτσι, όσοι μου αντιτίθενται.",
(3079, 1): "Αυτός ο κόσμος είναι δικός μου.\\nΣου αρέσει αυτό που βλέπεις;",
(3096, 1): "Χαίρε, Άβαταρ!",
(3096, 2): "Οι φίλοι μου κι εγώ ξεκινάμε λίγες διακοπές.",
(3096, 3): "Ακούω πως οι παραλίες κοντά στο Cove είναι ωραίες.",
(3096, 4): "Μακάρι να ήσουν κι εσύ εδώ...!",
(3097, 1): "Τα στρατεύματά μου συνάντησαν τον φίλο σου, τον Lord Draxinusom.",
(3097, 2): "Θα του μεταφέρω τους χαιρετισμούς σου...",
(3098, 1): "Κάνω πολλούς νέους φίλους στη Βρεταννία.",
(3099, 1): "Σύντομα θα είμαι μαζί σου, Άβαταρ.",
(3099, 2): "Μην φεύγεις_._._._.",
(3100, 1): "Κέρδισα άλλον έναν στην υπόθεσή μου.",
(3101, 1): "Τα ανήμπορα σπαρταρίσματά σου με διασκεδάζουν.",
(3102, 1): "Σκέψου τι δύναμη θα μπορούσε να είναι δική σου.",
(3104, 1): "Ναι, British,\\nhasten to thy vain struggle",
}

# fix 3104,1 accidentally mixed - rewrite all remaining in this dict properly
T[(3104, 1)] = "Ναι, British,\\nτρέξε στον μάταιο αγώνα σου"
T[(3104, 2)] = "Αλλά γνώριζε τούτο --"
T[(3104, 3)] = "όσοι διαλέξουν να με υπηρετήσουν\\nθα γλιτώσουν."
T[(3104, 4)] = "Όλοι οι άλλοι\\nθα σαπίσουν μέσα σε αυτούς τους τοίχους."
T[(3112, 1)] = T[(3076, 1)]
T[(3113, 1)] = T[(3077, 1)]
T[(3114, 1)] = T[(3078, 1)]
T[(3115, 1)] = T[(3079, 1)]

out = []
i = 0
n = 0
while i < len(lines):
    line = lines[i]
    if line.startswith("#@"):
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        parts = nxt.split("\t", 2)
        if len(parts) >= 2 and parts[0].isdigit():
            key = (int(parts[0]), int(parts[1]))
            if key in T:
                nl = "\n" if nxt.endswith("\n") else ""
                if nxt.endswith("\r\n"):
                    nl = "\r\n"
                out.append(line)
                out.append(f"{key[0]}\t{key[1]}\t{T[key]}{nl if not T[key].endswith(chr(10)) else ''}")
                # keepends already on original; write with \n
                if not nxt.endswith("\n"):
                    pass
                i += 2
                n += 1
                continue
    out.append(line)
    i += 1

# rewrite more carefully with keepends
text = path.read_text(encoding="utf-8")
raw = text.splitlines(keepends=True)
out = []
i = 0
n = 0
while i < len(raw):
    line = raw[i]
    if line.startswith("#@"):
        nxt = raw[i + 1] if i + 1 < len(raw) else ""
        body = nxt.rstrip("\r\n")
        parts = body.split("\t", 2)
        if len(parts) >= 2 and parts[0].isdigit():
            key = (int(parts[0]), int(parts[1]))
            if key in T:
                ending = nxt[len(body):]
                out.append(line)
                out.append(f"{key[0]}\t{key[1]}\t{T[key]}{ending}")
                i += 2
                n += 1
                continue
    out.append(line)
    i += 1

path.write_text("".join(out), encoding="utf-8")
print("patched", n, "expected", len(T))
missing = set(T) 
# recount keys actually in file
found=set()
i=0
raw=path.read_text(encoding='utf-8').splitlines()
for i,l in enumerate(raw):
    if not l.startswith('#') and l.strip():
        p=l.split('\t',2)
        if len(p)>=3 and p[0].isdigit():
            k=(int(p[0]),int(p[1]))
            if k in T:
                found.add(k)
print('in file', len(found), 'dict', len(T), 'not in file', set(T)-found)
