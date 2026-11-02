import json
import zipfile
from pathlib import Path

mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
jars = {
    "tfc": "TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar",
    "tfcfarmingplus": "TFCFarmingPlus-NeoForge-1.21.1-0.1.0.jar",
    "tfcagricultureplus": "TFCAgriculturePlus-NeoForge-1.21.1-0.1.0.jar",
}
# Parse the Java registry data from PropagationStock.java.
src = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop/PropagationStock.java").read_text(encoding="utf-8")
rows = []
for line in src.splitlines():
    if 'c("' in line:
        import re
        m = re.search(r'c\("([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\)', line)
        if m:
            rows.append(m.groups())
bad = []
for species, crop, product in rows:
    ns, path = crop.split(":", 1)
    with zipfile.ZipFile(mods / jars[ns]) as z:
        candidates = [
            f"assets/{ns}/blockstates/{path}.json",
            f"data/{ns}/loot_table/blocks/{path}.json",
        ]
        if not any(c in z.namelist() for c in candidates):
            bad.append((species, crop, candidates))
print("rows", len(rows), "bad crop refs", len(bad))
for b in bad[:20]:
    print(b)
