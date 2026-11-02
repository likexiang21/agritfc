import pathlib,json
for p in pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/item/crop_waste").glob("*.json"):
 d=json.loads(p.read_text(encoding="utf-8"))
 tex=d.get("textures",{}).get("layer0","")
 if "tfc:item/straw" in tex or "tfc:item" in tex:
  print(p.name, tex); break
