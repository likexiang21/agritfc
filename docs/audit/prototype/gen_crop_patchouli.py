import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfc/patchouli_books/field_guide")

category = {
    "en_us": {
        "name": "Agriculture Plus: Crops",
        "description": "B crop harvesting, nursery, grain, spices, nuts, mushrooms and TFC bushes.",
        "icon": "tfcagricultureplus:crop/strawberry",
        "sortnum": 24,
    },
    "zh_cn": {
        "name": "农业扩展：作物",
        "description": "B 的作物收获、育苗、谷物、香料、坚果、蘑菇与 TFC 灌木。",
        "icon": "tfcagricultureplus:crop/strawberry",
        "sortnum": 24,
    },
}

entries = {
    "crops/overview": {
        "en_us": {
            "name": "Harvest and waste",
            "icon": "tfcagricultureplus:crop/strawberry",
            "pages": [
                {"type": "patchouli:text", "title": "Mature harvest", "text": "Break a mature A, TFC or B crop with any tool. B replaces the default drop with a unified result:$(br2)$(li)seeds are returned;$(li)the crop product is retained;$(li)crop waste is added where the species defines it.$(br2)Immature crops do not drop products or seeds."},
                {"type": "patchouli:text", "title": "Double crops", "text": "For two-block crops, breaking either half clears the other half first. The same result is produced once, not twice."},
                {"type": "patchouli:text", "title": "Creative mode", "text": "In creative mode the block is removed without drops. Survival-only crop waste and seed return are not injected into the creative inventory."},
            ],
        },
        "zh_cn": {
            "name": "收获与废枝叶",
            "icon": "tfcagricultureplus:crop/strawberry",
            "pages": [
                {"type": "patchouli:text", "title": "成熟收获", "text": "用任意工具破坏成熟的 A/TFC/B 作物。B 会把默认掉落替换为统一结果：$(br2)$(li)返还种子；$(li)保留作物产品；$(li)按物种追加作物废枝叶。$(br2)未成熟作物不掉产品，也不掉种子。"},
                {"type": "patchouli:text", "title": "双格作物", "text": "双格作物破坏任意一半时，会先清理另一半；最终结果只结算一次，不会双倍掉落。"},
                {"type": "patchouli:text", "title": "创造模式", "text": "创造模式只移除方块，不产生掉落；作物废枝叶与种子返还不会进入创造背包。"},
            ],
        },
    },
    "crops/nursery": {
        "en_us": {
            "name": "Seeds and nursery",
            "icon": "tfcagricultureplus:nursery_tray",
            "pages": [
                {"type": "patchouli:text", "title": "Direct sowing", "text": "TFC seeds keep TFC's original direct sowing. A and B seeds are gated: right-clicking farmland with them shows the nursery hint instead of planting directly."},
                {"type": "patchouli:text", "title": "Nursery tray", "text": "Place an A or B seed in the nursery tray. The tray grows a seedling; take the seedling out when it is ready."},
                {"type": "patchouli:text", "title": "Transplant", "text": "Right-click suitable farmland with a seedling to plant it. The tray, seed and seedling keep their data across save and chunk reload."},
                {"type": "patchouli:text", "title": "Seed treatment", "text": "Seeds may carry one of three saved treatment states: soaked, germinated or dressed. The treatment is stored on the seed stack, not in a global player flag."},
            ],
        },
        "zh_cn": {
            "name": "种子与育苗",
            "icon": "tfcagricultureplus:nursery_tray",
            "pages": [
                {"type": "patchouli:text", "title": "直接播种", "text": "TFC 种子保留 TFC 原有的直接播种。A/B 种子会被拦截：对耕地右键时显示育苗提示，而不是直接种下。"},
                {"type": "patchouli:text", "title": "育苗盘", "text": "把 A/B 种子放入育苗盘。育苗盘会培育幼苗；成熟后取出幼苗。"},
                {"type": "patchouli:text", "title": "移栽", "text": "手持幼苗右键合适的耕地即可移栽。育苗盘、种子与幼苗的数据会随存档和区块重载保存。"},
                {"type": "patchouli:text", "title": "种子处理", "text": "种子可带三种已保存的处理状态：浸种、催芽、拌种。状态记录在种子物品上，不是全局玩家标记。"},
            ],
        },
    },
    "crops/grain": {
        "en_us": {
            "name": "Grain bundles and wet grass",
            "icon": "tfcagricultureplus:grain_bundle/wheat",
            "pages": [
                {"type": "patchouli:text", "title": "Why bundles", "text": "Grain crops drop a grain bundle instead of loose grain. The bundle is threshed with a knife to recover grain and wet grass."},
                {"type": "patchouli:text", "title": "Wet grass", "text": "Wet grass is a B item. Dry it on a drying rack or another supported drying recipe to obtain straw."},
                {"type": "patchouli:text", "title": "Grain list", "text": "Bundles exist for ten A grains (millet, foxtail millet, fonio, spelt, emmer, einkorn, pearl millet, finger millet, sorghum, Job's tears) and six TFC grains (barley, oat, rice, rye, wheat, maize)."},
                {"type": "patchouli:text", "title": "Uses", "text": "Grain keeps its normal food and recipe uses. Wet grass is accepted by medium compost greens. Bundles themselves are crafting intermediates, not food."},
            ],
        },
        "zh_cn": {
            "name": "谷物捆与湿草",
            "icon": "tfcagricultureplus:grain_bundle/wheat",
            "pages": [
                {"type": "patchouli:text", "title": "为什么有谷物捆", "text": "谷物成熟后掉落谷物捆，而不是直接掉散装谷粒。用刀脱粒可回收谷粒与湿草。"},
                {"type": "patchouli:text", "title": "湿草", "text": "湿草是 B 的物品。放在干燥架或其它支持的干燥配方上干燥，得到稻草。"},
                {"type": "patchouli:text", "title": "谷物清单", "text": "共有 10 种 A 谷物（黍、谷子、福尼奥米、斯佩耳特麦、二粒麦、单粒麦、珍珠粟、穇子、高粱、薏苡）与 6 种 TFC 谷物（大麦、燕麦、水稻、黑麦、小麦、玉米）的谷物捆。"},
                {"type": "patchouli:text", "title": "用途", "text": "谷粒保留原有食物与配方用途。湿草可进入中级堆肥绿料标签。谷物捆本身是制作中间物，不是食物。"},
            ],
        },
    },
    "crops/spices": {
        "en_us": {
            "name": "Spices",
            "icon": "tfcagricultureplus:spice/basil",
            "pages": [
                {"type": "patchouli:text", "title": "Two forms", "text": "B has fifteen crop-form spices and five tree-form spices. Crop spices are grown from spice seeds; tree spices grow from spice saplings."},
                {"type": "patchouli:text", "title": "Harvest", "text": "Mature crop spices are harvested like other crops. Tree spices drop their product from the leaves or trunk according to their species."},
                {"type": "patchouli:text", "title": "Propagation", "text": "Crop spices use corms or roots where the species requires them; tree spices use saplings. The trellis is a decoration/support block for the tree form."},
                {"type": "patchouli:text", "title": "Processing", "text": "Spice products are ground in a stone mortar into ground spice. Ground spices are the seasoning inputs for the pan and other kitchen recipes."},
            ],
        },
        "zh_cn": {
            "name": "香料",
            "icon": "tfcagricultureplus:spice/basil",
            "pages": [
                {"type": "patchouli:text", "title": "两种形态", "text": "B 有 15 种作物形态香料与 5 种树形态香料。作物香料由香料种子种出；树香料由香料树苗长成。"},
                {"type": "patchouli:text", "title": "收获", "text": "成熟作物香料按普通作物收获。树香料的产物按物种从树叶或树干掉落。"},
                {"type": "patchouli:text", "title": "繁殖", "text": "需要球茎或根部的作物香料使用对应繁殖材料；树香料使用树苗。香料支架是树形态的支撑/装饰方块。"},
                {"type": "patchouli:text", "title": "加工", "text": "香料产物用石臼研磨成香料粉。香料粉是炒锅与其它厨房配方的调味输入。"},
            ],
        },
    },
    "crops/nuts": {
        "en_us": {
            "name": "Nut trees and leaf states",
            "icon": "tfcagricultureplus:pistachio",
            "pages": [
                {"type": "patchouli:text", "title": "Three B nut trees", "text": "B adds pistachio, cashew and macadamia. Each has a sapling, leaves, nut and shell. Existing TFC and AFC nut leaves also receive the B nut state."},
                {"type": "patchouli:text", "title": "Leaf state", "text": "Leaves use four nut_state values:$(br2)$(li)0 = none;$(li)1 = flower;$(li)2 = green;$(li)3 = ripe.$(br2)Spring advances to flower, summer to green, autumn to ripe and winter clears the state."},
                {"type": "patchouli:text", "title": "Ripe drop", "text": "Ripe leaves occasionally drop one nut and one shell. The drop is seasonal; it does not happen outside the ripe state."},
            ],
        },
        "zh_cn": {
            "name": "坚果树与叶状态",
            "icon": "tfcagricultureplus:pistachio",
            "pages": [
                {"type": "patchouli:text", "title": "三种 B 坚果", "text": "B 新增开心果、腰果、夏威夷果。每种都有树苗、树叶、坚果与果壳。TFC/AFC 已有坚果树叶也会获得 B 的坚果叶状态。"},
                {"type": "patchouli:text", "title": "叶状态", "text": "树叶使用四个 nut_state 值：$(br2)$(li)0 = 无；$(li)1 = 花；$(li)2 = 青；$(li)3 = 成熟。$(br2)春季进入花，夏季青，秋季成熟，冬季清空。"},
                {"type": "patchouli:text", "title": "成熟掉落", "text": "成熟树叶偶尔掉落 1 个坚果与 1 个果壳。掉落只在成熟状态发生，具有季节性。"},
            ],
        },
    },
    "crops/mushrooms": {
        "en_us": {
            "name": "Wild mushrooms and bags",
            "icon": "tfcagricultureplus:mushroom_bag",
            "pages": [
                {"type": "patchouli:text", "title": "Fifteen species", "text": "B adds fifteen wild mushrooms. Eleven are cultivable in a mushroom bag; four are natural-only and reject the bag."},
                {"type": "patchouli:text", "title": "Wild growth", "text": "Wild mushrooms grow through three ages and can spread to nearby compatible soil. They need dirt, grass or another supported substrate."},
                {"type": "patchouli:text", "title": "Mushroom bag", "text": "The bag has four visible stages. It grows only within the species' temperature tolerance; below or above it, growth stops. A bag has a limited number of uses before it is spent."},
                {"type": "patchouli:text", "title": "Natural-only", "text": "Natural-only species are marked in the species registry. Right-clicking their bag input is rejected with a message; they cannot be cultivated."},
            ],
        },
        "zh_cn": {
            "name": "野生蘑菇与菌包",
            "icon": "tfcagricultureplus:mushroom_bag",
            "pages": [
                {"type": "patchouli:text", "title": "十五种", "text": "B 新增 15 种野生蘑菇。其中 11 种可用菌包栽培；4 种为仅自然生成，菌包会拒绝。"},
                {"type": "patchouli:text", "title": "野生生长", "text": "野生蘑菇有三个可见龄期，并可向附近兼容土壤扩散。需要泥土、草方块或其它支持的基质。"},
                {"type": "patchouli:text", "title": "菌包", "text": "菌包有四个可见阶段。只有处于该物种温度耐受范围内才会生长；过冷或过热都会停止。菌包有有限使用次数，耗尽后失效。"},
                {"type": "patchouli:text", "title": "仅自然生成", "text": "仅自然生成的物种在物种表中有标记。用菌包尝试栽培会被拒绝并提示；它们不能人工栽培。"},
            ],
        },
    },
    "crops/bushes": {
        "en_us": {
            "name": "TFC berry bushes",
            "icon": "tfcagricultureplus:bush_waste/blackberry",
            "pages": [
                {"type": "patchouli:text", "title": "Ten TFC bushes", "text": "B handles ten TFC berry bushes: blackberry, blueberry, bunchberry, cloudberry, cranberry, elderberry, gooseberry, raspberry, snowberry and wintergreen."},
                {"type": "patchouli:text", "title": "Harvest", "text": "Breaking a mature TFC bush is intercepted; the bush is harvested and left in its picked state instead of being removed. Empty-hand right-click harvesting is also handled."},
                {"type": "patchouli:text", "title": "Waste", "text": "Each bush yields its own bush waste item. These ten waste items are distinct from the 102 crop/spice waste items."},
            ],
        },
        "zh_cn": {
            "name": "TFC 浆果灌木",
            "icon": "tfcagricultureplus:bush_waste/blackberry",
            "pages": [
                {"type": "patchouli:text", "title": "十种 TFC 灌木", "text": "B 处理 10 种 TFC 浆果灌木：黑莓、蓝莓、御膳橘、云莓、蔓越莓、接骨木莓、醋栗、树莓、雪果、冬青。"},
                {"type": "patchouli:text", "title": "收获", "text": "破坏成熟 TFC 灌木会被拦截：采收后保留采摘状态，而不是直接移除。空手右键采收同样由 B 处理。"},
                {"type": "patchouli:text", "title": "废枝", "text": "每种灌木产出自己的灌木废枝。这 10 个废枝与 102 个作物/香料废枝叶是不同物品。"},
            ],
        },
    },
}

for lang in ("en_us", "zh_cn"):
    cat_path = root / lang / "categories" / "agriculture_plus_crops.json"
    cat_path.parent.mkdir(parents=True, exist_ok=True)
    cat_path.write_text(json.dumps(category[lang], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for rel, data in entries.items():
        entry = {
            "name": data[lang]["name"],
            "category": "tfc:agriculture_plus_crops",
            "icon": data[lang]["icon"],
            "pages": data[lang]["pages"],
        }
        p = root / lang / "entries" / (rel + ".json")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("written", len(entries) * 2 + 2, "patchouli files")
