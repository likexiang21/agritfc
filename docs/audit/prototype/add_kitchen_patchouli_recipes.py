import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfc/patchouli_books/field_guide")
recipes = {
    "counter_cabinet": ("tfcagricultureplus:kitchen/counter_cabinet/oak", "Counter cabinet: 8 lumber in a 3×3 ring with an open centre.", "橱柜：8 份木材围成 3×3 外圈，中间留空。"),
    "half_cabinet": ("tfcagricultureplus:kitchen/half_cabinet/oak", "Half cabinet: 5 lumber, two rows with an open bottom row.", "半高柜：5 份木材，两行，底行留空。"),
    "sink_cabinet": ("tfcagricultureplus:kitchen/sink_cabinet/oak", "Sink cabinet: 8 lumber around a wrought iron sheet; holds 4000 mB water.", "水槽柜：8 份木材围住 1 张锻铁板；可存 4000 mB 水。"),
    "spice_rack": ("tfcagricultureplus:kitchen/spice_rack/oak", "Spice rack: 3 lumber and 2 rods; stores only the spice tag.", "香料架：3 份木材 + 2 根木棍；只存香料标签物品。"),
    "food_display": ("tfcagricultureplus:kitchen/food_display/oak", "Food display: 8 lumber around glass; stores only food.", "食品展示柜：8 份木材围住玻璃；只存食物。"),
    "fruit_bowl": ("tfcagricultureplus:kitchen/fruit_bowl/oak", "Fruit bowl: 5 lumber in a bowl pattern; stores one food item.", "果盘：5 份木材组成浅碗；只存 1 个食物。"),
}
for lang, idx in (("en_us", 0), ("zh_cn", 1)):
    p = root / lang / "entries/agriculture_plus_kitchen/intro.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    existing = {page.get("recipe") for page in d["pages"] if page.get("type") == "patchouli:crafting"}
    for key, (rid, en, zh) in recipes.items():
        if rid not in existing:
            d["pages"].append({"type": "patchouli:crafting", "recipe": rid, "text": en if idx == 0 else zh})
    # spotlight metal can + plate once
    spot = [
        {"type": "patchouli:spotlight", "item": "tfcagricultureplus:metal_can/copper", "title": "Metal can" if idx == 0 else "金属罐",
         "text": ("A 500 mB can; its icon shows the stored fluid. Fill/drain with a bucket, jug or other fluid container." if idx == 0 else "500 mB 金属罐；图标显示装入的液体。可用桶/罐等流体容器装入或倒出。")},
        {"type": "patchouli:spotlight", "item": "tfcagricultureplus:plate/ceramic", "title": "Serving plate" if idx == 0 else "陶盘",
         "text": ("A fired clay plate for pan dishes. Knap an unfired plate, fire it, then place it; the plate stores the dish." if idx == 0 else "烧制陶盘，用于盛装炒锅菜品。先打制未烧陶盘，烧制后放置；盘子会保存菜品。")},
    ]
    existing_items = {page.get("item") for page in d["pages"] if page.get("type") == "patchouli:spotlight"}
    for page in spot:
        if page["item"] not in existing_items:
            d["pages"].append(page)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("kitchen pages updated")
