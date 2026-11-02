from pathlib import Path

p = Path("mod_rebuild/docs/audit/prototype/validate_crop_p0a.py")
if "PASS: spice tree resources" not in p.read_text(encoding="utf-8"):
    p.write_text(p.read_text(encoding="utf-8") + '''
# P0-AS tree-form spices.
spice_trees = ["pimento", "cinnamon", "clove", "nutmeg", "star_anise"]
for tree in spice_trees:
    leaf_path = "spice_leaves/" + tree
    sapling_path = "spice_sapling/" + tree
    assert (assets / "blockstates" / (leaf_path + ".json")).is_file()
    assert (assets / "blockstates" / (sapling_path + ".json")).is_file()
    assert (assets / "models/block" / (leaf_path + ".json")).is_file()
    assert (assets / "models/block" / (sapling_path + ".json")).is_file()
    assert (assets / "models/item" / (sapling_path + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/loot_table/blocks" / (leaf_path + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/loot_table/blocks" / (sapling_path + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/recipe/crafting" / ("spice_sapling_" + tree + ".json")).is_file()
print("PASS: spice tree resources")
''', encoding="utf-8")
print("validator appended")
