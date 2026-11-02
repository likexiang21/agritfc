from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
# Only saffron currently uses form=corm.
spice = "saffron"
model = assets / "models/item/spice_corm" / (spice + ".json")
model.parent.mkdir(parents=True, exist_ok=True)
model.write_text(json.dumps({"parent": "minecraft:item/generated",
                             "textures": {"layer0": "tfc:item/straw"}}, indent=2) + "\n", encoding="utf-8")
for lang, label in (("en_us", "Saffron Corm"), ("zh_cn", "藏红花球茎")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    d["item.tfcagricultureplus.spice_corm." + spice] = label
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("corm resources written")
