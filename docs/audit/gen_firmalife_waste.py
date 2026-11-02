import json
import pathlib

names = [
    "cocoa_branch", "cocoa_growing_branch", "cocoa_leaves", "cocoa_sapling",
    "fig_branch", "fig_growing_branch", "fig_leaves", "fig_sapling",
    "nightshade_bush", "pineapple_bush", "wild_red_grapes", "wild_white_grapes",
    "grape_string_red", "grape_string_white",
]

root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources")
models = root / "assets/tfcagricultureplus/models/item/crop_waste"
models.mkdir(parents=True, exist_ok=True)
for name in names:
    p = models / (name + ".json")
    p.write_text(json.dumps({
        "parent": "minecraft:item/generated",
        "textures": {"layer0": "tfc:item/straw"},
    }, indent=2) + "\n", encoding="utf-8")

en = root / "assets/tfcagricultureplus/lang/en_us.json"
zh = root / "assets/tfcagricultureplus/lang/zh_cn.json"
en_data = json.loads(en.read_text(encoding="utf-8"))
zh_data = json.loads(zh.read_text(encoding="utf-8"))
for name in names:
    label = " ".join(part.capitalize() for part in name.split("_"))
    en_data["item.tfcagricultureplus.crop_waste." + name] = label + " Waste"
    zh_data["item.tfcagricultureplus.crop_waste." + name] = label + " 废枝叶"
for path, data in ((en, en_data), (zh, zh_data)):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

compost = root / "data/tfc/tags/item/compost_greens/medium.json"
data = json.loads(compost.read_text(encoding="utf-8"))
for name in names:
    item = "tfcagricultureplus:crop_waste/" + name
    if item not in data["values"]:
        data["values"].append(item)
compost.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("generated", len(names), "firmalife crop waste items")
