import json, pathlib
root=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/block/nut_leaves")
mapping={"cashew":"kapok","macadamia":"maple","pistachio":"willow"}
for sp,wood in mapping.items():
 p=root/(sp+".json")
 p.write_text(json.dumps({"parent":"minecraft:block/leaves","textures":{"all":f"tfc:block/wood/leaves/{wood}_fluff"}},indent=2)+"\n",encoding="utf-8")
 print(sp)
