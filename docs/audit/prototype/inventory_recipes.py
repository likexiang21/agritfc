import pathlib, json, re
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus")
recipes = []
for p in (base / "recipe").rglob("*.json"):
    try: d=json.loads(p.read_text(encoding="utf-8"))
    except Exception: continue
    out = d.get("result") or d.get("result_item") or d.get("output")
    rid = None
    if isinstance(out, dict):
        rid = out.get("id") or out.get("item")
    if rid is None:
        # try all string values containing our namespace
        s = p.read_text(encoding="utf-8")
        m = re.findall(r'"tfcagricultureplus:([^"]+)"', s)
        if m: rid = "tfcagricultureplus:" + m[0]
    recipes.append((p.name, rid, p.relative_to(base)))
# collect item ids from item models
items = set()
for p in pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/item").rglob("*.json"):
    rel = p.relative_to(pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/item"))
    items.add(str(rel.with_suffix("")).replace("\\", "/"))
# categories of interest
for prefix in ("food/", "food", "spice/", "nut/", "nut_shell/", "crop_waste/", "ground_nut/", "ground_spice/", "wet_grass", "seed", "seedling", "spice_corm/", "spice_root/", "spice_seed/"):
    pass
print("items", len(items))
print("recipes", len(recipes))
# show recipes whose output is food/spice/nut
for name, rid, rel in recipes:
    if rid and any(x in rid for x in ("food", "spice", "nut", "seed", "wet_grass", "crop_waste")):
        print(rid, "|", rel)
