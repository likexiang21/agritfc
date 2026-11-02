import json, pathlib
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
for name in ("en_us.json", "zh_cn.json"):
    p = base / name
    data = json.loads(p.read_text(encoding="utf-8"))
    out = {}
    for key, value in data.items():
        new_key = key.replace("/", ".")
        if new_key in out and out[new_key] != value:
            raise SystemExit("collision " + new_key)
        out[new_key] = value
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(name, len(out), "slash keys left", sum(1 for k in out if "/" in k))
