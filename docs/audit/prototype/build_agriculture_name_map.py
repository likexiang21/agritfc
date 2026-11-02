import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
zh = json.loads((base / "zh_cn.json").read_text(encoding="utf-8"))
en = json.loads((base / "en_us.json").read_text(encoding="utf-8"))
a = json.loads(Path("mod_rebuild/docs/audit/prototype/a_food_names_bilingual.json").read_text(encoding="utf-8"))

# Crop display names, curated on top of A's food item names.
manual_zh = {
    "cabbage": "卷心菜", "strawberry": "草莓", "beet": "甜菜", "carrot": "胡萝卜",
    "garlic": "大蒜", "onion": "洋葱", "potato": "土豆", "pumpkin": "南瓜",
    "radish": "萝卜", "soybean": "大豆", "squash": "西葫芦", "tomato": "番茄",
    "red_bell_pepper": "红甜椒", "yellow_bell_pepper": "黄甜椒", "melon": "甜瓜",
    "green_bean": "四季豆", "lentil": "兵豆", "peanut": "花生", "cassava": "木薯",
    "winter_melon": "冬瓜", "bottle_gourd": "瓠瓜", "cantaloupe": "哈密瓜", "hops": "啤酒花",
}
manual_en = {
    "cabbage": "Cabbage", "strawberry": "Strawberry", "beet": "Beet", "carrot": "Carrot",
    "garlic": "Garlic", "onion": "Onion", "potato": "Potato", "pumpkin": "Pumpkin",
    "radish": "Radish", "soybean": "Soybean", "squash": "Squash", "tomato": "Tomato",
    "red_bell_pepper": "Red Bell Pepper", "yellow_bell_pepper": "Yellow Bell Pepper",
    "melon": "Melon", "green_bean": "Green Bean", "lentil": "Lentil", "peanut": "Peanut",
    "cassava": "Cassava", "winter_melon": "Winter Melon", "bottle_gourd": "Bottle Gourd",
    "cantaloupe": "Cantaloupe", "hops": "Hops",
}

berry_zh = {"blackberry":"黑莓","blueberry":"蓝莓","bunchberry":"御膳橘","cloudberry":"云莓","cranberry":"蔓越莓","elderberry":"接骨木莓","gooseberry":"醋栗","raspberry":"树莓","snowberry":"雪果","wintergreen":"冬青"}
berry_en = {"blackberry":"Blackberry","blueberry":"Blueberry","bunchberry":"Bunchberry","cloudberry":"Cloudberry","cranberry":"Cranberry","elderberry":"Elderberry","gooseberry":"Gooseberry","raspberry":"Raspberry","snowberry":"Snowberry","wintergreen":"Wintergreen"}

grain_zh = {"millet":"黍","foxtail_millet":"谷子","fonio":"福尼奥米","spelt":"斯佩耳特麦","emmer":"二粒麦","einkorn":"单粒麦","pearl_millet":"珍珠粟","finger_millet":"穇子","sorghum":"高粱","jobs_tears":"薏苡","barley":"大麦","oat":"燕麦","rice":"水稻","rye":"黑麦","wheat":"小麦","maize":"玉米"}
grain_en = {"millet":"Millet","foxtail_millet":"Foxtail Millet","fonio":"Fonio","spelt":"Spelt","emmer":"Emmer","einkorn":"Einkorn","pearl_millet":"Pearl Millet","finger_millet":"Finger Millet","sorghum":"Sorghum","jobs_tears":"Job's Tears","barley":"Barley","oat":"Oat","rice":"Rice","rye":"Rye","wheat":"Wheat","maize":"Maize"}

spice_zh = {"basil":"罗勒","bay_laurel":"月桂","black_pepper":"黑胡椒","cardamom":"小豆蔻","cilantro":"芫荽","cumin":"孜然","dill":"莳萝","fennel":"茴香","mustard":"芥菜","oregano":"牛至","rosemary":"迷迭香","saffron":"藏红花","sage":"鼠尾草","thyme":"百里香","vanilla":"香荚兰","cinnamon":"肉桂","clove":"丁香","nutmeg":"肉豆蔻","pimento":"多香果","star_anise":"八角"}
spice_en = {"basil":"Basil","bay_laurel":"Bay Laurel","black_pepper":"Black Pepper","cardamom":"Cardamom","cilantro":"Cilantro","cumin":"Cumin","dill":"Dill","fennel":"Fennel","mustard":"Mustard","oregano":"Oregano","rosemary":"Rosemary","saffron":"Saffron","sage":"Sage","thyme":"Thyme","vanilla":"Vanilla","cinnamon":"Cinnamon","clove":"Clove","nutmeg":"Nutmeg","pimento":"Allspice","star_anise":"Star Anise"}

