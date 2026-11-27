from pathlib import Path

from PIL import Image, ImageDraw


SCRATCH = Path(__file__).resolve().parent
SRC = SCRATCH / "pic-template"
DST = Path(r"C:\Games\UnderworldRevisited\Languages\el\pictures")

FG_NORMAL = (204, 204, 220, 255)
FG_PRESSED = (252, 252, 252, 255)
SHADOW = (0, 0, 0, 255)
ENGLISH_INK = {FG_NORMAL, FG_PRESSED, (220, 220, 220, 255)}

# Five-pixel capitals, with extra columns for diagonals and counters that need them.
FONT = {
    "Α": (".#.", "#.#", "###", "#.#", "#.#"),
    "Β": ("##.", "#.#", "##.", "#.#", "##."),
    "Γ": ("###", "#..", "#..", "#..", "#.."),
    "Δ": ("..#..", "..#..", ".#.#.", ".#.#.", "#####"),
    "Ε": ("###", "#..", "##.", "#..", "###"),
    "Ζ": ("###", "..#", ".#.", "#..", "###"),
    "Η": ("#.#", "#.#", "###", "#.#", "#.#"),
    "Θ": (".#.", "#.#", "###", "#.#", ".#."),
    "Ι": ("#", "#", "#", "#", "#"),
    "Κ": ("#.#", "#.#", "##.", "#.#", "#.#"),
    "Λ": (".#.", "#.#", "#.#", "#.#", "#.#"),
    "Μ": ("#...#", "##.##", "#.#.#", "#...#", "#...#"),
    "Ν": ("#...#", "##..#", "#.#.#", "#..##", "#...#"),
    "Ξ": ("###", "...", ".#.", "...", "###"),
    "Ο": (".#.", "#.#", "#.#", "#.#", ".#."),
    "Π": ("###", "#.#", "#.#", "#.#", "#.#"),
    "Ρ": ("##.", "#.#", "##.", "#..", "#.."),
    "Σ": ("###", "#..", ".#.", "#..", "###"),
    "Τ": ("###", ".#.", ".#.", ".#.", ".#."),
    "Υ": ("#.#", "#.#", ".#.", ".#.", ".#."),
    "Φ": ("..#..", ".###.", "#.#.#", ".###.", "..#.."),
    "Χ": ("#.#", "#.#", ".#.", "#.#", "#.#"),
    "Ψ": ("#.#.#", "#.#.#", ".###.", "..#..", "..#.."),
    "Ω": (".###.", "#...#", "#...#", ".#.#.", "##.##"),
    ".": (".", ".", ".", ".", "#"),
    ":": (".", "#", ".", "#", "."),
    ";": ("..", ".#", "..", ".#", "#."),
}

# These pairs have room in their outlines for adjacent bounding boxes.
# Keep punctuation separate: the Greek question mark needs a visible comma tail.
TIGHT_PAIRS = {"ΡΤ", "ΤΩ", "ΓΟ"}
# A two-column gamma gives the long confirmation a real punctuation gap.
# Its full top bar and vertical stem still distinguish it from iota.
COMPACT_GAMMA = ("##", "#.", "#.", "#.", "#.")

# Normal and pressed templates are consecutive image IDs.
BUTTON_PAIRS = {
    0x06: ("ΣΩΣΕ",),
    # A syllable break preserves full-width phi/omega and the original bevel.
    0x08: ("ΦΟΡ", "ΤΩΣΗ"),
    0x0A: ("ΜΟΥΣΙΚΗ",),
    0x0C: ("ΗΧΟΣ",),
    0x0E: ("ΛΕΠΤ.",),
    0x10: ("ΠΙΣΩ",),
    0x12: ("ΕΞΟΔΟΣ",),
    0x14: ("ΝΑΙ",),
    0x16: ("ΟΧΙ",),
    0x18: ("ΑΚΥΡΟ",),
    0x1A: ("ΕΤΟΙΜΟ",),
    0x1C: ("ΕΤΟΙΜΟ",),
    0x26: ("ΧΑΜΗΛΗ",),
    0x28: ("ΜΕΣΑΙΑ",),
    0x2A: ("ΥΨΗΛΗ",),
    0x2C: ("ΠΟΛΥ", "ΥΨΗΛΗ"),
    0x39: ("ΝΑΙ",),
    0x3B: ("ΟΧΙ",),
}

