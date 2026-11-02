import pathlib,json
root=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets")
for ns in ("tfc","afc"):
 p=root/ns/"blockstates/wood/leaves"
 print(ns, p.exists(), len(list(p.glob('*.json'))) if p.exists() else 0)
 if p.exists():
  for f in list(p.glob('*.json'))[:2]:
   print(f.name, list(json.loads(f.read_text(encoding='utf-8')).keys()))
