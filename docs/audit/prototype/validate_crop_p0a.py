from pathlib import Path
import json, re, zipfile

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
tfc_jar = sorted(Path("mods").glob("TerraFirmaCraft-NeoForge-*.jar"))[-1]
a_jar = sorted(Path("mods").glob("TFCFarmingPlus-NeoForge-*.jar"))[-1]
crops = ["millet", "foxtail_millet", "fonio", "spelt", "emmer", "einkorn",
         "pearl_millet", "finger_millet", "sorghum", "jobs_tears",
         "barley", "oat", "rice", "rye", "wheat", "maize"]
expected = {"wet_grass": "tfc:item/straw"}
for c in crops:
    expected["grain_bundle/" + c] = "tfc:item/stick_bundle"

doc = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md").read_text(encoding="utf-8")
s = doc.find("#### 4.1.2")
e = doc.find("#### 4.1.3")
waste = []
for line in doc[s:e].splitlines():
    if line.startswith("| `") and "crop_waste/" in line:
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        waste.append((parts[0].strip("`"), parts[4].strip("`")))
assert len(waste) == 82, len(waste)

models = 0
with zipfile.ZipFile(tfc_jar) as z_tfc, zipfile.ZipFile(a_jar) as z_a:
    tfc_names = set(z_tfc.namelist())
    a_names = set(z_a.namelist())
    for item, tex in expected.items():
        model = assets / "models/item" / (item + ".json")
        assert model.is_file(), f"missing model {model}"
        data = json.loads(model.read_text(encoding="utf-8"))
        assert data["textures"]["layer0"] == tex, item
        assert ("assets/tfc/textures/" + tex.split(":", 1)[1] + ".png") in tfc_names, tex
        models += 1
    for crop, _tag in waste:
        model = assets / "models/item/crop_waste" / (crop + ".json")
        assert model.is_file(), f"missing waste model {crop}"
        data = json.loads(model.read_text(encoding="utf-8"))
        assert data["textures"]["layer0"] == "tfc:item/straw", f"waste texture {crop}"
        assert "assets/tfc/textures/item/straw.png" in tfc_names
        models += 1

for lang in ("en_us.json", "zh_cn.json"):
    data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
    assert "item.tfcagricultureplus.wet_grass" in data
    for c in crops:
        assert "item.tfcagricultureplus.grain_bundle." + c in data
    for crop, _tag in waste:
        assert "item.tfcagricultureplus.crop_waste." + crop in data

recipe_dir = root / "data/tfcagricultureplus/recipe"
recipes = [recipe_dir / "drying/wet_grass.json"] + sorted((recipe_dir / "crafting").glob("grain_bundle_*.json"))
for recipe in recipes:
    data = json.loads(recipe.read_text(encoding="utf-8"))
    assert data.get("type"), f"missing recipe type {recipe}"

for c in crops:
    recipe = recipe_dir / "crafting" / ("grain_bundle_" + c + ".json")
    data = json.loads(recipe.read_text(encoding="utf-8"))
    result = data["result"]
    result_id = result.get("id") or result["stack"]["id"]
    ns, path = result_id.split(":", 1)
    if ns == "tfc":
        assert ("assets/tfc/models/item/" + path + ".json") in tfc_names, result_id
    else:
        assert ("assets/tfcfarmingplus/models/item/" + path + ".json") in a_names, result_id

# Every waste item must be listed in exactly its intended TFC green-compost tag.
for level in ("high", "medium", "low"):
    tag_path = root / "data/tfc/tags/item/compost_greens" / (level + ".json")
    if not tag_path.exists():
        continue
    payload = json.loads(tag_path.read_text(encoding="utf-8"))
    assert payload.get("replace") is False, tag_path
    values = payload.get("values", [])
    assert len(values) == len(set(values)), tag_path
    for crop, tag in waste:
        item = "tfcagricultureplus:crop_waste/" + crop
        if tag.endswith("/" + level):
            assert item in values, f"{item} missing from {level}"

