from pathlib import Path
import json
import re

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"

problems = []
blockstates = {}
for p in (assets / "blockstates").rglob("*.json"):
    rel = p.relative_to(assets / "blockstates").with_suffix("").as_posix()
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        problems.append(f"blockstate json {rel}: {e}")
        continue
    blockstates[rel] = d

models = {p.relative_to(assets / "models").with_suffix("").as_posix() for p in (assets / "models").rglob("*.json")}
textures = {p.relative_to(assets / "textures").with_suffix("").as_posix() for p in (assets / "textures").rglob("*.png")}

def check_model_ref(ref, where):
    if ref.startswith("tfcagricultureplus:"):
        rel = ref.split(":", 1)[1]
        if rel not in models:
            problems.append(f"missing local model {ref} used by {where}")

def walk(obj, where):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("model", "parent") and isinstance(v, str):
                check_model_ref(v, where)
            walk(v, where)
    elif isinstance(obj, list):
        for v in obj:
            walk(v, where)

for rel, d in blockstates.items():
    walk(d, f"blockstate {rel}")

# every blockstate block id must have a lang key (blocks with states)
lang = json.loads((assets / "lang/en_us.json").read_text(encoding="utf-8"))
missing_lang = []
for rel in blockstates:
    bid = "block.tfcagricultureplus:" + rel.replace("/", ".")
    # vanilla lang uses block.namespace.path (dots), but our generated keys often block.tfcagricultureplus.path
    if bid not in lang and ("block.tfcagricultureplus." + rel.replace("/", ".")) not in lang:
        missing_lang.append(rel)

print("blockstates", len(blockstates))
print("models", len(models), "textures", len(textures))
print("problems", len(problems))
for x in problems[:40]:
    print("PROBLEM", x)
print("missing block lang", len(missing_lang))
for x in missing_lang[:20]:
    print("MISSING_LANG", x)

# recipes: all B ingredient/result refs exist as item model or blockstate
items = {p.relative_to(assets / "models/item").with_suffix("").as_posix() for p in (assets / "models/item").rglob("*.json")}
badrefs = []
for p in (data / "recipe").rglob("*.json"):
    text = p.read_text(encoding="utf-8")
    if "tfcagricultureplus:" not in text:
        continue
    for ref in re.findall(r'"tfcagricultureplus:([^"]+)"', text):
        if ref.startswith("recipe/") or ref.startswith("item/") or ref.startswith("block/"):
            continue
        if ref in items or ref in blockstates or ref.split("/")[-1] in {x.split("/")[-1] for x in items}:
            continue
        badrefs.append((p.relative_to(data).as_posix(), ref))
print("recipe B refs not obviously local", len(badrefs))
for x in badrefs[:20]:
    print("RECIPE_REF", x)
