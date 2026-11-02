import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
m = json.loads(Path("mod_rebuild/docs/audit/prototype/agriculture_name_map.json").read_text(encoding="utf-8"))
for lang, key in (("zh_cn.json", "zh"), ("en_us.json", "en")):
    p = base / lang
    d = json.loads(p.read_text(encoding="utf-8"))
    changed = 0
    for k, v in m[key].items():
        if k in d:
            d[k] = v
            changed += 1
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lang, "changed", changed, "keys", len(d))
