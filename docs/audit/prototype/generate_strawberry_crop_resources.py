from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
bs = assets / "blockstates/crop/strawberry.json"
bs.parent.mkdir(parents=True, exist_ok=True)
bs.write_text(json.dumps({"variants": {f"age={a}": {"model": "tfcagricultureplus:block/crop/strawberry"}
                                      for a in range(8)}}, indent=2) + "\n", encoding="utf-8")
model = assets / "models/block/crop/strawberry.json"
model.parent.mkdir(parents=True, exist_ok=True)
model.write_text(json.dumps({"parent": "minecraft:block/crop",
                             "textures": {"crop": "tfc:block/crop/strawberry_5"}}, indent=2) + "\n", encoding="utf-8")
seed_model = assets / "models/item/seeds/strawberry.json"
seed_model.parent.mkdir(parents=True, exist_ok=True)
seed_model.write_text(json.dumps({"parent": "minecraft:item/generated",
                                 "textures": {"layer0": "tfc:item/seeds/strawberry"}}, indent=2) + "\n", encoding="utf-8")
loot = data / "loot_table/blocks/crop/strawberry.json"
loot.parent.mkdir(parents=True, exist_ok=True)
loot.write_text(json.dumps({"type": "minecraft:block", "pools": [
    {"rolls": 1, "entries": [{"type": "minecraft:item", "name": "tfc:food/strawberry"}]},
    {"rolls": 1, "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:seeds/strawberry"}]}
]}, indent=2) + "\n", encoding="utf-8")
for lang, block_label, seed_label in (("en_us", "Strawberry Crop", "Strawberry Seeds"),
                                      ("zh_cn", "草莓作物", "草莓种子")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    d["block.tfcagricultureplus.crop/strawberry"] = block_label
    d["item.tfcagricultureplus.seeds/strawberry"] = seed_label
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("strawberry crop resources written")
