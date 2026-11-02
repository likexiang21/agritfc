from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfc"
nuts = ["acorn", "chestnut", "pine_nut", "hickory_nut", "pistachio", "cashew", "macadamia", "beechnut"]
for nut in nuts:
    model = assets / "models/item/nut_shell" / (nut + ".json")
    model.parent.mkdir(parents=True, exist_ok=True)
    model.write_text(json.dumps({"parent": "minecraft:item/generated",
                                 "textures": {"layer0": "tfc:item/straw"}}, indent=2) + "\n", encoding="utf-8")
for lang, label in (("en_us", "Nut Shell ({})"), ("zh_cn", "坚果壳（{}）")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    for nut in nuts:
        d["item.tfcagricultureplus.nut_shell." + nut] = label.format(nut)
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

path = data / "tags/item/compost_browns/high.json"
path.parent.mkdir(parents=True, exist_ok=True)
payload = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"replace": False, "values": []}
values = list(payload.get("values", [])) + ["tfcagricultureplus:nut_shell/" + n for n in nuts]
path.write_text(json.dumps({"replace": False, "values": sorted(set(values))}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("nut shells", len(nuts))
