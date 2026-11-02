import json, pathlib
root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
for age in range(3):
    model = {"parent": "minecraft:block/cross",
             "textures": {"cross": f"tfc:block/crop/wheat_{age}"}}
    (root / f"models/block/wild_mushroom/age_{age}.json").write_text(json.dumps(model, indent=2) + "\n", encoding="utf-8")
for p in (root / "blockstates/wild_mushroom").glob("*.json"):
    data = json.loads(p.read_text(encoding="utf-8"))
    data["variants"] = {f"age={age}": {"model": f"tfcagricultureplus:block/wild_mushroom/age_{age}"} for age in range(3)}
    p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
print("wild mushroom age models updated")
