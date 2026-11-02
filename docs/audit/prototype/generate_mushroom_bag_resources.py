from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
block_model = assets / "models/block/mushroom_bag.json"
block_model.parent.mkdir(parents=True, exist_ok=True)
block_model.write_text(json.dumps({
    "parent": "minecraft:block/cube_all",
    "textures": {"all": "tfc:block/wood/planks/oak"}
}, indent=2) + "\n", encoding="utf-8")
item_model = assets / "models/item/mushroom_bag.json"
item_model.write_text(json.dumps({"parent": "tfcagricultureplus:block/mushroom_bag"}, indent=2) + "\n", encoding="utf-8")
blockstate = assets / "blockstates/mushroom_bag.json"
blockstate.write_text(json.dumps({"variants": {f"stage={s}": {"model": "tfcagricultureplus:block/mushroom_bag"} for s in range(4)}}, indent=2) + "\n", encoding="utf-8")
loot = data / "loot_table/blocks/mushroom_bag.json"
loot.parent.mkdir(parents=True, exist_ok=True)
loot.write_text(json.dumps({
    "type": "minecraft:block",
    "pools": [{"rolls": 1, "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:mushroom_bag"}],
               "conditions": [{"condition": "minecraft:survives_explosion"}]}]
}, indent=2) + "\n", encoding="utf-8")
recipe = data / "recipe/crafting/mushroom_bag.json"
recipe.parent.mkdir(parents=True, exist_ok=True)
recipe.write_text(json.dumps({
    "type": "minecraft:crafting_shapeless",
    "ingredients": [{"item": "tfc:straw"}, {"item": "minecraft:dirt"}],
    "result": {"count": 1, "id": "tfcagricultureplus:mushroom_bag"}
}, indent=2) + "\n", encoding="utf-8")
for lang, name in (("en_us", "Mushroom Bag"), ("zh_cn", "蘑菇菌包")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    d["block.tfcagricultureplus.mushroom_bag"] = name
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("mushroom bag resources written")
