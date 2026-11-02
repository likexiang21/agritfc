import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
zh = json.loads((base / "zh_cn.json").read_text(encoding="utf-8"))
en = json.loads((base / "en_us.json").read_text(encoding="utf-8"))

TFC_WOODS = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow"]
AFC_WOODS = ["araucaria","baobab","beech","cypress","eucalyptus","fig","ginkgo","hevea","ipe","ironwood","mahoe","mahogany","teak","tualang"]
tfc_zh = json.loads(Path("mod_rebuild/docs/audit/prototype/wood_names.json").read_text(encoding="utf-8"))
wood_zh = {w: tfc_zh.get(w, "").replace("原木", "") for w in TFC_WOODS}
wood_zh.update({
    "araucaria":"南洋杉木","baobab":"猴面包木","beech":"山毛榉木","cypress":"柏木",
    "eucalyptus":"桉木","fig":"无花果木","ginkgo":"银杏木","hevea":"橡胶木",
    "ipe":"重蚁木","ironwood":"铁木","mahoe":"木槿木","mahogany":"桃花心木",
    "teak":"柚木","tualang":"塔朗木",
})
wood_en = {
    "acacia":"Acacia","ash":"Ash","aspen":"Aspen","birch":"Birch","blackwood":"Blackwood",
    "chestnut":"Chestnut","douglas_fir":"Douglas Fir","hickory":"Hickory","kapok":"Kapok",
    "mangrove":"Mangrove","maple":"Maple","oak":"Oak","palm":"Palm","pine":"Pine",
    "rosewood":"Rosewood","sequoia":"Sequoia","spruce":"Spruce","sycamore":"Sycamore",
    "white_cedar":"White Cedar","willow":"Willow","araucaria":"Araucaria","baobab":"Baobab",
    "beech":"Beech","cypress":"Cypress","eucalyptus":"Eucalyptus","fig":"Fig","ginkgo":"Ginkgo",
    "hevea":"Hevea","ipe":"Ipe","ironwood":"Ironwood","mahoe":"Mahoe","mahogany":"Mahogany",
    "teak":"Teak","tualang":"Tualang",
}

families_zh = {
    "log_cutting_board":"原木案板","cutting_board":"案板","knife_block":"刀具架",
    "drying_rack":"干燥架","fruit_bowl":"果盘","sink_cabinet":"水槽柜",
    "counter_cabinet":"橱柜台面","spice_rack":"香料架","half_cabinet":"半高柜",
    "food_display":"食品展示柜",
}
families_en = {
    "log_cutting_board":"Log Cutting Board","cutting_board":"Cutting Board","knife_block":"Knife Block",
    "drying_rack":"Drying Rack","fruit_bowl":"Fruit Bowl","sink_cabinet":"Sink Cabinet",
    "counter_cabinet":"Counter Cabinet","spice_rack":"Spice Rack","half_cabinet":"Half Cabinet",
    "food_display":"Food Display",
}
parts_zh = {"bark":"树皮","bast":"韧皮","debarked_log":"去皮原木","debarked_half":"半木","debarked_quarter":"四分木"}
parts_en = {"bark":"Bark","bast":"Bast","debarked_log":"Debarked Log","debarked_half":"Half Log","debarked_quarter":"Quarter Log"}

changed = 0
for wood, wz, we in [(w, wood_zh[w], wood_en[w]) for w in TFC_WOODS + AFC_WOODS]:
    for fam, fz in families_zh.items():
        k = f"block.tfcagricultureplus.{fam}.{wood}"
        if k in zh:
            zh[k] = f"{wz}{fz}"; en[k] = f"{we} {families_en[fam]}"; changed += 1
    for part, pz in parts_zh.items():
        k = f"block.tfcagricultureplus.{part}.{wood}"
        if k not in zh:
            k = f"item.tfcagricultureplus.{part}.{wood}"
        if k in zh:
            zh[k] = f"{wz}{pz}"; en[k] = f"{we} {parts_en[part]}"; changed += 1

for lang, key in (("zh_cn.json", "zh"), ("en_us.json", "en")):
    p = base / lang
    data = json.loads(p.read_text(encoding="utf-8"))
    data.update(zh if key == "zh" else en)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lang, "keys", len(data))
print("changed", changed)
