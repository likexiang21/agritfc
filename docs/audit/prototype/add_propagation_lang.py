import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
methods = {
    "seed_direct": ("种子直播", "Direct sowing"),
    "nursery": ("育苗移栽", "Nursery transplant"),
    "runner": ("匍匐茎分株", "Runner division"),
    "tuber": ("种薯/块茎", "Seed tuber"),
    "rhizome": ("根茎分株", "Rhizome division"),
    "corm": ("种球/球茎", "Seed corm"),
    "crown": ("冠芽/分株", "Crown division"),
    "division": ("分株", "Division"),
}
for lang, idx, msg in (
    ("zh_cn.json", 0, "%s繁殖：不能直接播种"),
    ("en_us.json", 1, "%s propagation: direct sowing is not allowed"),
):
    p = base / lang
    d = json.loads(p.read_text(encoding="utf-8"))
    d["message.tfcagricultureplus.planting.method"] = msg
    for key, pair in methods.items():
        d[f"method.tfcagricultureplus.{key}"] = pair[idx]
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lang, len(d))
