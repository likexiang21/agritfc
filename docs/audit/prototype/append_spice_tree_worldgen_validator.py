from pathlib import Path

p = Path("mod_rebuild/docs/audit/prototype/validate_crop_p0a.py")
if "PASS: spice tree worldgen resources" not in p.read_text(encoding="utf-8"):
    p.write_text(p.read_text(encoding="utf-8") + '''
for tree in spice_trees:
    assert (root / "data/tfcagricultureplus/worldgen/configured_feature" / ("spice_sapling_" + tree + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/worldgen/placed_feature" / ("spice_sapling_" + tree + ".json")).is_file()
assert (root / "data/tfcagricultureplus/neoforge/biome_modifier/add_spice_trees.json").is_file()
print("PASS: spice tree worldgen resources")
''', encoding="utf-8")
print("validator appended")
