# -*- coding: utf-8 -*-
from pathlib import Path

UW1 = Path(r"C:\Games\UnderworldRevisited\Languages\el.strings.tsv")
UW2 = Path(r"C:\Games\UnderworldRevisited\Languages\UW2\el.strings.tsv")


def load_block(path, block):
    lines = path.read_text(encoding="utf-8").splitlines()
    by_cs = {}
    by_en = {}
    i = 0
    while i < len(lines):
        if lines[i].startswith("#@ ") and i + 1 < len(lines):
            cs = lines[i][3:].strip()
            parts = lines[i + 1].split("\t", 2)
            if len(parts) == 3 and parts[0] == block:
                text = parts[2]
                by_cs[cs] = text
                by_en[text] = text
        i += 1
    return lines, by_cs


uw1_lines, uw1_cs = load_block(UW1, "6")
uw2_lines, _ = load_block(UW2, "6")

uw1_en_to_el = {}
i = 0
# We only have Greek in UW1; map via checksum later.

NEW_EN = {
    "Bouncing": "Αναπήδηση",
    "Bounce": "Αναπήδηση",
    "Valor": "Ανδρεία",
    "Poison Weapon": "Δηλητηριασμένο όπλο",
    "Invisibilty": "Αορατότητα",
    "Acid Spit": "Φτύσιμο οξέος",
    "Deadly Seeker": "Θανάσιμος αναζητητής",
    "Snowballs": "Χιονόμπαλες",
    "Mass Confusion": "Μαζική σύγχυση",
    "Shockwave": "Κρουστικό κύμα",
    "Frost": "Παγετός",
    "Bleeding": "Αιμορραγία",
    "Charm": "Γοητεία",
    "Smite Foe": "Πλήγμα εχθρού",
    "Study Monster": "Μελέτη τέρατος",
    "Dispel Rune": "Διάλυση ρούνου",
    "Mending": "Επιδιόρθωση",
    "Detect Trap": "Ανίχνευση παγίδας",
    "Enchantment": "Μάγευμα",
    "Rune Of Flame": "Ρούνος φλόγας",
    "Rune of Flame": "Ρούνος φλόγας",
    "Rune Of Stasis": "Ρούνος στάσης",
    "Rune of Stasis": "Ρούνος στάσης",
    "Summon Demon": "Κλήση δαίμονα",
    "Portal": "Πύλη",
    "Restoration": "Αποκατάσταση",
    "Locate": "Εντοπισμός",
    "Dispel Hunger": "Διάλυση πείνας",
    "Altara": "Altara",
    "Mind Blast": "Πλήγμα νου",
    "Basilisk Oil": "Λάδι βασιλίσκου",
    "Map Area": "Χαρτογράφηση περιοχής",
    "Luck": "Τύχη",
    "Leaping": "Άλμα",
    "Lightning": "Κεραυνός",
    "Repel Undead": "Απόθηση νεκροζώντανων",
    "Magic Satellite": "Μαγικός δορυφόρος",
    "Minor Accuracy": "Μικρή ακρίβεια",
    "Major Accuracy": "Μεγάλη ακρίβεια",
    "Great Accuracy": "Σπουδαία ακρίβεια",
    "Unsurpassed Accuracy": "Αξεπέραστη ακρίβεια",
    "Minor Damage": "Μικρή ζημιά",
    "Major Damage": "Μεγάλη ζημιά",
    "Great Damage": "Σπουδαία ζημιά",
    "Unsurpassed Damage": "Αξεπέραστη ζημιά",
    "LifeStealer": "Κλέφτης ζωής",
    "Undead Bane": "Όλεθρος νεκροζώντανων",
    "Fire Doom": "Πύρινος όλεθρος",
    "Stone Strike": "Πλήγμα πέτρας",
    "Unknown Special": "Άγνωστο ειδικό",
    "Entry": "Είσοδος",
}

