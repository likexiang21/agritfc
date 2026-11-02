import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
names = {
    "counter_cabinet": ("橱柜台面", "Counter Cabinet"),
    "half_cabinet": ("半高柜", "Half Cabinet"),
    "sink_cabinet": ("水槽柜", "Sink Cabinet"),
    "spice_rack": ("香料架", "Spice Rack"),
    "food_display": ("食品展示柜", "Food Display"),
    "fruit_bowl": ("果盘", "Fruit Bowl"),
}
for lang, idx in (("zh_cn.json", 0), ("en_us.json", 1)):
    p = base / lang
    d = json.loads(p.read_text(encoding="utf-8"))
    for kind, pair in names.items():
        d[f"block_entity.tfcagricultureplus.kitchen_storage.{kind}"] = pair[idx]
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lang, len(d))
