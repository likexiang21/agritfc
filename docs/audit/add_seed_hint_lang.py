import json
from pathlib import Path
base = Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
for name, value in (("en_us.json", "This seed must be raised in a nursery tray before transplanting."), ("zh_cn.json", "该种子需先在育苗盘育苗后移栽。")):
    p = base / name
    t = p.read_text(encoding="utf-8")
    assert '"message.tfcagricultureplus.seed_requires_nursery"' not in t
    idx = t.rfind("}")
    t = t[:idx].rstrip()
    t += ',\n  "message.tfcagricultureplus.seed_requires_nursery": ' + json.dumps(value, ensure_ascii=False) + '\n}\n'
    p.write_text(t, encoding="utf-8")
    print(name, "updated")
