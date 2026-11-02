from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/worldgen/placed_feature")
changed = []
for p in root.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    touched = False
    feature = d.get("feature", "")
    sapling = None
    if feature.startswith("tfcagricultureplus:nut_sapling_"):
        sapling = "tfcagricultureplus:nut_sapling/" + feature.rsplit("_", 1)[-1]
    elif feature.startswith("tfcagricultureplus:spice_sapling_"):
        sapling = "tfcagricultureplus:spice_sapling/" + feature.rsplit("_", 1)[-1]
    for placement in d.get("placement", []):
        if placement.get("type") == "minecraft:count":
            c = placement.get("count")
            if isinstance(c, dict) and c.get("type") == "minecraft:uniform":
                lo = c.get("min_inclusive", c.get("value", {}).get("min_inclusive", c.get("min")))
                hi = c.get("max_inclusive", c.get("value", {}).get("max_inclusive", c.get("max")))
                placement["count"] = {
                    "type": "minecraft:uniform",
                    "min_inclusive": lo,
                    "max_inclusive": hi,
                }
                touched = True
        if placement.get("type") == "minecraft:block_predicate_filter":
            pred = placement.get("predicate")
            if isinstance(pred, dict) and pred.get("type") == "minecraft:would_survive" and "state" not in pred:
                if sapling is not None:
                    pred["state"] = {"Name": sapling, "Properties": {"stage": "0"}}
                else:
                    placement.pop("predicate", None)
                touched = True
    if touched:
        p.write_text(json.dumps(d, indent=2) + "\n", encoding="utf-8")
        changed.append(p.name)
print("fixed", len(changed))
