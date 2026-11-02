import json
import pathlib
import re
import zipfile

root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources")
jar = pathlib.Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar")

# Parse docs mapping (crop -> high/medium/low)
doc = pathlib.Path(r"mod_rebuild/docs/291-crop-system-complete-modification-20261028.md").read_text(encoding="utf-8")
mapping = {}
for line in doc.splitlines():
    m = re.search(r"\|\s*`([a-z0-9_]+)`\s*\|[^\n]*?`tfc:compost_greens/(high|medium|low)`", line)
    if m:
        mapping[m.group(1)] = m.group(2)

greens = {"high": [], "medium": [], "low": []}
for crop, cat in mapping.items():
    greens[cat].append("tfcagricultureplus:crop_waste/" + crop)
greens["high"].append("tfcagricultureplus:wet_grass")

bushes = ["blackberry", "blueberry", "bunchberry", "cloudberry", "cranberry",
          "elderberry", "gooseberry", "raspberry", "snowberry", "wintergreen"]
for bush in bushes:
    greens["medium"].append("tfcagricultureplus:bush_waste/" + bush)

browns = {"high": [], "medium": [], "low": []}
shells = ["acorn", "beechnut", "cashew", "chestnut", "hickory_nut", "macadamia", "pine_nut", "pistachio"]
for shell in shells:
    browns["high"].append("tfcagricultureplus:nut_shell/" + shell)

with zipfile.ZipFile(jar) as z:
    for group, values in (("compost_greens", greens), ("compost_browns", browns)):
        for cat, extra in values.items():
            src = f"data/tfc/tags/item/{group}/{cat}.json"
            data = json.loads(z.read(src).decode("utf-8"))
            existing = data.get("values", [])
            merged = list(existing)
            for item in extra:
                if item not in merged:
                    merged.append(item)
            data["values"] = merged
            out = root / "data/tfc/tags/item" / group / (cat + ".json")
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(out.relative_to(root), "values", len(merged), "added", len(extra))
