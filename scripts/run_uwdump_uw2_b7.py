# -*- coding: utf-8 -*-
import subprocess
from pathlib import Path

uwdump = Path(r"C:\Games\UnderworldRevisited\UnderworldRevisited-0.26.0-TranslationKit-win64\uwdump.exe")
data = r"C:\Users\kzagoris\AppData\LocalLow\Underworld Revisited\Underworld Revisited\GameData\UW2\DATA"
tsv = r"C:\Games\UnderworldRevisited\Languages\UW2\el.strings.tsv"
cmd = [str(uwdump), "validate-tsv", data, tsv, "--game", "uw2", "--language", "el"]
p = subprocess.run(cmd, capture_output=True)
out = (p.stdout + p.stderr).decode("utf-8", errors="replace")
print(out)
print("exit", p.returncode)
