import json,pathlib
base=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/worldgen/placed_feature")
for p in base.glob("*.json"):
 d=json.loads(p.read_text(encoding="utf-8"))
 name=p.stem
 chance=60 if name.startswith("wild_mushroom_") else 120
 placement=d.setdefault("placement",[])
 if not any(x.get("type")=="minecraft:rarity_filter" for x in placement):
  placement.insert(0,{"type":"minecraft:rarity_filter","chance":chance})
 p.write_text(json.dumps(d,indent=2)+"\n",encoding="utf-8")
print("updated",len(list(base.glob('*.json'))))
