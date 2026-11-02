import zipfile, json
from pathlib import Path

p = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\TFCFarmingPlus-NeoForge-1.21.1-0.1.0.jar")
out = {}
for lang in ("en_us", "zh_cn"):
    with zipfile.ZipFile(p) as z:
        d = json.loads(z.read(f"assets/tfcfarmingplus/lang/{lang}.json").decode("utf-8"))
    part = {}
    for k, v in d.items():
        if k.startswith("item.tfcfarmingplus.food."):
            part[k.rsplit(".", 1)[1]] = v
    out[lang] = part
Path("mod_rebuild/docs/audit/prototype/a_food_names_bilingual.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("en", len(out["en_us"]), "zh", len(out["zh_cn"]))