# Extra English->Greek from known UW1 labels (when checksum differs)
KNOWN_EN = {
    "Darkness": "Σκοτάδι",
    "Burning Match": "Φλεγόμενο σπίρτο",
    "Candlelight": "Φως κεριού",
    "Light": "Φως",
    "Magic Lantern": "Μαγικό φανάρι",
    "Night Vision": "Νυχτερινή όραση",
    "Daylight": "Φως ημέρας",
    "Sunlight": "Ηλιακό φως",
    "Leap": "Άλμα",
    "Slow Fall": "Αργή πτώση",
    "Levitate": "Μετεωρισμός",
    "Water Walk": "Βάδισμα στο νερό",
    "Fly": "Πτήση",
    "Resist Blows": "Αντίσταση στα χτυπήματα",
    "Thick Skin": "Παχύ δέρμα",
    "Iron Flesh": "Σιδερένια σάρκα",
    "Curse": "Κατάρα",
    "Stealth": "Αθόρυβη κίνηση",
    "Conceal": "Απόκρυψη",
    "Invisibility": "Αορατότητα",
    "Missile Protection": "Προστασία από βλήματα",
    "Flameproof": "Πυράντοχο",
    "Poison Resistance": "Αντίσταση στο δηλητήριο",
    "Magic Protection": "Προστασία από μαγεία",
    "Greater Magic Protection": "Μεγάλη προστασία από μαγεία",
    "Lesser Heal": "Μικρή θεραπεία",
    "Heal": "Θεραπεία",
    "Enhanced Heal": "Ενισχυμένη θεραπεία",
    "Greater Heal": "Μεγάλη θεραπεία",
    "Magic Arrow": "Μαγικό βέλος",
    "Electrical Bolt": "Ηλεκτρικός κεραυνός",
    "Fireball": "Πύρινη σφαίρα",
    "Reveal": "Αποκάλυψη",
    "Sheet Lightning": "Πέπλο κεραυνού",
    "Flame Wind": "Φλόγινος άνεμος",
    "Cause Fear": "Πρόκληση φόβου",
    "Smite Undead": "Πλήγμα νεκροζώντανων",
    "Poison": "Δηλητήριο",
    "Paralyze": "Παράλυση",
    "Create Food": "Δημιουργία τροφής",
    "Summon Monster": "Κλήση τέρατος",
    "Cursed": "Καταραμένο",
    "Increase Mana": "Αύξηση μάνας",
    "Mana Boost": "Ενίσχυση μάνας",
    "Regain Mana": "Ανάκτηση μάνας",
    "Restore Mana": "Αποκατάσταση μάνας",
    "Speed": "Ταχύτητα",
    "Remove Trap": "Αφαίρεση παγίδας",
    "Name Enchantment": "Ονομασία μαγεύματος",
    "Open": "Άνοιγμα",
    "Cure Poison": "Θεραπεία δηλητηρίου",
    "Roaming Sight": "Περιπλανώμενη όραση",
    "Telekinesis": "Τηλεκίνηση",
    "Tremor": "Δόνηση",
    "Gate Travel": "Ταξίδι πύλης",
    "Freeze Time": "Πάγωμα χρόνου",
    "Armageddon": "Αρμαγεδδών",
    "Regeneration": "Αναγέννηση",
    "Mana Regeneration": "Αναγέννηση μάνας",
    "Hallucination": "Ψευδαίσθηση",
    "Mass Paralyze": "Μαζική παράλυση",
    "Acid": "Οξύ",
    "Local Teleport": "Τοπική τηλεμεταφορά",
    "Minor Protection": "Μικρή προστασία",
    "Protection": "Προστασία",
    "Additional Protection": "Επιπλέον προστασία",
    "Major Protection": "Μεγάλη προστασία",
    "Great Protection": "Σπουδαία προστασία",
    "Very Great Protection": "Πολύ σπουδαία προστασία",
    "Tremendous Protection": "Τεράστια προστασία",
    "Unsurpassed Protection": "Αξεπέραστη προστασία",
    "Minor Toughness": "Μικρή ανθεκτικότητα",
    "Toughness": "Ανθεκτικότητα",
    "Additional Toughness": "Επιπλέον ανθεκτικότητα",
    "Major Toughness": "Μεγάλη ανθεκτικότητα",
    "Great Toughness": "Σπουδαία ανθεκτικότητα",
    "Very Great Toughness": "Πολύ σπουδαία ανθεκτικότητα",
    "Tremendous Toughness": "Τεράστια ανθεκτικότητα",
    "Unsurpassed Toughness": "Αξεπέραστη ανθεκτικότητα",
}

out = []
i = 0
copied_cs = 0
copied_en = 0
new_n = 0
left = []
while i < len(uw2_lines):
    line = uw2_lines[i]
    if line.startswith("#@ ") and i + 1 < len(uw2_lines):
        cs = line[3:].strip()
        parts = uw2_lines[i + 1].split("\t", 2)
        if len(parts) == 3 and parts[0] == "6":
            en = parts[2]
            el = None
            src = None
            if cs in uw1_cs:
                el = uw1_cs[cs]
                src = "cs"
                copied_cs += 1
            elif en in KNOWN_EN:
                el = KNOWN_EN[en]
                src = "en"
                copied_en += 1
            elif en in NEW_EN:
                el = NEW_EN[en]
                src = "new"
                new_n += 1
            elif en == "":
                el = ""
                src = "empty"
            if el is None:
                left.append((parts[1], en, cs))
                out.append(line)
                out.append(uw2_lines[i + 1])
            else:
                out.append(line)
                out.append(f"{parts[0]}\t{parts[1]}\t{el}")
            i += 2
            continue
    out.append(line)
    i += 1

UW2.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"cs={copied_cs} en={copied_en} new={new_n} left={len(left)}")
for row in left:
    print(row)