HEADINGS = {
    0x2E: ("ΦΟΡ", "ΤΩΣΗ:"),
    0x2F: ("ΜΟΥΣΙΚΗ:", "ΝΑΙ"),
    0x30: ("ΜΟΥΣΙΚΗ:", "ΟΧΙ"),
    0x31: ("ΗΧΟΣ:", "ΝΑΙ"),
    0x32: ("ΗΧΟΣ:", "ΟΧΙ"),
    0x33: ("ΜΟΥΣΙΚΗ:",),
    0x34: ("ΗΧΟΣ:",),
    0x35: ("ΛΕΠΤ.:", "ΧΑΜΗΛΗ"),
    0x36: ("ΛΕΠΤ.:", "ΜΕΣΑΙΑ"),
    0x37: ("ΛΕΠΤ.:", "ΥΨΗΛΗ"),
    0x38: ("ΛΕΠΤ.:", "ΠΟΛΥ", "ΥΨΗΛΗ"),
}

PANEL_BUTTONS = {
    0x01: ((0x06, 2), (0x08, 17), (0x0A, 32), (0x0C, 47),
           (0x0E, 62), (0x10, 77), (0x12, 92)),
    0x02: ((0x18, 77),),
    0x03: ((0x39, 32), (0x3B, 47)),
    0x04: ((0x14, 32), (0x16, 47), (0x1A, 62)),
    0x05: ((0x26, 32), (0x28, 47), (0x2A, 62), (0x2C, 77), (0x1C, 92)),
}

# Keep each panel's heading texture, including the rim of panel 05.
# Each entry gives the erase boundary, Greek lines, and their cap-height start rows.
PANEL_HEADINGS = {
    0x02: (16, ("ΣΩΣΕ:",), (6,)),
    0x03: (32, ("ΕΞΟΔΟΣ:", "ΕΙΣΑΙ", "ΣΙΓΟΥΡΟΣ;"), (6, 18, 25)),
    0x04: (32, HEADINGS[0x2F] + HEADINGS[0x33], (4, 10, 21)),
    0x05: (32, HEADINGS[0x35] + ("ΝΕΟ", "ΕΠΙΠΕΔΟ:"), (2, 8, 19, 25)),
}


def filename(code):
    return f"OPTBTNS_{code:02X}.png"


def template(code, size):
    with Image.open(SRC / filename(code)) as source:
        if source.size != size:
            raise ValueError(f"{filename(code)} has size {source.size}, expected {size}")
        return source.convert("RGBA")


def erase_english(im, rect, shadow_left=None):
    """Replace only original lettering and its shadow with nearby texture colors."""
    x0, y0, x1, y1 = rect

    def in_rect(x, y):
        return x0 <= x < x1 and y0 <= y < y1

    px = im.load()
    ink = {(x, y) for y in range(y0, y1) for x in range(x0, x1)
           if px[x, y] in ENGLISH_INK}
    if shadow_left is None:
        shadow_left = x0
    # The English font casts black to the left and below, including the corner.
    shadow_candidates = {(x + dx, y + dy) for x, y in ink
                         for dx, dy in ((-1, 0), (-1, 1), (0, 1))}
    pending = ink | {(x, y) for x, y in shadow_candidates
                     if x >= shadow_left and in_rect(x, y) and px[x, y] == SHADOW}

    # Fill in waves from the surrounding texture. Choose a sampled RGBA value,
    # keeping the local palette intact and leaving every unmasked pixel alone.
    cardinal = ((-1, 0), (1, 0), (0, -1), (0, 1))
    diagonal = ((-1, -1), (1, -1), (-1, 1), (1, 1))
    while pending:
        replacements = {}
        for x, y in pending:
            for offsets in (cardinal, diagonal):
                neighbors = [px[x + dx, y + dy] for dx, dy in offsets
                             if in_rect(x + dx, y + dy)
                             and (x + dx, y + dy) not in pending
                             and px[x + dx, y + dy] != SHADOW
                             and px[x + dx, y + dy] not in ENGLISH_INK]
                if neighbors:
                    mean = [sum(c[i] for c in neighbors) / len(neighbors) for i in range(4)]
                    replacements[x, y] = min(
                        neighbors, key=lambda c: sum((a - b) ** 2 for a, b in zip(c, mean))
                    )
                    break
        if not replacements:
            raise ValueError(f"No texture samples for English text in {rect}")
        for point, color in replacements.items():
            px[point] = color
        pending.difference_update(replacements)
    if any(px[x, y] in ENGLISH_INK for y in range(y0, y1) for x in range(x0, x1)):
        raise ValueError(f"English foreground remains in {rect}")


