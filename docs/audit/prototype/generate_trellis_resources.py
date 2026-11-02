from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
(assets / "blockstates/spice_trellis.json").write_text(json.dumps({"variants": {"": {"model": "tfcagricultureplus:block/spice_trellis"}}}, indent=2) + "\n", encoding="utf-8")
(assets / "models/block/spice_trellis.json").write_text(json.dumps({"parent": "minecraft:block/cube_all", "textures": {"all": "tfc:block/wood/planks/oak"}}, indent=2) + "\n", encoding="utf-8")
(assets / "models/item/spice_trellis.json").write_text(json.dumps({"parent": "tfcagricultureplus:block/spice_trellis"}, indent=2) + "\n", encoding="utf-8")
(data / "loot_table/blocks/spice_trellis.json").write_text(json.dumps({"type": "minecraft:block", "pools": [{"rolls": 1, "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:spice_trellis"}], "conditions": [{"condition": "minecraft:survives_explosion"}]}]}, indent=2) + "\n", encoding="utf-8")
(data / "recipe/crafting/spice_trellis.json").write_text(json.dumps({
    "type": "minecraft:crafting_shaped",
    "pattern": ["S S", "PPP", "S S"],
    "key": {"S": {"item": "minecraft:stick"}, "P": {"item": "minecraft:oak_planks"}},
    "result": {"count": 2, "id": "tfcagricultureplus:spice_trellis"}
}, indent=2) + "\n", encoding="utf-8")
for lang, label in (("en_us", "Spice Trellis"), ("zh_cn", "香料支架")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    d["block.tfcagricultureplus.spice_trellis"] = label
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("trellis resources written")
