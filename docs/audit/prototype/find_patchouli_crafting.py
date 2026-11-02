import zipfile
from pathlib import Path

p = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar")
with zipfile.ZipFile(p) as z:
    for n in z.namelist():
        if n.startswith("assets/tfc/patchouli_books/field_guide/en_us/entries/") and n.endswith(".json"):
            s = z.read(n).decode("utf-8")
            if '"type":"patchouli:crafting"' in s or '"type": "patchouli:crafting"' in s:
                print(n)
                idx = s.find("patchouli:crafting")
                print(s[max(0, idx-300):idx+700])
                break
    else:
        print("no crafting page found")
