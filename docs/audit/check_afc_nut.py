import json,pathlib
root=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets")
for ns in ("tfc","afc"):
 p=root/ns/"blockstates/wood/leaves"
 files=list(p.glob('*.json')) if p.exists() else []
 missing=[]
 for f in files:
  s=f.read_text(encoding='utf-8')
  if 'nut_state' not in s: missing.append(f.name)
 print(ns,len(files),'missing nut_state',len(missing),missing[:5])
