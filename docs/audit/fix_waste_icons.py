import json, pathlib
root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
textures = {
    "cocoa_branch": "firmalife:item/fruit_leaf",
    "cocoa_growing_branch": "firmalife:item/fruit_leaf",
    "cocoa_leaves": "firmalife:item/fruit_leaf",
    "cocoa_sapling": "firmalife:item/fruit_leaf",
    "fig_branch": "firmalife:item/fruit_leaf",
    "fig_growing_branch": "firmalife:item/fruit_leaf",
    "fig_leaves": "firmalife:item/fruit_leaf",
    "fig_sapling": "firmalife:item/fruit_leaf",
    "nightshade_bush": "firmalife:item/food/nightshade_berry",
    "pineapple_bush": "firmalife:item/food/pineapple",
    "wild_red_grapes": "firmalife:item/food/red_grapes",
    "wild_white_grapes": "firmalife:item/food/white_grapes",
    "grape_string_red": "firmalife:item/food/red_grapes",
    "grape_string_white": "firmalife:item/food/white_grapes",
}
for name, tex in textures.items():
    p = root / "models/item/crop_waste" / (name + ".json")
    p.write_text(json.dumps({"parent": "minecraft:item/generated",
                            "textures": {"layer0": tex}}, indent=2) + "\n", encoding="utf-8")

zh_names = {
    "cocoa_branch": "可可枝", "cocoa_growing_branch": "可可生枝", "cocoa_leaves": "可可叶",
    "cocoa_sapling": "可可树苗", "fig_branch": "无花果枝", "fig_growing_branch": "无花果生枝",
    "fig_leaves": "无花果叶", "fig_sapling": "无花果树苗", "nightshade_bush": "夜影灌木",
    "pineapple_bush": "菠萝灌木", "wild_red_grapes": "野生红葡萄",
    "wild_white_grapes": "野生白葡萄", "grape_string_red": "红葡萄藤",
    "grape_string_white": "白葡萄藤",
}
for name, cn in zh_names.items():
    for lang, value in (("en_us.json", None), ("zh_cn.json", cn + "废枝叶")):
        p = root / "lang" / lang
        data = json.loads(p.read_text(encoding="utf-8"))
        key = "item.tfcagricultureplus.crop_waste." + name
        if value is not None:
            data[key] = value
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("updated 14 waste icons and zh names")
