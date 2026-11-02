import json, re
from pathlib import Path
lang = json.loads(Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang/zh_cn.json").read_text(encoding="utf-8"))
bad = []
for k, v in lang.items():
    if isinstance(v, str) and re.search(r"[A-Za-z_]", v) and (k.startswith("item.") or k.startswith("block.")):
        bad.append(f"{k} = {v}")
Path("mod_rebuild/docs/audit/prototype/ascii_names.txt").write_text("\n".join(bad), encoding="utf-8")
print("count", len(bad))