nut_zh = {"acorn":"橡子","chestnut":"栗子","pine_nut":"松子","hickory_nut":"山核桃","beechnut":"山毛榉坚果","pistachio":"开心果","cashew":"腰果","macadamia":"夏威夷果"}
nut_en = {"acorn":"Acorn","chestnut":"Chestnut","pine_nut":"Pine Nut","hickory_nut":"Hickory Nut","beechnut":"Beechnut","pistachio":"Pistachio","cashew":"Cashew","macadamia":"Macadamia"}
spice_tree_zh = {k: spice_zh[k] for k in ("pimento","cinnamon","clove","nutmeg","star_anise")}
spice_tree_en = {k: spice_en[k] for k in ("pimento","cinnamon","clove","nutmeg","star_anise")}

missing = []
map_zh, map_en = {}, {}

def crop(species, lang):
    return (manual_zh if lang == "zh" else manual_en).get(species) or (a["zh_cn" if lang == "zh" else "en_us"].get(species))

def put(key, zh_val, en_val):
    if key not in zh or key not in en:
        missing.append(key)
        return
    map_zh[key] = zh_val
    map_en[key] = en_val

for key in zh:
    for prefix, maker in (
        ("item.tfcagricultureplus.crop_waste.", "crop_waste"),
        ("item.tfcagricultureplus.spice_waste.", "spice_waste"),
        ("item.tfcagricultureplus.bush_waste.", "bush_waste"),
        ("item.tfcagricultureplus.grain_bundle.", "grain_bundle"),
        ("item.tfcagricultureplus.spice_seed.", "spice_seed"),
        ("item.tfcagricultureplus.spice.", "spice"),
        ("item.tfcagricultureplus.ground_spice.", "ground_spice"),
        ("item.tfcagricultureplus.ground_nut.", "ground_nut"),
        ("item.tfcagricultureplus.nut_shell.", "nut_shell"),
        ("item.tfcagricultureplus.nut_sapling/", "nut_sapling_item"),
        ("block.tfcagricultureplus.nut_sapling/", "nut_sapling_block"),
        ("block.tfcagricultureplus.nut_leaves/", "nut_leaves"),
        ("item.tfcagricultureplus.spice_sapling/", "spice_sapling_item"),
        ("block.tfcagricultureplus.spice_sapling/", "spice_sapling_block"),
        ("block.tfcagricultureplus.spice_leaves/", "spice_leaves"),
        ("block.tfcagricultureplus.spice_crop/", "spice_crop"),
    ):
        if not key.startswith(prefix):
            continue
        species = key[len(prefix):]
        if maker == "crop_waste":
            c_zh, c_en = crop(species, "zh"), crop(species, "en")
            if not c_zh or not c_en:
                missing.append((key, species)); break
            put(key, f"{c_zh}废枝叶", f"{c_en} Waste Leaves")
        elif maker == "spice_waste":
            put(key, f"{spice_zh[species]}废枝叶", f"{spice_en[species]} Waste Leaves")
        elif maker == "bush_waste":
            put(key, f"{berry_zh[species]}灌木废枝", f"{berry_en[species]} Bush Waste")
        elif maker == "grain_bundle":
            put(key, f"{grain_zh[species]}捆", f"{grain_en[species]} Bundle")
        elif maker == "spice_seed":
            put(key, f"{spice_zh[species]}种子", f"{spice_en[species]} Seeds")
        elif maker == "spice":
            put(key, spice_zh[species], spice_en[species])
        elif maker == "ground_spice":
            put(key, f"{spice_zh[species]}粉", f"Ground {spice_en[species]}")
        elif maker == "ground_nut":
            put(key, f"{nut_zh[species]}粉", f"Ground {nut_en[species]}")
        elif maker == "nut_shell":
            put(key, f"{nut_zh[species]}壳", f"{nut_en[species]} Shell")
        elif maker.startswith("nut_sapling"):
            put(key, f"{nut_zh[species]}树苗", f"{nut_en[species]} Sapling")
        elif maker == "nut_leaves":
            put(key, f"{nut_zh[species]}树叶", f"{nut_en[species]} Leaves")
        elif maker.startswith("spice_sapling"):
            put(key, f"{spice_tree_zh[species]}树苗", f"{spice_tree_en[species]} Sapling")
        elif maker == "spice_leaves":
            put(key, f"{spice_tree_zh[species]}树叶", f"{spice_tree_en[species]} Leaves")
        elif maker == "spice_crop":
            put(key, f"{spice_zh[species]}作物", f"{spice_en[species]} Crop")
        break

# Direct nut items
for key in zh:
    if key.startswith("item.tfcagricultureplus.") and key.count(".") == 2:
        species = key.rsplit(".", 1)[-1]
        if species in nut_zh:
            put(key, nut_zh[species], nut_en[species])

Path("mod_rebuild/docs/audit/prototype/agriculture_name_map.json").write_text(
    json.dumps({"zh": map_zh, "en": map_en, "missing": missing}, ensure_ascii=False, indent=2),
    encoding="utf-8")
print("mapped", len(map_zh), "missing", len(missing))
for m in missing[:10]:
    print("MISSING", m)
