from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
nuts = ["acorn", "chestnut", "pine_nut", "hickory_nut", "pistachio", "cashew", "macadamia", "beechnut"]
for nut in nuts:
    model = assets / "models/item/ground_nut" / (nut + ".json")
    model.parent.mkdir(parents=True, exist_ok=True)
    model.write_text(json.dumps({"parent": "minecraft:item/generated",
                                 "textures": {"layer0": "tfc:item/straw"}}, indent=2) + "\n", encoding="utf-8")
    recipe = data / "recipe/mortar" / ("ground_" + nut + ".json")
    recipe.parent.mkdir(parents=True, exist_ok=True)
    recipe.write_text(json.dumps({
        "type": "tfcagricultureplus:mortar",
        "ingredient": {"item": "tfcagricultureplus:" + nut},
        "result": {"id": "tfcagricultureplus:ground_nut/" + nut, "count": 1},
        "grind_time": 4
    }, indent=2) + "\n", encoding="utf-8")
for lang, label in (("en_us", "Ground Nut ({})"), ("zh_cn", "坚果粉（{}）")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    for nut in nuts:
        d["item.tfcagricultureplus.ground_nut." + nut] = label.format(nut)
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("ground nuts", len(nuts))
