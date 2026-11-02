from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus")
for tree in ("pistachio", "cashew", "macadamia"):
    feature = root / "worldgen/configured_feature" / ("nut_sapling_" + tree + ".json")
    feature.parent.mkdir(parents=True, exist_ok=True)
    feature.write_text(json.dumps({
        "type": "minecraft:simple_block",
        "config": {"to_place": {"type": "minecraft:simple_state_provider", "state": {
            "Name": "tfcagricultureplus:nut_sapling/" + tree,
            "Properties": {"stage": "0"}
        }}}
    }, indent=2) + "\n", encoding="utf-8")
    placed = root / "worldgen/placed_feature" / ("nut_sapling_" + tree + ".json")
    placed.parent.mkdir(parents=True, exist_ok=True)
    placed.write_text(json.dumps({
        "feature": "tfcagricultureplus:nut_sapling_" + tree,
        "placement": [
            {"type": "minecraft:count", "count": {"type": "minecraft:uniform", "min": 1, "max": 2}},
            {"type": "minecraft:in_square"},
            {"type": "minecraft:heightmap", "heightmap": "MOTION_BLOCKING"},
            {"type": "minecraft:block_predicate_filter",
             "predicate": {"type": "minecraft:would_survive"}},
            {"type": "minecraft:biome"}
        ]
    }, indent=2) + "\n", encoding="utf-8")
modifier = root / "neoforge/biome_modifier/add_nut_saplings.json"
modifier.write_text(json.dumps({
    "type": "neoforge:add_features",
    "biomes": "#tfcagricultureplus:wild_mushroom_biomes",
    "features": ["tfcagricultureplus:nut_sapling_pistachio", "tfcagricultureplus:nut_sapling_cashew", "tfcagricultureplus:nut_sapling_macadamia"],
    "step": "vegetal_decoration"
}, indent=2) + "\n", encoding="utf-8")
print("nut tree worldgen written")
