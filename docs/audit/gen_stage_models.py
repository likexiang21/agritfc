import json, pathlib, copy
root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
bag = json.loads((root / "models/block/mushroom_bag.json").read_text(encoding="utf-8"))
bag.setdefault("textures", {})["cap"] = "minecraft:block/brown_mushroom_block"
bag.setdefault("textures", {})["stem"] = "minecraft:block/mushroom_stem"

def cube(frm, to, tex):
    return {"from": frm, "to": to, "faces": {d: {"texture": tex} for d in ("down","up","north","south","west","east")}}

for stage, elems in {
    1: [cube([5,10,5],[11,12,11],"#cap"), cube([6.5,9,6.5],[9.5,10,9.5],"#stem")],
    2: [cube([4,10,4],[12,13,12],"#cap"), cube([6.5,9,6.5],[9.5,10,9.5],"#stem"), cube([3.5,11,7],[5,12,9],"#cap")],
    3: [cube([3,10,3],[13,14,13],"#cap"), cube([6.5,9,6.5],[9.5,10,9.5],"#stem"), cube([4,11,4],[6,13,6],"#cap"), cube([10,11,10],[12,13,12],"#cap")],
}.items():
    model = copy.deepcopy(bag)
    model["elements"] = model["elements"] + elems
    (root / f"models/block/mushroom_bag_stage_{stage}.json").write_text(json.dumps(model, indent=2) + "\n", encoding="utf-8")

tray = json.loads((root / "models/block/nursery_tray.json").read_text(encoding="utf-8"))
tray.setdefault("textures", {})["sprout"] = "tfc:block/crop/wheat_7"
for stage, elems in {
    1: [cube([7,2,7],[9,4,9],"#sprout")],
    2: [cube([6.5,2,6.5],[9.5,6,9.5],"#sprout"), cube([8,6,8],[10,7,10],"#sprout")],
}.items():
    model = copy.deepcopy(tray)
    model["elements"] = model["elements"] + elems
    (root / f"models/block/nursery_tray_stage_{stage}.json").write_text(json.dumps(model, indent=2) + "\n", encoding="utf-8")

# blockstates
bag_bs = {"variants": {f"stage={s}": {"model": "tfcagricultureplus:block/mushroom_bag" if s == 0 else f"tfcagricultureplus:block/mushroom_bag_stage_{s}"} for s in range(4)}}
(root / "blockstates/mushroom_bag.json").write_text(json.dumps(bag_bs, indent=2) + "\n", encoding="utf-8")
tray_bs = {"variants": {f"stage={s}": {"model": "tfcagricultureplus:block/nursery_tray" if s == 0 else f"tfcagricultureplus:block/nursery_tray_stage_{s}"} for s in range(3)}}
(root / "blockstates/nursery_tray.json").write_text(json.dumps(tray_bs, indent=2) + "\n", encoding="utf-8")
print("generated stage models")
