from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
species = [
    ("oyster", "平菇", False), ("shiitake", "香菇", False), ("button", "双孢菇", False),
    ("enoki", "金针菇", False), ("wood_ear", "木耳", False), ("reishi", "灵芝", False),
    ("lions_mane", "猴头菇", False), ("maitake", "舞茸", False), ("king_oyster", "杏鲍菇", False),
    ("shimeji", "蟹味菇", False), ("turkey_tail", "云芝", False),
    ("porcini", "牛肝菌", True), ("morel", "羊肚菌", True),
    ("chanterelle", "鸡油菌", True), ("black_truffle", "黑松露", True),
]
texture = "tfc:block/plant/red_oat_grass/red_oat_grass"

for name, cn, natural_only in species:
    block_id = "wild_mushroom/" + name
    block_model = assets / "models/block" / (block_id + ".json")
    block_model.parent.mkdir(parents=True, exist_ok=True)
    block_model.write_text(json.dumps({
        "parent": "minecraft:block/cross",
        "textures": {"cross": texture}
    }, indent=2) + "\n", encoding="utf-8")
    item_model = assets / "models/item" / (block_id + ".json")
    item_model.parent.mkdir(parents=True, exist_ok=True)
    item_model.write_text(json.dumps({"parent": "tfcagricultureplus:block/" + block_id}, indent=2) + "\n", encoding="utf-8")
    blockstate = assets / "blockstates" / (block_id + ".json")
    blockstate.parent.mkdir(parents=True, exist_ok=True)
    blockstate.write_text(json.dumps({"variants": {f"age={a}": {"model": "tfcagricultureplus:block/" + block_id} for a in range(3)}}, indent=2) + "\n", encoding="utf-8")
    loot = data / "loot_table/blocks" / (block_id + ".json")
    loot.parent.mkdir(parents=True, exist_ok=True)
    loot.write_text(json.dumps({"type": "minecraft:block", "pools": [{
        "rolls": 1,
        "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:" + block_id}],
        "conditions": [{"condition": "minecraft:survives_explosion"}]
    }]}, indent=2) + "\n", encoding="utf-8")

    configured = data / "worldgen/configured_feature" / ("wild_mushroom_" + name + ".json")
    configured.parent.mkdir(parents=True, exist_ok=True)
    configured.write_text(json.dumps({
        "type": "minecraft:simple_block",
        "config": {"to_place": {
            "type": "minecraft:simple_state_provider",
            "state": {"Name": "tfcagricultureplus:" + block_id, "Properties": {"age": "0"}}
        }}
    }, indent=2) + "\n", encoding="utf-8")
    placed = data / "worldgen/placed_feature" / ("wild_mushroom_" + name + ".json")
    placed.parent.mkdir(parents=True, exist_ok=True)
    placed.write_text(json.dumps({
        "feature": "tfcagricultureplus:wild_mushroom_" + name,
        "placement": [
            {"type": "minecraft:count", "count": {"type": "minecraft:uniform", "min": 1, "max": 2}},
            {"type": "minecraft:in_square"},
            {"type": "minecraft:heightmap", "heightmap": "MOTION_BLOCKING"},
            {"type": "minecraft:biome"}
        ]
    }, indent=2) + "\n", encoding="utf-8")

# Language keys
for lang in ("en_us.json", "zh_cn.json"):
    path = assets / "lang" / lang
    value = json.loads(path.read_text(encoding="utf-8"))
    for name, cn, _ in species:
        value["block.tfcagricultureplus.wild_mushroom." + name] = ("野生" + cn) if lang.startswith("zh") else ("Wild " + name.replace("_", " ").title())
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# All 15 are placed; four natural-only never get a bag recipe (bag system is not implemented yet).
biome_tag = data / "tags/worldgen/biome/wild_mushroom_biomes.json"
biome_tag.parent.mkdir(parents=True, exist_ok=True)
biome_tag.write_text(json.dumps({
    "replace": False,
    "values": ["#minecraft:is_forest", "#minecraft:is_taiga", "#minecraft:is_swamp"]
}, indent=2) + "\n", encoding="utf-8")

modifier = data / "neoforge/biome_modifier/add_wild_mushrooms.json"
modifier.parent.mkdir(parents=True, exist_ok=True)
modifier.write_text(json.dumps({
    "type": "neoforge:add_features",
    "biomes": "#tfcagricultureplus:wild_mushroom_biomes",
    "features": ["tfcagricultureplus:wild_mushroom_" + name for name, _, _ in species],
    "step": "vegetal_decoration"
}, indent=2) + "\n", encoding="utf-8")

print("wild mushrooms:", len(species), "worldgen features:", len(list(configured.parent.glob('wild_mushroom_*.json'))))
