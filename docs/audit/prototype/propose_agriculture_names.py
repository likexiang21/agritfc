import json
import re
from pathlib import Path

lang_path = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang/zh_cn.json")
lang = json.loads(lang_path.read_text(encoding="utf-8"))
a_food = json.loads(Path("mod_rebuild/docs/audit/prototype/a_food_names.json").read_text(encoding="utf-8"))

# Fully curated crop/berry display names. A food names are used where they are correct.
manual_crops = {
    "cabbage": "卷心菜", "strawberry": "草莓", "beet": "甜菜", "carrot": "胡萝卜",
    "garlic": "大蒜", "onion": "洋葱", "potato": "土豆", "pumpkin": "南瓜",
    "radish": "萝卜", "soybean": "大豆", "squash": "西葫芦", "tomato": "番茄",
    "red_bell_pepper": "红甜椒", "yellow_bell_pepper": "黄甜椒", "melon": "甜瓜",
    "green_bean": "四季豆", "lentil": "兵豆", "peanut": "花生", "cassava": "木薯",
    "winter_melon": "冬瓜", "bottle_gourd": "瓠瓜", "cantaloupe": "哈密瓜",
}
berry = {
    "blackberry": "黑莓", "blueberry": "蓝莓", "bunchberry": "御膳橘",
    "cloudberry": "云莓", "cranberry": "蔓越莓", "elderberry": "接骨木莓",
    "gooseberry": "醋栗", "raspberry": "树莓", "snowberry": "雪果",
    "wintergreen": "冬青",
}
grain = {
    "millet": "黍", "foxtail_millet": "谷子", "fonio": "福尼奥米",
    "spelt": "斯佩耳特麦", "emmer": "二粒麦", "einkorn": "单粒麦",
    "pearl_millet": "珍珠粟", "finger_millet": "穇子", "sorghum": "高粱",
    "jobs_tears": "薏苡", "barley": "大麦", "oat": "燕麦", "rice": "水稻",
    "rye": "黑麦", "wheat": "小麦", "maize": "玉米",
}
spice = {
    "basil": "罗勒", "bay_laurel": "月桂", "black_pepper": "黑胡椒",
    "cardamom": "小豆蔻", "cilantro": "芫荽", "cumin": "孜然",
    "dill": "莳萝", "fennel": "茴香", "mustard": "芥菜", "oregano": "牛至",
    "rosemary": "迷迭香", "saffron": "藏红花", "sage": "鼠尾草",
    "thyme": "百里香", "vanilla": "香荚兰", "cinnamon": "肉桂",
    "clove": "丁香", "nutmeg": "肉豆蔻", "pimento": "多香果", "star_anise": "八角",
}
nut = {
    "acorn": "橡子", "chestnut": "栗子", "pine_nut": "松子",
    "hickory_nut": "山核桃", "beechnut": "山毛榉坚果",
    "pistachio": "开心果", "cashew": "腰果", "macadamia": "夏威夷果",
}
nut_tree = {"pistachio": "开心果", "cashew": "腰果", "macadamia": "夏威夷果"}
spice_tree = {"pimento": "多香果", "cinnamon": "肉桂", "clove": "丁香", "nutmeg": "肉豆蔻", "star_anise": "八角"}

def crop_name(species):
    return manual_crops.get(species) or a_food.get(species)

proposal = {}
missing = []
for key in lang:
    if key.startswith("item.tfcagricultureplus.crop_waste."):
        species = key.split(".")[-1]
        name = crop_name(species)
        if not name:
            missing.append(("crop_waste", species)); continue
        proposal[key] = f"{name}废枝叶"
    elif key.startswith("item.tfcagricultureplus.spice_waste."):
        species = key.split(".")[-1]
        proposal[key] = f"{spice[species]}废枝叶"
    elif key.startswith("item.tfcagricultureplus.bush_waste."):
        species = key.split(".")[-1]
        proposal[key] = f"{berry[species]}灌木废枝"
    elif key.startswith("item.tfcagricultureplus.grain_bundle."):
        species = key.split(".")[-1]
        proposal[key] = f"{grain[species]}捆"
    elif key.startswith("item.tfcagricultureplus.spice_seed."):
        species = key.split(".")[-1]
        proposal[key] = f"{spice[species]}种子"
    elif key.startswith("item.tfcagricultureplus.spice."):
        species = key.split(".")[-1]
        proposal[key] = spice[species]
    elif key.startswith("item.tfcagricultureplus.ground_spice."):
        species = key.split(".")[-1]
        proposal[key] = f"{spice[species]}粉"
    elif key.startswith("item.tfcagricultureplus.ground_nut."):
        species = key.split(".")[-1]
        proposal[key] = f"{nut[species]}粉"
    elif key.startswith("item.tfcagricultureplus.nut_shell."):
        species = key.split(".")[-1]
        proposal[key] = f"{nut[species]}壳"
    elif key.startswith("item.tfcagricultureplus.nut_sapling."):
        species = key.split(".")[-1]
        proposal[key] = f"{nut_tree[species]}树苗"
    elif key.startswith("block.tfcagricultureplus.nut_sapling."):
        species = key.split(".")[-1]
        proposal[key] = f"{nut_tree[species]}树苗"
    elif key.startswith("block.tfcagricultureplus.nut_leaves."):
        species = key.split(".")[-1]
        proposal[key] = f"{nut_tree[species]}树叶"
    elif key.startswith("item.tfcagricultureplus.spice_sapling."):
        species = key.split(".")[-1]
        proposal[key] = f"{spice_tree[species]}树苗"
    elif key.startswith("block.tfcagricultureplus.spice_sapling."):
        species = key.split(".")[-1]
        proposal[key] = f"{spice_tree[species]}树苗"
    elif key.startswith("block.tfcagricultureplus.spice_leaves."):
        species = key.split(".")[-1]
        proposal[key] = f"{spice_tree[species]}树叶"
    elif key.startswith("item.tfcagricultureplus.nut."):
        species = key.split(".")[-1]
        proposal[key] = nut[species]

Path("mod_rebuild/docs/audit/prototype/agriculture_name_proposal.json").write_text(
    json.dumps({"names": proposal, "missing": missing}, ensure_ascii=False, indent=2), encoding="utf-8")
print("mapped", len(proposal), "missing", missing)
print("sample")
for k in list(proposal)[:15]:
    print(k, "=", proposal[k])
