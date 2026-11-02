from pathlib import Path

p = Path("mod_rebuild/docs/audit/prototype/validate_crop_p0a.py")
if "PASS: tree biome tags" not in p.read_text(encoding="utf-8"):
    p.write_text(p.read_text(encoding="utf-8") + '''
assert (root / "data/tfcagricultureplus/tags/worldgen/biome/nut_tree_biomes.json").is_file()
assert (root / "data/tfcagricultureplus/tags/worldgen/biome/spice_tree_biomes.json").is_file()
nut_modifier = json.loads((root / "data/tfcagricultureplus/neoforge/biome_modifier/add_nut_saplings.json").read_text(encoding="utf-8"))
spice_modifier = json.loads((root / "data/tfcagricultureplus/neoforge/biome_modifier/add_spice_trees.json").read_text(encoding="utf-8"))
assert nut_modifier["biomes"] == "#tfcagricultureplus:nut_tree_biomes"
assert spice_modifier["biomes"] == "#tfcagricultureplus:spice_tree_biomes"
print("PASS: tree biome tags")
''', encoding="utf-8")
print("validator appended")
