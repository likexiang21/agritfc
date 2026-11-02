import pathlib, json, collections
base=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe")
c=collections.Counter()
for p in base.rglob("*.json"):
 try: d=json.loads(p.read_text(encoding="utf-8"))
 except Exception: continue
 c[d.get("type","?")]+=1
for k,v in c.most_common(): print(v,k)
