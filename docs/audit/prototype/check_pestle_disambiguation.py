from pathlib import Path
import json

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe/knapping")
rows = []
for p in base.rglob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("type") != "tfc:knapping":
        continue
    if "pestle" not in json.dumps(d):
        continue
    rows.append((p.name, d.get("knapping_type"), tuple(d.get("pattern", [])), d.get("ingredient")))

unique = {(r[1], r[2], json.dumps(r[3], sort_keys=True)) for r in rows}
print("pestle recipes", len(rows), "unique knapping_type+pattern+ingredient", len(unique))
for r in rows:
    print(r[0], "ingredient=", r[3])
