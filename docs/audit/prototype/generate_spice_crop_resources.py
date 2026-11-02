from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
species = ["basil", "bay_laurel", "cardamom", "cilantro", "cumin", "oregano", "pimento", "vanilla",
           "black_pepper", "cinnamon", "clove", "nutmeg", "saffron", "star_anise", "rosemary",
           "thyme", "sage", "dill", "fennel", "mustard"]
for spice in species:
    crop_path = "spice_crop/" + spice
    bs = assets / "blockstates" / (crop_path + ".json")
    bs.parent.mkdir(parents=True, exist_ok=True)
    bs.write_text(json.dumps({"variants": {f"age={a}": {"model": "tfcagricultureplus:block/" + crop_path}
                                           for a in range(8)}}, indent=2) + "\n", encoding="utf-8")
    model = assets / "models/block" / (crop_path + ".json")
    model.parent.mkdir(parents=True, exist_ok=True)
    model.write_text(json.dumps({"parent": "minecraft:block/cross",
                                 "textures": {"cross": "tfc:block/crop/wheat_7"}}, indent=2) + "\n", encoding="utf-8")
    for item in ("spice_seed/" + spice, "spice/" + spice):
        item_model = assets / "models/item" / (item + ".json")
        item_model.parent.mkdir(parents=True, exist_ok=True)
        item_model.write_text(json.dumps({"parent": "minecraft:item/generated",
                                          "textures": {"layer0": "tfc:item/straw"}}, indent=2) + "\n", encoding="utf-8")
    loot = data / "loot_table/blocks" / (crop_path + ".json")
    loot.parent.mkdir(parents=True, exist_ok=True)
    loot.write_text(json.dumps({"type": "minecraft:block", "pools": [
        {"rolls": 1, "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:spice/" + spice}]},
        {"rolls": 1, "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:spice_seed/" + spice}]}
    ]}, indent=2) + "\n", encoding="utf-8")

for lang, seed_label, product_label in (
    ("en_us", "Spice Seed ({})", "Spice ({})"),
    ("zh_cn", "香料种子（{}）", "香料（{}）"),
):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    for spice in species:
        d["item.tfcagricultureplus.spice_seed." + spice] = seed_label.format(spice)
        d["item.tfcagricultureplus.spice." + spice] = product_label.format(spice)
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("spice crops", len(species))
