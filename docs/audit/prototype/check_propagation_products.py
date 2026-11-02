import json
import zipfile
from pathlib import Path

mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
jars = {
    "tfc": "TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar",
    "tfcfarmingplus": "TFCFarmingPlus-NeoForge-1.21.1-0.1.0.jar",
    "tfcagricultureplus": "TFCAgriculturePlus-NeoForge-1.21.1-0.1.0.jar",
}
base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe/crafting/propagation_stock")
bad = []
for p in base.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    item = d["ingredients"][0]["item"]
    ns, path = item.split(":", 1)
    with zipfile.ZipFile(mods / jars[ns]) as z:
        candidates = [
            f"assets/{ns}/models/item/{path}.json",
            f"assets/{ns}/models/item/{path.replace('/', '_')}.json",
        ]
        if not any(c in z.namelist() for c in candidates):
            bad.append((p.name, item, candidates))
print("bad product models", len(bad))
for b in bad[:20]:
    print(b)
