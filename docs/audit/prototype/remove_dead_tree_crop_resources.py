from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
trees = ["pimento", "cinnamon", "clove", "nutmeg", "star_anise"]
removed = []
paths = []
for tree in trees:
    paths.extend([
        assets / "blockstates/spice_crop" / (tree + ".json"),
        assets / "models/block/spice_crop" / (tree + ".json"),
        assets / "models/item/spice_seed" / (tree + ".json"),
        data / "loot_table/blocks/spice_crop" / (tree + ".json"),
    ])
for p in paths:
    if p.is_file():
        p.unlink()
        removed.append(str(p.relative_to(root)))
# remove lang keys for dead crop/seed resources
for lang in ("en_us.json", "zh_cn.json"):
    p = assets / "lang" / lang
    d = json.loads(p.read_text(encoding="utf-8"))
    for tree in trees:
        d.pop("block.tfcagricultureplus.spice_crop." + tree, None)
        d.pop("item.tfcagricultureplus.spice_seed." + tree, None)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("removed", len(removed))
for r in removed:
    print(r)
