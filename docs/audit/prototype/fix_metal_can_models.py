import json
from pathlib import Path

models = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/item/metal_can")
metals = [p.stem for p in models.glob("*.json")]
for p in models.glob("*.json"):
    metal = p.stem
    data = {
        "loader": "tfc:fluid_container",
        "parent": "neoforge:item/default",
        "textures": {
            "base": f"tfc:item/metal/sheet/{metal}",
            "fluid": "tfc:item/metal/bucket/overlay",
        },
    }
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

lang_dir = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
for lang, template in (("zh_cn.json", "装有%s的金属罐"), ("en_us.json", "%s Metal Can")):
    p = lang_dir / lang
    d = json.loads(p.read_text(encoding="utf-8"))
    for metal in metals:
        d[f"item.tfcagricultureplus.metal_can.{metal}.filled"] = template
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lang, "keys", len(d))
print("models", len(metals))
