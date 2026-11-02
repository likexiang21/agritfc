import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/block")

# Shared drying rack: four legs + top frame + slats, height 12 (matches the 0.75 block shape).
elements = []
def box(fr, to, tex="#wood"):
    return {"from": list(fr), "to": list(to), "faces": {d: {"texture": tex} for d in ("north","south","east","west","up","down")}}

for x, z in ((1,1),(14,1),(1,14),(14,14)):
    elements.append(box((x,0,z),(x+1,12,z+1)))
# top frame
elements += [
    box((1,11,1),(15,12,2)),
    box((1,11,14),(15,12,15)),
    box((1,11,2),(2,12,14)),
    box((14,11,2),(15,12,14)),
]
# slats along z at several x positions
for x in (3, 5, 7, 9, 11, 13):
    elements.append(box((x,11,3),(x+1,11.5,13)))

shared = {"textures": {"particle": "#wood"}, "elements": elements}
(base / "drying_rack.json").write_text(json.dumps(shared, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

tfc = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow"]
afc = ["araucaria","baobab","beech","cypress","eucalyptus","fig","ginkgo","hevea","ipe","ironwood","mahoe","mahogany","teak","tualang"]
for w in tfc:
    p = base / "drying_rack" / f"{w}.json"
    p.write_text(json.dumps({"parent":"tfcagricultureplus:block/drying_rack","textures":{"wood":f"tfc:block/wood/planks/{w}"}}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
for w in afc:
    p = base / "drying_rack" / f"{w}.json"
    p.write_text(json.dumps({"parent":"tfcagricultureplus:block/drying_rack","textures":{"wood":f"afc:block/wood/planks/{w}"}}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print("drying rack models rewritten")
