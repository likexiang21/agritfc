import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfc/patchouli_books/field_guide")
assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
item_models = {p.relative_to(assets / "models/item").with_suffix("").as_posix() for p in (assets / "models/item").rglob("*.json")}
blockstates = {p.relative_to(assets / "blockstates").with_suffix("").as_posix() for p in (assets / "blockstates").rglob("*.json")}
problems = []
for p in root.rglob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    for page in d.get("pages", []):
        if page.get("type") == "patchouli:spotlight":
            item = page.get("item", "")
            if item.startswith("tfcagricultureplus:"):
                rid = item.split(":", 1)[1]
                if rid not in item_models and rid not in blockstates:
                    problems.append((p.name, item))
print("bad spotlight items", len(problems))
for x in problems:
    print(x)
