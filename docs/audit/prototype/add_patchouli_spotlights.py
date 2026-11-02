import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfc/patchouli_books/field_guide")
spotlights = {
    "en_us": {
        "crops/overview": [{
            "type": "patchouli:spotlight", "item": "tfcagricultureplus:crop_waste/spinach",
            "title": "Crop waste", "text": "Crop waste is a real byproduct, not a second seed. It is used as compost green or animal feed where supported."}],
        "crops/nursery": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:nursery_tray",
             "title": "Nursery tray", "text": "The tray is the A/B seed propagation station. TFC seeds do not need it."},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:seedling",
             "title": "Seedling", "text": "Take the seedling out of the tray, then transplant it onto valid farmland."}],
        "crops/grain": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:grain_bundle/wheat",
             "title": "Grain bundle", "text": "The bundle is the intermediate drop. Thresh it with a knife for grain and wet grass."},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:wet_grass",
             "title": "Wet grass", "text": "Dry wet grass to obtain straw; it is also a medium compost green."}],
        "crops/spices": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:spice/basil",
             "title": "Spice product", "text": "Mature spices drop their product. Grind it in the stone mortar."},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:ground_spice/basil",
             "title": "Ground spice", "text": "Ground spices are the seasoning input for the pan."}],
        "crops/nuts": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:pistachio",
             "title": "Nut", "text": "Ripe nut leaves drop nuts and shells seasonally."},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:nut_sapling/pistachio",
             "title": "Nut sapling", "text": "Plant the sapling to grow the tree; leaves carry nut_state."}],
        "crops/mushrooms": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:mushroom_bag",
             "title": "Mushroom bag", "text": "Only the eleven cultivable species grow in the bag."},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:wild_mushroom/oyster",
             "title": "Wild mushroom", "text": "Wild species grow/spread on compatible soil; natural-only species reject the bag."}],
        "crops/bushes": [{
            "type": "patchouli:spotlight", "item": "tfcagricultureplus:bush_waste/blackberry",
            "title": "Bush waste", "text": "Ten TFC bushes produce their own waste; the bush is left in its picked state."}],
    },
    "zh_cn": {
        "crops/overview": [{
            "type": "patchouli:spotlight", "item": "tfcagricultureplus:crop_waste/spinach",
            "title": "作物废枝叶", "text": "废枝叶是实际副产物，不是第二份种子；可作堆肥绿料或饲料。"}],
        "crops/nursery": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:nursery_tray",
             "title": "育苗盘", "text": "育苗盘是 A/B 种子的培育设备；TFC 种子不需要。"},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:seedling",
             "title": "幼苗", "text": "从育苗盘取出幼苗，再移栽到合适耕地。"}],
        "crops/grain": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:grain_bundle/wheat",
             "title": "谷物捆", "text": "谷物捆是中间掉落；用刀脱粒得到谷粒与湿草。"},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:wet_grass",
             "title": "湿草", "text": "湿草干燥后得到稻草，也可作中级堆肥绿料。"}],
        "crops/spices": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:spice/basil",
             "title": "香料产物", "text": "成熟香料掉落产物；用石臼研磨。"},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:ground_spice/basil",
             "title": "香料粉", "text": "香料粉是炒锅的调味输入。"}],
        "crops/nuts": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:pistachio",
             "title": "坚果", "text": "成熟树叶按季节掉落坚果与果壳。"},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:nut_sapling/pistachio",
             "title": "坚果幼苗", "text": "种下幼苗长成树；树叶带 nut_state。"}],
        "crops/mushrooms": [
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:mushroom_bag",
             "title": "菌包", "text": "只有 11 种可栽培蘑菇能在菌包中生长。"},
            {"type": "patchouli:spotlight", "item": "tfcagricultureplus:wild_mushroom/oyster",
             "title": "野生蘑菇", "text": "野生种在兼容土壤生长/扩散；仅自然生成种会拒绝菌包。"}],
        "crops/bushes": [{
            "type": "patchouli:spotlight", "item": "tfcagricultureplus:bush_waste/blackberry",
            "title": "灌木废枝", "text": "10 种 TFC 灌木各有废枝；采收后保留采摘状态。"}],
    },
}

for lang, entries in spotlights.items():
    for rel, pages in entries.items():
        p = root / lang / "entries" / (rel + ".json")
        d = json.loads(p.read_text(encoding="utf-8"))
        existing = {page.get("item") for page in d["pages"] if page.get("type") == "patchouli:spotlight"}
        for page in pages:
            if page["item"] not in existing:
                d["pages"].append(page)
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("spotlight pages added")
