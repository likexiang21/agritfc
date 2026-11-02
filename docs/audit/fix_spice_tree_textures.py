import json, pathlib
root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/block")
mapping = {
    "cinnamon": ("kapok", "kapok"),
    "clove": ("maple", "maple"),
    "nutmeg": ("sequoia", "sequoia"),
    "pimento": ("palm", "palm"),
    "star_anise": ("willow", "willow"),
}
for species, (leaf, sapling) in mapping.items():
    p = root / "spice_leaves" / (species + ".json")
    p.write_text(json.dumps({"parent": "minecraft:block/leaves",
                             "textures": {"all": f"tfc:block/wood/leaves/{leaf}_fluff"}}, indent=2) + "\n", encoding="utf-8")
    q = root / "spice_sapling" / (species + ".json")
    q.write_text(json.dumps({"parent": "minecraft:block/cross",
                             "textures": {"cross": f"tfc:block/wood/sapling/{sapling}"}}, indent=2) + "\n", encoding="utf-8")
print("updated spice tree models")
