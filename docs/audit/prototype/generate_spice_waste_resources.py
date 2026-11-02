from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfc"
species = ["basil", "bay_laurel", "cardamom", "cilantro", "cumin", "oregano", "pimento", "vanilla",
           "black_pepper", "cinnamon", "clove", "nutmeg", "saffron", "star_anise", "rosemary",
           "thyme", "sage", "dill", "fennel", "mustard"]
herbs = {"basil", "cilantro", "cumin", "oregano", "dill", "fennel", "mustard", "thyme", "sage"}
for spice in species:
    model = assets / "models/item/spice_waste" / (spice + ".json")
    model.parent.mkdir(parents=True, exist_ok=True)
    model.write_text(json.dumps({"parent": "minecraft:item/generated",
                                 "textures": {"layer0": "tfc:item/straw"}}, indent=2) + "\n", encoding="utf-8")
for lang, label in (("en_us", "Spice Waste ({})"), ("zh_cn", "香料废枝叶（{}）")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    for spice in species:
        d["item.tfcagricultureplus.spice_waste." + spice] = label.format(spice)
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

by_tag = {"high": [], "medium": []}
for spice in species:
    by_tag["high" if spice in herbs else "medium"].append("tfcagricultureplus:spice_waste/" + spice)
for level, values in by_tag.items():
    path = data / "tags/item/compost_greens" / (level + ".json")
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if path.exists():
        payload = json.loads(path.read_text(encoding="utf-8"))
        existing = [v for v in payload.get("values", []) if isinstance(v, str)]
    merged = sorted(set(existing + values))
    path.write_text(json.dumps({"replace": False, "values": merged}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("spice waste items", len(species), "tag counts", {k: len(v) for k, v in by_tag.items()})
