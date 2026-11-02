from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus")
species = ["pimento", "cinnamon", "clove", "nutmeg", "star_anise"]
for sp in species:
    feature = root / "worldgen/configured_feature" / ("spice_sapling_" + sp + ".json")
    feature.parent.mkdir(parents=True, exist_ok=True)
    feature.write_text(json.dumps({
        "type": "minecraft:simple_block",
        "config": {"to_place": {"type": "minecraft:simple_state_provider", "state": {
            "Name": "tfcagricultureplus:spice_sapling/" + sp,
            "Properties": {"stage": "0"}
        }}}
    }, indent=2) + "\n", encoding="utf-8")
    placed = root / "worldgen/placed_feature" / ("spice_sapling_" + sp + ".json")
    placed.parent.mkdir(parents=True, exist_ok=True)
    placed.write_text(json.dumps({
        "feature": "tfcagricultureplus:spice_sapling_" + sp,
        "placement": [
            {"type": "minecraft:count", "count": {"type": "minecraft:uniform", "min": 1, "max": 2}},
            {"type": "minecraft:in_square"},
            {"type": "minecraft:heightmap", "heightmap": "MOTION_BLOCKING"},
            {"type": "minecraft:block_predicate_filter", "predicate": {"type": "minecraft:would_survive"}},
            {"type": "minecraft:biome"}
        ]
    }, indent=2) + "\n", encoding="utf-8")
modifier = root / "neoforge/biome_modifier/add_spice_trees.json"
modifier.write_text(json.dumps({
    "type": "neoforge:add_features",
    "biomes": "#tfcagricultureplus:wild_mushroom_biomes",
    "features": ["tfcagricultureplus:spice_sapling_" + sp for sp in species],
    "step": "vegetal_decoration"
}, indent=2) + "\n", encoding="utf-8")
print("spice tree worldgen written")