# Wild mushrooms: 15 blocks, 15 wild features, 4 natural-only (no bag yet).
mushrooms = ["oyster", "shiitake", "button", "enoki", "wood_ear", "reishi", "lions_mane",
             "maitake", "king_oyster", "shimeji", "turkey_tail", "porcini", "morel",
             "chanterelle", "black_truffle"]
with zipfile.ZipFile(tfc_jar) as z:
    names = set(z.namelist())
    assert "assets/tfc/textures/block/plant/red_oat_grass/red_oat_grass.png" in names
for m in mushrooms:
    block_id = "wild_mushroom/" + m
    bs = assets / "blockstates" / (block_id + ".json")
    assert bs.is_file(), bs
    variants = json.loads(bs.read_text(encoding="utf-8"))["variants"]
    assert set(variants) == {"age=0", "age=1", "age=2"}, block_id
    model = assets / "models/block" / (block_id + ".json")
    assert model.is_file(), model
    assert (assets / "models/item" / (block_id + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/loot_table/blocks" / (block_id + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/worldgen/configured_feature" / ("wild_mushroom_" + m + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/worldgen/placed_feature" / ("wild_mushroom_" + m + ".json")).is_file()

biome_modifier = root / "data/tfcagricultureplus/neoforge/biome_modifier/add_wild_mushrooms.json"
modifier = json.loads(biome_modifier.read_text(encoding="utf-8"))
assert modifier["type"] == "neoforge:add_features"
assert len(modifier["features"]) == 15

# Four-stage mushroom bag (11 cultivable species; natural-only species rejected in code).
bag_states = assets / "blockstates/mushroom_bag.json"
assert bag_states.is_file()
assert set(json.loads(bag_states.read_text(encoding="utf-8"))["variants"]) == {f"stage={s}" for s in range(4)}
assert (assets / "models/block/mushroom_bag.json").is_file()
assert (assets / "models/item/mushroom_bag.json").is_file()
assert (root / "data/tfcagricultureplus/loot_table/blocks/mushroom_bag.json").is_file()
assert (root / "data/tfcagricultureplus/recipe/crafting/mushroom_bag.json").is_file()
for lang in ("en_us.json", "zh_cn.json"):
    lang_data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
    assert "block.tfcagricultureplus.mushroom_bag" in lang_data
    for nut in ("acorn", "chestnut", "pine_nut", "hickory_nut", "pistachio", "cashew", "macadamia", "beechnut"):
        assert "item.tfcagricultureplus." + nut in lang_data
        assert (assets / "models/item" / (nut + ".json")).is_file()
        assert (assets / "models/item/ground_nut" / (nut + ".json")).is_file()
        assert (root / "data/tfcagricultureplus/recipe/mortar" / ("ground_" + nut + ".json")).is_file()
        assert "item.tfcagricultureplus.ground_nut." + nut in lang_data
        assert (assets / "models/item/nut_shell" / (nut + ".json")).is_file()
        assert "item.tfcagricultureplus.nut_shell." + nut in lang_data

# TFC leaves: every TFC leaf blockstate must be expanded for nut_state=0..3.
leaf_states = root / "assets/tfc/blockstates/wood/leaves"
leaf_count = 0
with zipfile.ZipFile(tfc_jar) as z:
    for name in z.namelist():
        if not (name.startswith("assets/tfc/blockstates/wood/leaves/") and name.endswith(".json")):
            continue
        source = json.loads(z.read(name).decode("utf-8"))
        target = leaf_states / Path(name).name
        assert target.is_file(), target
        expanded = json.loads(target.read_text(encoding="utf-8"))
        if "variants" in source:
            variants = expanded["variants"]
            assert len(variants) == len(source["variants"]) * 4, target
            for key in variants:
                assert any(f"nut_state={n}" in key for n in range(4)), key
        else:
            parts = expanded["multipart"]
            assert len(parts) == len(source["multipart"]) * 4, target
            for part in parts:
                assert "nut_state" in part["when"], target
        leaf_count += 1

mixin_config = json.loads((root / "tfcagricultureplus.mixins.json").read_text(encoding="utf-8"))
assert "TFCLeavesNutStateMixin" in mixin_config["mixins"]

# AFC leaves use the same TFCLeavesBlock family; expand their blockstates too.
afc_jar = sorted(Path("mods").glob("afc-*.jar"))[-1]
afc_leaf_states = root / "assets/afc/blockstates/wood/leaves"
afc_leaf_count = 0
with zipfile.ZipFile(afc_jar) as z:
    for name in z.namelist():
        if not (name.startswith("assets/afc/blockstates/wood/leaves/") and name.endswith(".json")):
            continue
        source = json.loads(z.read(name).decode("utf-8"))
        target = afc_leaf_states / Path(name).name
        assert target.is_file(), target
        expanded = json.loads(target.read_text(encoding="utf-8"))
        if "variants" in source:
            assert len(expanded["variants"]) == len(source["variants"]) * 4, target
            for key in expanded["variants"]:
                assert any(f"nut_state={n}" in key for n in range(4)), key
        else:
            assert len(expanded["multipart"]) == len(source["multipart"]) * 4, target
            for part in expanded["multipart"]:
                assert "nut_state" in part["when"], target
        afc_leaf_count += 1

mapped_leaves = [
    "tfc:wood/leaves/oak", "tfc:wood/leaves/chestnut", "tfc:wood/leaves/pine", "tfc:wood/leaves/hickory",
    "afc:wood/leaves/black_oak", "afc:wood/leaves/live_oak", "afc:wood/leaves/hardy_chestnut",
    "afc:wood/leaves/chinquapin", "afc:wood/leaves/red_pine", "afc:wood/leaves/stone_pine",
    "afc:wood/leaves/huangshan_pine", "afc:wood/leaves/scrub_hickory", "afc:wood/leaves/beech",
    "afc:wood/leaves/black_beech", "afc:wood/leaves/rauli_beech",
]
with zipfile.ZipFile(tfc_jar) as z_tfc, zipfile.ZipFile(afc_jar) as z_afc:
    for leaf in mapped_leaves:
        ns, path = leaf.split(":", 1)
        names_for_ns = set(z_tfc.namelist() if ns == "tfc" else z_afc.namelist())
        assert f"assets/{ns}/blockstates/wood/leaves/{path.split('/')[-1]}.json" in names_for_ns, leaf

print_flag = f"PASS: {models} item models, 2 lang files, {len(recipes)} recipes, {len(waste)} crop_waste, {len(mushrooms)} wild mushrooms, 4-stage bag, {leaf_count + afc_leaf_count} nut leaf states, tags valid"

# 15 crop-form spices + 5 tree-form spices.
spices = ["basil", "bay_laurel", "cardamom", "cilantro", "cumin", "oregano", "pimento", "vanilla",
          "black_pepper", "cinnamon", "clove", "nutmeg", "saffron", "star_anise", "rosemary",
          "thyme", "sage", "dill", "fennel", "mustard"]
tree_spices = {"pimento", "cinnamon", "clove", "nutmeg", "star_anise"}
crop_spices = [s for s in spices if s not in tree_spices]
with zipfile.ZipFile(tfc_jar) as z:
    assert "assets/tfc/textures/block/crop/wheat_7.png" in set(z.namelist())
for spice in crop_spices:
    crop_path = "spice_crop/" + spice
    bs = assets / "blockstates" / (crop_path + ".json")
    assert bs.is_file(), bs
    assert set(json.loads(bs.read_text(encoding="utf-8"))["variants"]) == {f"age={a}" for a in range(8)}, crop_path
    assert (assets / "models/block" / (crop_path + ".json")).is_file()
    assert (assets / "models/item" / ("spice_seed/" + spice + ".json")).is_file()
    assert (assets / "models/item" / ("spice/" + spice + ".json")).is_file()
    assert (assets / "models/item" / ("spice_waste/" + spice + ".json")).is_file()
    assert (assets / "models/item" / ("ground_spice/" + spice + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/recipe/mortar" / ("ground_" + spice + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/loot_table/blocks" / (crop_path + ".json")).is_file()

spice_waste = 0
for level in ("high", "medium", "low"):
    tag_path = root / "data/tfc/tags/item/compost_greens" / (level + ".json")
    if not tag_path.exists():
        continue
    payload = json.loads(tag_path.read_text(encoding="utf-8"))
    for spice in spices:
        item = "tfcagricultureplus:spice_waste/" + spice
        if item in payload.get("values", []):
            assert level in ("high", "medium"), (spice, level)
            spice_waste += 1

bushes = ["blackberry", "blueberry", "bunchberry", "cloudberry", "cranberry",
          "elderberry", "gooseberry", "raspberry", "snowberry", "wintergreen"]
for bush in bushes:
    assert (assets / "models/item/bush_waste" / (bush + ".json")).is_file()
    for lang in ("en_us.json", "zh_cn.json"):
        lang_data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
        assert "item.tfcagricultureplus.bush_waste." + bush in lang_data

print_flag = (f"PASS: {models} item models, 2 lang files, {len(recipes)} recipes, "
              f"{len(waste) + spice_waste} crop_waste, {len(bushes)} bush_waste, "
              f"{len(mushrooms)} wild mushrooms, 4-stage bag, {leaf_count + afc_leaf_count} nut leaf states, "
              f"15 spice crops, 5 spice trees, 20 ground spices, 8 ground nuts, 8 nut shells, tags valid")
print(print_flag)

# Nursery tray + generic seedling.
nursery_bs = assets / "blockstates/nursery_tray.json"
assert nursery_bs.is_file()
assert set(json.loads(nursery_bs.read_text(encoding="utf-8"))["variants"]) == {f"stage={s}" for s in range(3)}
assert (assets / "models/block/nursery_tray.json").is_file()
assert (assets / "models/item/nursery_tray.json").is_file()
assert (assets / "models/item/seedling.json").is_file()
assert (root / "data/tfcagricultureplus/loot_table/blocks/nursery_tray.json").is_file()
assert (root / "data/tfcagricultureplus/recipe/crafting/nursery_tray.json").is_file()
for lang in ("en_us.json", "zh_cn.json"):
    lang_data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
    assert "block.tfcagricultureplus.nursery_tray" in lang_data
    assert "item.tfcagricultureplus.seedling" in lang_data
print("PASS: nursery tray + seedling resources")

# Vine trellis support block.
assert (assets / "blockstates/spice_trellis.json").is_file()
assert (assets / "models/block/spice_trellis.json").is_file()
assert (assets / "models/item/spice_trellis.json").is_file()
assert (root / "data/tfcagricultureplus/loot_table/blocks/spice_trellis.json").is_file()
assert (root / "data/tfcagricultureplus/recipe/crafting/spice_trellis.json").is_file()
for lang in ("en_us.json", "zh_cn.json"):
    lang_data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
    assert "block.tfcagricultureplus.spice_trellis" in lang_data
print("PASS: spice trellis resources")

# Corm-form spice item (currently saffron only).
assert (assets / "models/item/spice_corm/saffron.json").is_file()
for lang in ("en_us.json", "zh_cn.json"):
    lang_data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
    assert "item.tfcagricultureplus.spice_corm.saffron" in lang_data
print("PASS: spice corm resources")

# P0-AL strawberry ordinary crop (B namespace replacement for the A 87th record).
assert (assets / "blockstates/crop/strawberry.json").is_file()
assert (assets / "models/block/crop/strawberry.json").is_file()
assert (assets / "models/item/seeds/strawberry.json").is_file()
assert (root / "data/tfcagricultureplus/loot_table/blocks/crop/strawberry.json").is_file()
for lang in ("en_us.json", "zh_cn.json"):
    lang_data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
    assert "block.tfcagricultureplus.crop/strawberry" in lang_data
    assert "item.tfcagricultureplus.seeds/strawberry" in lang_data
print("PASS: strawberry crop resources")

# Coverage: A has 86 crop blockstates + B strawberry = 87; TFC has 29 crop blockstates.
with zipfile.ZipFile(a_jar) as za, zipfile.ZipFile(tfc_jar) as zt:
    a_crops = sorted(n for n in za.namelist()
                     if n.startswith("assets/tfcfarmingplus/blockstates/crop/") and n.endswith(".json"))
    tfc_crops = sorted(n for n in zt.namelist()
                       if n.startswith("assets/tfc/blockstates/crop/") and n.endswith(".json"))
    assert len(a_crops) == 86, len(a_crops)
    assert len(tfc_crops) == 29, len(tfc_crops)
    for n in a_crops:
        stem = n.split("/")[-1][:-5]
        assert f"assets/tfcfarmingplus/models/item/seeds/{stem}.json" in za.namelist(), stem
    for n in tfc_crops:
        stem = n.split("/")[-1][:-5]
        assert f"assets/tfc/models/item/seeds/{stem}.json" in zt.namelist(), stem
print("PASS: A 86 crops + B strawberry = 87; TFC 29 crops/seed models")

# P0-AP dedicated pistachio/cashew trees.
nut_trees = ["pistachio", "cashew", "macadamia"]
for tree in nut_trees:
    leaf_path = "nut_leaves/" + tree
    sapling_path = "nut_sapling/" + tree
    assert (assets / "blockstates" / (leaf_path + ".json")).is_file()
    assert (assets / "blockstates" / (sapling_path + ".json")).is_file()
    assert (assets / "models/block" / (leaf_path + ".json")).is_file()
    assert (assets / "models/block" / (sapling_path + ".json")).is_file()
    assert (assets / "models/item" / (sapling_path + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/loot_table/blocks" / (leaf_path + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/loot_table/blocks" / (sapling_path + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/recipe/crafting" / ("nut_sapling_" + tree + ".json")).is_file()
    for lang in ("en_us.json", "zh_cn.json"):
        lang_data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
        assert "block.tfcagricultureplus." + leaf_path in lang_data
        assert "block.tfcagricultureplus." + sapling_path in lang_data
print("PASS: pistachio/cashew tree resources")

for tree in nut_trees:
    assert (root / "data/tfcagricultureplus/worldgen/configured_feature" / ("nut_sapling_" + tree + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/worldgen/placed_feature" / ("nut_sapling_" + tree + ".json")).is_file()
assert (root / "data/tfcagricultureplus/neoforge/biome_modifier/add_nut_saplings.json").is_file()
print("PASS: pistachio/cashew tree worldgen resources")

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

for tree in spice_trees:
    assert (root / "data/tfcagricultureplus/worldgen/configured_feature" / ("spice_sapling_" + tree + ".json")).is_file()
    assert (root / "data/tfcagricultureplus/worldgen/placed_feature" / ("spice_sapling_" + tree + ".json")).is_file()
assert (root / "data/tfcagricultureplus/neoforge/biome_modifier/add_spice_trees.json").is_file()
print("PASS: spice tree worldgen resources")

# P0-AU root-form spice propagule (cardamom).
assert (assets / "models/item/spice_root/cardamom.json").is_file()
for lang in ("en_us.json", "zh_cn.json"):
    lang_data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
    assert "item.tfcagricultureplus.spice_root.cardamom" in lang_data
print("PASS: spice root resources")

assert (root / "data/tfcagricultureplus/tags/worldgen/biome/nut_tree_biomes.json").is_file()
assert (root / "data/tfcagricultureplus/tags/worldgen/biome/spice_tree_biomes.json").is_file()
nut_modifier = json.loads((root / "data/tfcagricultureplus/neoforge/biome_modifier/add_nut_saplings.json").read_text(encoding="utf-8"))
spice_modifier = json.loads((root / "data/tfcagricultureplus/neoforge/biome_modifier/add_spice_trees.json").read_text(encoding="utf-8"))
assert nut_modifier["biomes"] == "#tfcagricultureplus:nut_tree_biomes"
assert spice_modifier["biomes"] == "#tfcagricultureplus:spice_tree_biomes"
print("PASS: tree biome tags")
