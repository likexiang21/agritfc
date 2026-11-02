from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfc"
bushes = ["blackberry", "blueberry", "bunchberry", "cloudberry", "cranberry",
          "elderberry", "gooseberry", "raspberry", "snowberry", "wintergreen"]
for bush in bushes:
    model = assets / "models/item/bush_waste" / (bush + ".json")
    model.parent.mkdir(parents=True, exist_ok=True)
    model.write_text(json.dumps({"parent": "minecraft:item/generated",
                                 "textures": {"layer0": "tfc:item/straw"}}, indent=2) + "\n", encoding="utf-8")
for lang, label in (("en_us", "Bush Waste ({})"), ("zh_cn", "浆果灌木废枝（{}）")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    for bush in bushes:
        d["item.tfcagricultureplus.bush_waste." + bush] = label.format(bush)
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

path = data / "tags/item/compost_greens/high.json"
path.parent.mkdir(parents=True, exist_ok=True)
payload = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"replace": False, "values": []}
values = list(payload.get("values", [])) + ["tfcagricultureplus:bush_waste/" + b for b in bushes]
path.write_text(json.dumps({"replace": False, "values": sorted(set(values))}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("bush waste", len(bushes))