def paint_text(im, lines, start_rows, x_bounds, fg=FG_NORMAL):
    """Center the Greek ink and its one-pixel shadow within the horizontal bounds."""
    x0, x1 = x_bounds
    ink = set()
    for line, y in zip(lines, start_rows, strict=True):
        letters = set()
        previous = ""
        advance = 0
        for ch in line:
            if previous and previous + ch not in TIGHT_PAIRS:
                advance += 1
            glyph = COMPACT_GAMMA if ch == "Γ" and line == "ΣΙΓΟΥΡΟΣ;" else FONT[ch]
            points = {(advance + col, y + row)
                      for row, bits in enumerate(glyph) for col, bit in enumerate(bits)
                      if bit == "#"}
            if any((x - 1, row) in letters for x, row in points):
                raise ValueError(f"Touching letters in {line!r}")
            letters.update(points)
            advance += len(glyph[0])
            previous = ch
        start_x = x0 + (x1 - x0 - advance + 1) // 2
        ink.update((start_x + x, row) for x, row in letters)

    shadow = {(x - 1, y + 1) for x, y in ink}
    if any(not (x0 <= x < x1 and 0 <= y < im.height) for x, y in ink | shadow):
        raise ValueError(f"Text {lines!r} exceeds bounds {x_bounds} at rows {start_rows}")
    px = im.load()
    for point in shadow:
        px[point] = SHADOW
    for point in ink:
        px[point] = fg
    return ink, shadow


def generate():
    images = {}
    for normal, lines in BUTTON_PAIRS.items():
        # Six rows including shadow: center within the 12-row button face.
        rows = (4,) if len(lines) == 1 else (1, 7)
        for code, fg in ((normal, FG_NORMAL), (normal + 1, FG_PRESSED)):
            im = template(code, (31, 14))
            erase_english(im, (0, 1, 31, 13), shadow_left=1)
            paint_text(im, lines, rows, (1, 30), fg)
            images[code] = im

    for code, lines in HEADINGS.items():
        if code == 0x38:
            size, rows = (34, 18), (0, 6, 12)
        elif code >= 0x35:
            size, rows = (34, 18), (2, 10)
        else:
            size, rows = (31, 14), (5,) if len(lines) == 1 else (2, 8)
        im = template(code, size)
        erase_english(im, (0, 0, *size))
        bounds = (0, im.width) if im.width == 31 else (1, im.width - 1)
        paint_text(im, lines, rows, bounds)
        images[code] = im

    for code, buttons in PANEL_BUTTONS.items():
        im = template(code, (35, 108))
        if code in PANEL_HEADINGS:
            bottom, lines, rows = PANEL_HEADINGS[code]
            erase_english(im, (0, 0, im.width, bottom))
            paint_text(im, lines, rows, (2, 33))
        for button, y in buttons:
            im.paste(images[button], (1, y))
        images[code] = im

    validate_images(images)
    return images


def validate_images(images):
    """Check palette, dimensions and exact panel/button identity before saving."""
    assert len(images) == 52, f"Expected 52 images, got {len(images)}"
    for ch, glyph in FONT.items():
        assert len(glyph) == 5 and len(set(map(len, glyph))) == 1, f"Malformed glyph: {ch}"
    assert len(set(FONT.values())) == len(FONT), "Duplicate glyph silhouettes"
    palette = set()
    for code, im in images.items():
        expected = (35, 108) if code in PANEL_BUTTONS else (34, 18) if 0x35 <= code <= 0x38 else (31, 14)
        assert im.size == expected, filename(code)
        palette.update(template(code, expected).get_flattened_data())
    for code, im in images.items():
        assert set(im.get_flattened_data()) <= palette, f"Non-original palette color: {filename(code)}"
    for code, buttons in PANEL_BUTTONS.items():
        for button, y in buttons:
            crop = images[code].crop((1, y, 32, y + 14))
            assert crop.tobytes() == images[button].tobytes(), f"Panel/button mismatch: {code:02X}/{button:02X}"


def draw_preview(path, images, codes, dimensions, columns, step, origin, label_gap):
    sheet = Image.new("RGBA", dimensions, (25, 25, 25, 255))
    labels = ImageDraw.Draw(sheet)
    for index, code in enumerate(codes):
        row, column = divmod(index, columns)
        x, y = origin[0] + column * step[0], origin[1] + row * step[1]
        labels.text((x, y), f"OPTBTNS_{code:02X}", fill=(255, 255, 100, 255))
        im = images[code]
        zoom = im.resize((im.width * 3, im.height * 3), Image.Resampling.NEAREST)
        sheet.alpha_composite(zoom, (x, y + label_gap))
    sheet.save(path)


def main():
    images = generate()
    DST.mkdir(parents=True, exist_ok=True)
    for code, im in sorted(images.items()):
        im.save(DST / filename(code))

    draw_preview(SCRATCH / "el_optbtns_panels.png", images, sorted(PANEL_BUTTONS),
                 (620, 360), 5, (120, 0), (10, 4), 16)
    buttons = sorted(images.keys() - PANEL_BUTTONS.keys())
    draw_preview(SCRATCH / "el_optbtns_buttons.png", images, buttons,
                 (700, 610), 6, (115, 75), (8, 8), 14)
    print(f"Generated {len(images)} OPTBTNS PNGs into {DST} and saved two 3x previews")


if __name__ == "__main__":
    main()

