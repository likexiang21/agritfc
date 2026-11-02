import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
for name in ("en_us.json", "zh_cn.json"):
    p = base / name
    d = json.loads(p.read_text(encoding="utf-8"))
    for key in ("item.tfcagricultureplus.bowl.wood", "item.tfcagricultureplus.bowl.ceramic"):
        d.pop(key, None)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(name, len(d))
