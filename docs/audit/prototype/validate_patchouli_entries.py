import json
import re
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfc/patchouli_books/field_guide"
data = root / "data/tfcagricultureplus/recipe"
item_models = {p.relative_to(root / "assets/tfcagricultureplus/models/item").with_suffix("").as_posix()
               for p in (root / "assets/tfcagricultureplus/models/item").rglob("*.json")}
blockstates = {p.relative_to(root / "assets/tfcagricultureplus/blockstates").with_suffix("").as_posix()
               for p in (root / "assets/tfcagricultureplus/blockstates").rglob("*.json")}
recipe_ids = {p.relative_to(data).with_suffix("").as_posix() for p in data.rglob("*.json")}

problems = []
for lang in ("en_us", "zh_cn"):
    entries = list((assets / lang / "entries").rglob("*.json"))
    categories = {p.stem for p in (assets / lang / "categories").glob("*.json")}
    if len(entries) != 10:
        problems.append(f"{lang}: expected 10 entries, got {len(entries)}")
    for p in entries:
        d = json.loads(p.read_text(encoding="utf-8"))
        if d.get("category", "").split(":")[-1] not in categories:
            problems.append(f"{lang}/{p.name}: missing category {d.get('category')}")
        if not d.get("pages"):
            problems.append(f"{lang}/{p.name}: no pages")
        for page in d["pages"]:
            t = page.get("type")
            if t == "patchouli:spotlight":
                item = page.get("item", "")
                if item.startswith("tfcagricultureplus:"):
                    rid = item.split(":", 1)[1]
                    if rid not in item_models and rid not in blockstates:
                        problems.append(f"{lang}/{p.name}: bad spotlight {item}")
            if t == "patchouli:crafting":
                recipe = page.get("recipe", "")
                if recipe.startswith("tfcagricultureplus:"):
                    rid = recipe.split(":", 1)[1]
                    if rid not in recipe_ids:
                        problems.append(f"{lang}/{p.name}: bad recipe {recipe}")
    # parity by relative path and page count
    for p in entries:
        other = assets / ("zh_cn" if lang == "en_us" else "en_us") / p.relative_to(assets / lang)
        if not other.exists():
            problems.append(f"parity missing {other}")
        else:
            if len(json.loads(p.read_text(encoding="utf-8")).get("pages", [])) != len(json.loads(other.read_text(encoding="utf-8")).get("pages", [])):
                problems.append(f"parity page count {p.relative_to(assets)}")

print("entries", len(list((assets / 'en_us/entries').rglob('*.json'))),
      "categories", len(list((assets / 'en_us/categories').glob('*.json'))))
print("problems", len(problems))
for p in problems:
    print("BAD", p)
if not problems:
    print("PASS: patchouli entries")
