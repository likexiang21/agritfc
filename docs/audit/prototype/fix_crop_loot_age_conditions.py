from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/loot_table/blocks")
changed = []
for p in list((root / "spice_crop").glob("*.json")) + [root / "crop" / "strawberry.json"]:
    d = json.loads(p.read_text(encoding="utf-8"))
    if p.parent.name == "spice_crop":
        block_id = "tfcagricultureplus:spice_crop/" + p.stem
    else:
        block_id = "tfcagricultureplus:crop/strawberry"
    for pool in d.get("pools", []):
        if "conditions" not in pool:
            pool["conditions"] = [{
                "condition": "minecraft:block_state_property",
                "block": block_id,
                "properties": {"age": "7"},
            }]
    p.write_text(json.dumps(d, indent=2) + "\n", encoding="utf-8")
    changed.append(p.name)
print("patched", len(changed), "loot tables")
