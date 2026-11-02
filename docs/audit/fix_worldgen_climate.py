import json,pathlib
base=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/worldgen/placed_feature")
for p in base.glob("*.json"):
 d=json.loads(p.read_text(encoding="utf-8"))
 placement=d.setdefault("placement",[])
 if any(x.get("type")=="tfc:climate" for x in placement): continue
 if p.stem.startswith("wild_mushroom_"):
  climate={"type":"tfc:climate","min_temperature":-10,"max_temperature":35,"min_groundwater":100,"max_groundwater":500}
 else:
  climate={"type":"tfc:climate","min_temperature":-15,"max_temperature":40,"min_groundwater":80,"max_groundwater":500}
 idx=next((i for i,x in enumerate(placement) if x.get("type")=="minecraft:rarity_filter"),0)+1
 placement.insert(idx,climate)
 p.write_text(json.dumps(d,indent=2)+"\n",encoding="utf-8")
print("climate added")
