import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfc/patchouli_books/field_guide")
assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
item_models = {p.relative_to(assets / "models/item").with_suffix("").as_posix() for p in (assets / "models/item").rglob("*.json")}
blockstates = {p.relative_to(assets / "blockstates").with_suffix("").as_posix() for p in (assets / "blockstates").rglob("*.json")}
problems = []
for p in root.rglob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    icon = d.get("icon")
    if isinstance(icon, str) and icon.startswith("tfcagricultureplus:"):
        rid = icon.split(":", 1)[1]
        if rid not in item_models:
            problems.append((p.name, icon))
print("bad icons", len(problems))
for x in problems:
    print(x)
print("entries", len(list(root.glob("*/entries/**/*.json"))), "categories", len(list(root.glob("*/categories/*.json"))))
