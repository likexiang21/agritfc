from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
block_model = assets / "models/block/nursery_tray.json"
block_model.parent.mkdir(parents=True, exist_ok=True)
block_model.write_text(json.dumps({"parent": "minecraft:block/cube_all",
                                   "textures": {"all": "tfc:block/wood/planks/oak"}}, indent=2) + "\n", encoding="utf-8")
(assets / "models/item/nursery_tray.json").write_text(
    json.dumps({"parent": "tfcagricultureplus:block/nursery_tray"}, indent=2) + "\n", encoding="utf-8")
(assets / "models/item/seedling.json").parent.mkdir(parents=True, exist_ok=True)
(assets / "models/item/seedling.json").write_text(json.dumps({"parent": "minecraft:item/generated",
                                                              "textures": {"layer0": "tfc:item/straw"}}, indent=2) + "\n", encoding="utf-8")
blockstate = assets / "blockstates/nursery_tray.json"
blockstate.write_text(json.dumps({"variants": {f"stage={s}": {"model": "tfcagricultureplus:block/nursery_tray"} for s in range(3)}}, indent=2) + "\n", encoding="utf-8")
loot = data / "loot_table/blocks/nursery_tray.json"
loot.parent.mkdir(parents=True, exist_ok=True)
loot.write_text(json.dumps({"type": "minecraft:block", "pools": [{"rolls": 1,
    "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:nursery_tray"}],
    "conditions": [{"condition": "minecraft:survives_explosion"}]}]}, indent=2) + "\n", encoding="utf-8")
recipe = data / "recipe/crafting/nursery_tray.json"
recipe.parent.mkdir(parents=True, exist_ok=True)
recipe.write_text(json.dumps({"type": "minecraft:crafting_shapeless",
                              "ingredients": [{"item": "minecraft:oak_planks"}, {"item": "tfc:straw"}],
                              "result": {"count": 1, "id": "tfcagricultureplus:nursery_tray"}}, indent=2) + "\n", encoding="utf-8")
for lang, tray, seed in (("en_us", "Nursery Tray", "Seedling"), ("zh_cn", "育苗盘", "幼苗")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    d["block.tfcagricultureplus.nursery_tray"] = tray
    d["item.tfcagricultureplus.seedling"] = seed
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("nursery resources written")
