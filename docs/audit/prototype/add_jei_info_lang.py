import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
info = {
    "cooking_pan": (
        "Place the pan above a lit TFC heat source, add plant oil, then up to eight ingredients. Stir with a metal spatula; take the dish with a plate.",
        "把炒锅放在点燃的 TFC 热源上方，先加植物油，再加入最多 8 种食材。用金属锅铲翻炒；用盘子取出成品。"
    ),
    "nursery_tray": (
        "Put an A/B seed in the tray, wait for a seedling, then transplant the seedling onto suitable farmland.",
        "把 A/B 种子放入育苗盘，等待幼苗，再把幼苗移栽到合适的耕地。"
    ),
    "mushroom_bag": (
        "Eleven mushroom species can be cultivated. Growth needs the species' temperature range; the bag has a limited number of uses.",
        "11 种蘑菇可人工栽培。生长需要该物种的温度范围；菌包有有限使用次数。"
    ),
    "silkworm_rack": (
        "A temperature-controlled silkworm rack: feed leaves, collect eggs, and process cocoons into silk.",
        "温控养蚕架：放入树叶喂养、收集蚕种，并把蚕茧加工成蚕丝。"
    ),
    "drying_rack": (
        "Holds one item. Supported drying recipes use weather and time; take the result when finished.",
        "可放置一件物品。支持的干燥配方会利用天气与时间；完成后取出产物。"
    ),
    "cutting_board": (
        "Used for cutting-board recipes. Place dough or ingredients on the board and follow the press/knead/confirm controls.",
        "用于案板配方。把面团或食材放在案板上，按提示进行按压/揉捏/确认。"
    ),
    "log_cutting_board": (
        "An early cutting board made from a log; usable before a saw is available.",
        "用原木制成的早期案板；在获得锯之前就能使用。"
    ),
    "knife_block": (
        "Stores up to nine knives/tools. Right-click with a tool to insert; empty-hand right-click takes one out.",
        "最多存放 9 把刀/工具。手持工具右键存入；空手右键取出一件。"
    ),
    "mortar": (
        "Put food in the mortar and grind it with a pestle. Grinding consumes pestle durability.",
        "把食材放入石臼，用石杵研磨。研磨会消耗石杵耐久。"
    ),
    "kitchen_storage": (
        "Kitchen furniture has different storage rules: counters hold anything, spice racks hold spices, food displays hold food, sinks hold fluid containers.",
        "厨房家具的储存规则不同：橱柜台面存放任意物品，香料架存放香料，食品展示柜存放食物，水槽柜存放流体容器。"
    ),
}

for lang, idx in (("zh_cn.json", 1), ("en_us.json", 0)):
    p = base / lang
    d = json.loads(p.read_text(encoding="utf-8"))
    for key, pair in info.items():
        d[f"jei.tfcagricultureplus.info.{key}"] = pair[idx]
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lang, len(d))
