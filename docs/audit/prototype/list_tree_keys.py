import json
from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang/zh_cn.json")
d = json.loads(p.read_text(encoding="utf-8"))
out = []
for k, v in d.items():
    if any(x in k for x in ("nut", "spice_sapling", "spice_leaves", "spice_crop", "nut_leaves")):
        out.append(f"{k} = {v}")
Path("mod_rebuild/docs/audit/prototype/tree_keys.txt").write_text("\n".join(out), encoding="utf-8")
print(len(out))
