import pathlib
root=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources")
assets=root/"assets/tfcagricultureplus"
defs={p.stem for p in (root/"data/tfcagricultureplus/tfc/food").glob("*.json")}
# all item model paths that look like foods
foods=[]
for p in (assets/"models/item").rglob("*.json"):
 rel=str(p.relative_to(assets/"models/item").with_suffix("")).replace("\\","/")
 if rel.startswith("food/") or rel.startswith("ground_nut/") or rel.startswith("spice/") or rel.startswith("nut/"):
  foods.append(rel.split("/")[-1] if "/" in rel else rel)
for f in sorted(set(foods)):
 if f not in defs:
  print("NO_DEF", f)
print("defs",len(defs),"candidates",len(set(foods)))
