import pathlib, json, re

root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data"
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/java")

# all recipe outputs and inputs (rough: every item id string in each recipe file classified)
recipes = []
for p in (data / "tfcagricultureplus/recipe").rglob("*.json"):
    s = p.read_text(encoding="utf-8", errors="ignore")
    ids = set(re.findall(r'tfcagricultureplus:[a-zA-Z0-9_/]+', s))
    recipes.append((p, ids))

# item models
items = set()
for p in (assets / "models/item").rglob("*.json"):
    rel = p.relative_to(assets / "models/item").with_suffix("")
    items.add("tfcagricultureplus:" + str(rel).replace("\\", "/"))

out_count = {i: 0 for i in items}
in_count = {i: 0 for i in items}
for p, ids in recipes:
    # classify by known result paths
    for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        for i in ids:
            if i in line:
                if '"result"' in line or '"id"' in line:
                    pass
    # approximate: if recipe file has result block; use json
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        continue
    result = d.get("result") or d.get("result_item") or d.get("output")
    rid = None
    if isinstance(result, dict):
        rid = result.get("id") or result.get("item")
    if rid in out_count:
        out_count[rid] += 1
    # all ids in ingredients / inputs
    text = json.dumps(d)
    for i in items:
        if i in text and i != rid:
            in_count[i] += 1

print("Items with no recipe output and no non-recipe source? showing food/spice/nut/seed:")
for i in sorted(items):
    if any(x in i for x in ("food/", "spice/", "nut/", "nut_shell/", "wet_grass", "seed", "seedling", "crop_waste/", "ground_")):
        if out_count[i] == 0:
            print("NO_OUTPUT", i, "inputs", in_count[i])
print("--- items never used in any recipe input/output ---")
for i in sorted(items):
    if out_count[i] == 0 and in_count[i] == 0:
        print(i)
