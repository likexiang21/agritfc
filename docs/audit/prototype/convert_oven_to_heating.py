import json
from pathlib import Path

src = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe/oven")
dst = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe/heating")
dst.mkdir(parents=True, exist_ok=True)
files = list(src.glob("*.json"))
for p in files:
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("type") != "firmalife:oven":
        continue
    out = {
        "type": "tfc:heating",
        "ingredient": d["ingredient"],
        "result_item": d["result"],
        "temperature": d.get("temperature", 400.0),
    }
    (dst / p.name).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    p.unlink()
print("converted", len(files), "oven recipes to tfc:heating")
try:
    src.rmdir()
except OSError:
    pass
