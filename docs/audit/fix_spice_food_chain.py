import json,pathlib,re
base=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources")
p=base/"data/tfcagricultureplus/tags/item/foods/ground_spices.json"
d=json.loads(p.read_text(encoding="utf-8"))
spices=[]
for f in (base/"assets/tfcagricultureplus/models/item/ground_spice").glob("*.json"):
 spices.append("tfcagricultureplus:ground_spice/"+f.stem)
for v in sorted(spices):
 if v not in d["values"]: d["values"].append(v)
p.write_text(json.dumps(d,indent=2)+"\n",encoding="utf-8")
print("ground_spices",len(d["values"]))
# extra mortar recipe for food/ground_black_pepper
r=base/"data/tfcagricultureplus/recipe/mortar/ground_black_pepper_food.json"
r.parent.mkdir(parents=True,exist_ok=True)
r.write_text(json.dumps({"type":"tfcagricultureplus:mortar","ingredient":{"item":"tfcagricultureplus:spice/black_pepper"},"result":{"id":"tfcagricultureplus:food/ground_black_pepper","count":1},"grind_time":4},indent=2)+"\n",encoding="utf-8")
print("recipe added")
