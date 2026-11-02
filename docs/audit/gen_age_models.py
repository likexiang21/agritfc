import json, pathlib
root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
# generic age models using existing TFC wheat age textures (no new textures)
for age in range(8):
    model = {
        "parent": "minecraft:block/crop",
        "textures": {"crop": f"tfc:block/crop/wheat_{age}"}
    }
    (root / f"models/block/spice_crop/age_{age}.json").write_text(json.dumps(model, indent=2) + "\n", encoding="utf-8")
    berry = {
        "parent": "minecraft:block/crop",
        "textures": {"crop": f"tfc:block/crop/wheat_{age}"}
    }
    (root / f"models/block/crop/strawberry_age_{age}.json").write_text(json.dumps(berry, indent=2) + "\n", encoding="utf-8")

for p in (root / "blockstates/spice_crop").glob("*.json"):
    data = json.loads(p.read_text(encoding="utf-8"))
    data["variants"] = {
        f"age={age}": {"model": f"tfcagricultureplus:block/spice_crop/age_{age}"}
        for age in range(8)
    }
    p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

p = root / "blockstates/crop/strawberry.json"
data = json.loads(p.read_text(encoding="utf-8"))
data["variants"] = {
    f"age={age}": {"model": f"tfcagricultureplus:block/crop/strawberry_age_{age}"}
    for age in range(8)
}
p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
print("generated spice/strawberry age models")
