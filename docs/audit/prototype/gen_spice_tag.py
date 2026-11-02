import json
from pathlib import Path

lang = json.loads(Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang/zh_cn.json").read_text(encoding="utf-8"))
values = []
for k in lang:
    for prefix in ("item.tfcagricultureplus.spice.", "item.tfcagricultureplus.ground_spice."):
        if k.startswith(prefix):
            suffix = k[len("item.tfcagricultureplus."):]  # spice.basil
            folder, name = suffix.split(".", 1)
            values.append(f"tfcagricultureplus:{folder}/{name}")
values = sorted(set(values))
p = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/tags/item/spices.json")
p.write_text(json.dumps({"replace": False, "values": values}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("spices", len(values), values[:3])
