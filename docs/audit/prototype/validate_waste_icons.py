import json
import zipfile
from pathlib import Path

mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
jars = {
    "tfc": mods / "TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar",
    "tfcfarmingplus": mods / "TFCFarmingPlus-NeoForge-1.21.1-0.1.0.jar",
}
assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
problems = []

for folder in ("crop_waste", "bush_waste"):
    for p in (assets / "models/item" / folder).glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        layer = d.get("textures", {}).get("layer0", "")
        if layer == "tfc:item/straw":
            problems.append(f"{folder}/{p.stem}: still straw")
            continue
        if ":" not in layer:
            problems.append(f"{folder}/{p.stem}: bad texture {layer}")
            continue
        ns, path = layer.split(":", 1)
        if ns not in jars:
            problems.append(f"{folder}/{p.stem}: unknown namespace {ns}")
            continue
        with zipfile.ZipFile(jars[ns]) as z:
            if f"assets/{ns}/textures/{path}.png" not in z.namelist():
                problems.append(f"{folder}/{p.stem}: missing texture {layer}")

print("crop_waste", len(list((assets / 'models/item/crop_waste').glob('*.json'))))
print("bush_waste", len(list((assets / 'models/item/bush_waste').glob('*.json'))))
print("problems", len(problems))
for p in problems[:20]:
    print("BAD", p)
if not problems:
    print("PASS: crop/bush waste icons")
