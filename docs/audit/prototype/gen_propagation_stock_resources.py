import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe/crafting/propagation_stock")
models = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/item/propagation_stock")
lang_dir = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")

# species -> (crop/product source, zh base, en base)
entries = {
    "shallot": ("tfcfarmingplus:food/shallot", "红葱", "Shallot"),
    "garlic": ("tfc:food/garlic", "大蒜", "Garlic"),
    "taro": ("tfcfarmingplus:food/taro", "芋头", "Taro"),
    "water_chestnut": ("tfcfarmingplus:food/water_chestnut", "荸荠", "Water Chestnut"),
    "water_caltrop": ("tfcfarmingplus:food/water_caltrop", "菱角", "Water Caltrop"),
    "arrowhead": ("tfcfarmingplus:food/arrowhead", "慈菇", "Arrowhead"),
    "gorgon_nut": ("tfcfarmingplus:food/gorgon_nut", "芡实", "Gorgon Nut"),
    "sunchoke": ("tfcfarmingplus:food/sunchoke", "洋姜", "Sunchoke"),
    "yacon": ("tfcfarmingplus:food/yacon", "雪莲果", "Yacon"),
    "potato": ("tfc:food/potato", "土豆", "Potato"),
    "yam": ("tfcfarmingplus:food/yam", "山药", "Yam"),
    "ginger": ("tfcfarmingplus:food/ginger", "生姜", "Ginger"),
    "turmeric": ("tfcfarmingplus:food/turmeric", "姜黄", "Turmeric"),
    "lotus": ("tfcfarmingplus:food/lotus", "莲藕", "Lotus Root"),
    "artichoke": ("tfcfarmingplus:food/artichoke", "洋蓟", "Artichoke"),
    "cardoon": ("tfcfarmingplus:food/cardoon", "刺菜蓟", "Cardoon"),
    "rhubarb": ("tfcfarmingplus:food/rhubarb", "大黄", "Rhubarb"),
    "asparagus": ("tfcfarmingplus:food/asparagus", "芦笋", "Asparagus"),
    "chive": ("tfcfarmingplus:food/chive", "韭菜", "Chive"),
    "cassava": ("tfc:food/cassava", "木薯", "Cassava"),
    "strawberry": ("tfc:food/strawberry", "草莓", "Strawberry"),
}
suffix = {
    "CORM": ("种球", "Seed Corm"),
    "TUBER": ("种薯", "Seed Tuber"),
    "RHIZOME": ("种茎", "Seed Rhizome"),
    "CROWN": ("冠芽", "Crown Slip"),
    "DIVISION": ("分株苗", "Division Slip"),
    "RUNNER": ("匍匐茎苗", "Runner Slip"),
}
# method per species, mirroring CropPropagation
methods = {
    "shallot": "CORM", "garlic": "CORM", "taro": "CORM", "water_chestnut": "CORM",
    "water_caltrop": "CORM", "arrowhead": "CORM", "gorgon_nut": "CORM",
    "sunchoke": "TUBER", "yacon": "TUBER", "potato": "TUBER", "yam": "TUBER",
    "ginger": "RHIZOME", "turmeric": "RHIZOME", "lotus": "RHIZOME",
    "artichoke": "CROWN", "cardoon": "CROWN", "rhubarb": "CROWN", "asparagus": "CROWN",
    "chive": "DIVISION", "cassava": "DIVISION", "strawberry": "RUNNER",
}

for species, (product, zh_base, en_base) in entries.items():
    method = methods[species]
    recipe = {
        "type": "minecraft:crafting_shapeless",
        "category": "misc",
        "ingredients": [{"item": product}],
        "result": {"count": 2, "id": f"tfcagricultureplus:propagation_stock/{species}"},
    }
    p = base / f"{species}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(recipe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    texture = ("tfc:item/food/" + product.split("food/", 1)[1]) if product.startswith("tfc:") \
        else ("tfcfarmingplus:item/food/" + product.split("food/", 1)[1])
    model = {"parent": "minecraft:item/generated", "textures": {"layer0": texture}}
    mp = models / f"{species}.json"
    mp.parent.mkdir(parents=True, exist_ok=True)
    mp.write_text(json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

for lang, idx in (("zh_cn.json", 0), ("en_us.json", 1)):
    p = lang_dir / lang
    d = json.loads(p.read_text(encoding="utf-8"))
    for species, (_, zh_base, en_base) in entries.items():
        zh_suffix, en_suffix = suffix[methods[species]]
        d[f"item.tfcagricultureplus.propagation_stock.{species}"] = (
            f"{zh_base}{zh_suffix}" if idx == 0 else f"{en_base} {en_suffix}"
        )
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lang, len(d))
print("generated", len(entries), "stock entries")
