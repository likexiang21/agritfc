from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
species = ["pistachio", "cashew", "macadamia"]
for sp in species:
    leaf_path = "nut_leaves/" + sp
    variants = {}
    for nut in range(4):
        variants[f"persistent=true,nut_state={nut}"] = {"model": "tfcagricultureplus:block/" + leaf_path}
        for distance in range(1, 8):
            variants[f"persistent=false,distance={distance},nut_state={nut}"] = {
                "model": "tfcagricultureplus:block/" + leaf_path}
    bs = assets / "blockstates" / (leaf_path + ".json")
    bs.parent.mkdir(parents=True, exist_ok=True)
    bs.write_text(json.dumps({"variants": variants}, indent=2) + "\n", encoding="utf-8")
    model = assets / "models/block" / (leaf_path + ".json")
    model.parent.mkdir(parents=True, exist_ok=True)
    model.write_text(json.dumps({"parent": "minecraft:block/leaves",
                                 "textures": {"all": "tfc:block/wood/leaves/oak_fluff"}}, indent=2) + "\n", encoding="utf-8")

    sapling_path = "nut_sapling/" + sp
    sb = assets / "blockstates" / (sapling_path + ".json")
    sb.parent.mkdir(parents=True, exist_ok=True)
    sb.write_text(json.dumps({"variants": {
        f"stage={stage}": {"model": "tfcagricultureplus:block/" + sapling_path} for stage in range(3)
    }}, indent=2) + "\n", encoding="utf-8")
    sm = assets / "models/block" / (sapling_path + ".json")
    sm.parent.mkdir(parents=True, exist_ok=True)
    sm.write_text(json.dumps({"parent": "minecraft:block/cross",
                              "textures": {"cross": "tfc:block/berry_bush/strawberry_bush"}}, indent=2) + "\n", encoding="utf-8")
    im = assets / "models/item" / (sapling_path + ".json")
    im.parent.mkdir(parents=True, exist_ok=True)
    im.write_text(json.dumps({"parent": "tfcagricultureplus:block/" + sapling_path}, indent=2) + "\n", encoding="utf-8")

    leaf_loot = data / "loot_table/blocks" / (leaf_path + ".json")
    leaf_loot.parent.mkdir(parents=True, exist_ok=True)
    leaf_loot.write_text(json.dumps({"type": "minecraft:block", "pools": [
        {"rolls": 1, "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:" + sp}],
         "conditions": [{"condition": "minecraft:random_chance", "chance": 0.05}]},
        {"rolls": 1, "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:nut_shell/" + sp}],
         "conditions": [{"condition": "minecraft:random_chance", "chance": 0.05}]},
        {"rolls": 1, "entries": [{"type": "minecraft:item", "name": "tfcagricultureplus:" + sapling_path}],
         "conditions": [{"condition": "minecraft:random_chance", "chance": 0.05}]}
    ]}, indent=2) + "\n", encoding="utf-8")
    sapling_loot = data / "loot_table/blocks" / (sapling_path + ".json")
    sapling_loot.parent.mkdir(parents=True, exist_ok=True)
    sapling_loot.write_text(json.dumps({"type": "minecraft:block", "pools": [{"rolls": 1, "entries": [
        {"type": "minecraft:item", "name": "tfcagricultureplus:" + sapling_path}],
        "conditions": [{"condition": "minecraft:survives_explosion"}]}]}, indent=2) + "\n", encoding="utf-8")
    recipe = data / "recipe/crafting" / ("nut_sapling_" + sp + ".json")
    recipe.parent.mkdir(parents=True, exist_ok=True)
    recipe.write_text(json.dumps({"type": "minecraft:crafting_shapeless",
                                  "ingredients": [{"item": "tfcagricultureplus:" + sp},
                                                  {"item": "minecraft:dirt"}],
                                  "result": {"count": 1, "id": "tfcagricultureplus:" + sapling_path}},
                                 indent=2) + "\n", encoding="utf-8")
for lang, leaves, sapling in (("en_us", "Nut Leaves ({})", "Nut Sapling ({})"),
                              ("zh_cn", "坚果树叶（{}）", "坚果幼苗（{}）")):
    path = assets / "lang" / (lang + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    for sp in species:
        d["block.tfcagricultureplus.nut_leaves." + sp] = leaves.format(sp)
        d["block.tfcagricultureplus.nut_sapling." + sp] = sapling.format(sp)
        d["item.tfcagricultureplus.nut_sapling." + sp] = sapling.format(sp)
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("nut tree resources written")
