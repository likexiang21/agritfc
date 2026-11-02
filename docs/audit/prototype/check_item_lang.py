from pathlib import Path
import json

assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
lang = json.loads((assets / "lang/en_us.json").read_text(encoding="utf-8"))
models = {p.relative_to(assets / "models/item").with_suffix("").as_posix() for p in (assets / "models/item").rglob("*.json")}
blocks = {p.relative_to(assets / "blockstates").with_suffix("").as_posix() for p in (assets / "blockstates").rglob("*.json")}
missing = []
for item in sorted(models):
    if item in blocks:
        keys = ["block.tfcagricultureplus." + item]
    else:
        keys = ["item.tfcagricultureplus." + item, "item.tfcagricultureplus." + item.replace("/", ".")]
    if not any(k in lang for k in keys):
        missing.append(item)
print("item models", len(models), "blockstates", len(blocks), "missing item/block lang", len(missing))
for x in missing[:60]:
    print(x)
