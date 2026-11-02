from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
species = ["basil", "bay_laurel", "cardamom", "cilantro", "cumin", "oregano", "pimento", "vanilla",
           "black_pepper", "cinnamon", "clove", "nutmeg", "saffron", "star_anise", "rosemary",
           "thyme", "sage", "dill", "fennel", "mustard"]
for spice in species:
    model = assets / "models/item/ground_spice" / (spice + ".json")
    model.parent.mkdir(parents=True, exist_ok=True)
    model.write_text(json.dumps({"parent": "minecraft:item/generated",
                                 "textures": {"layer0": "tfc:item/straw"}}, indent=2) + "\n", encoding="utf-8")
    recipe = data / "recipe/mortar" / ("ground_" + spice + ".json")
    recipe.parent.mkdir(parents=True, exist_ok=True)
    recipe.write_text(json.dumps({
        "type": "tfcagricultureplus:mortar",
        "ingredient": {"item": "tfcagricultureplus:spice/" + spice},
        "result": {"id": "tfcagricultureplus:ground_spice/" + spice, "count": 1},
        "grind_time": 4
    }, indent=2) + "\n", encoding="utf-8")
for lang, label in (("en_us", "Ground Spice ({})"), ("zh_cn", "香料粉（{}）")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    for spice in species:
        d["item.tfcagricultureplus.ground_spice." + spice] = label.format(spice)
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("ground spices", len(species))
