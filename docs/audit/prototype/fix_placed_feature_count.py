from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/worldgen/placed_feature")
changed = []
for p in root.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    touched = False
    for placement in d.get("placement", []):
        if placement.get("type") != "minecraft:count":
            continue
        c = placement.get("count")
        if isinstance(c, dict) and c.get("type") == "minecraft:uniform" and "min" in c and "max" in c:
            placement["count"] = {
                "type": "minecraft:uniform",
                "value": {"min_inclusive": c["min"], "max_inclusive": c["max"]},
            }
            touched = True
    if touched:
        p.write_text(json.dumps(d, indent=2) + "\n", encoding="utf-8")
        changed.append(p.name)
print("fixed", len(changed))
for c in changed:
    print(c)
