import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
info = {
    "metal_can": (
        "A 500 mB metal can made by anvil from a wrought iron sheet. It holds the fluids in its fluid tag and shows the contained fluid on its icon.",
        "500 mB 金属罐，由锻铁板在铁砧上锻造。可装其流体标签允许的液体，图标会显示装入的液体。"
    ),
    "serving_plate": (
        "Clay plates are knapped, fired and optionally dyed before firing. Place a plate to serve pan dishes; it stores the dish data.",
        "陶盘经打制、烧制，可在烧前染色。放置后用于盛装炒锅菜品；会保存菜品数据。"
    ),
    "propagation_stock": (
        "Vegetative planting stock: use on farmland or shallow water to plant the species at age 0. One crop product crafts into two stock.",
        "无性繁殖材料：对耕地或浅水使用可种下对应作物（age 0）。1 份作物产品可合成 2 个繁殖材料。"
    ),
}
for lang, idx in (("zh_cn.json", 1), ("en_us.json", 0)):
    p = base / lang
    d = json.loads(p.read_text(encoding="utf-8"))
    for key, pair in info.items():
        d[f"jei.tfcagricultureplus.info.{key}"] = pair[idx]
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lang, len(d))
