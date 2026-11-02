from pathlib import Path
import json

assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
lang_dir = assets / "lang"

en = json.loads((lang_dir / "en_us.json").read_text(encoding="utf-8"))
zh = json.loads((lang_dir / "zh_cn.json").read_text(encoding="utf-8"))

names = {
    "crop/strawberry": ("Strawberry Crop", "草莓作物"),
    "serving_plate": ("Serving Plate", "餐盘"),
}
for key, value in en.items():
    if key.startswith("item.tfcagricultureplus.spice."):
        sid = key.rsplit(".", 1)[-1]
        names[f"spice_crop/{sid}"] = (f"{value} Crop", f"{zh.get(key, sid)}作物")
for sid in ("pistachio", "cashew", "macadamia"):
    sapling_en = en.get(f"item.tfcagricultureplus.nut_sapling/{sid}", f"{sid} Sapling")
    sapling_zh = zh.get(f"item.tfcagricultureplus.nut_sapling/{sid}", f"{sid}树苗")
    names[f"nut_sapling/{sid}"] = (sapling_en, sapling_zh)
    names[f"nut_leaves/{sid}"] = (sapling_en.replace(" Sapling", " Leaves"), sapling_zh.replace("树苗", "树叶"))

for fname, idx in (("en_us.json", 0), ("zh_cn.json", 1)):
    p = lang_dir / fname
    d = json.loads(p.read_text(encoding="utf-8"))
    for block, pair in names.items():
        d.setdefault("block.tfcagricultureplus." + block, pair[idx])
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("updated", fname, len(d))
