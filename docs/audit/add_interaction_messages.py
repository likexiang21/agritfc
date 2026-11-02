import json, pathlib
root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
keys = {
 "message.tfcagricultureplus.cutting_board.durability": ("Board durability: %s", "案板耐久：%s"),
 "message.tfcagricultureplus.cutting_board.occupied": ("Something is already on the board.", "案板上已有物品。"),
 "message.tfcagricultureplus.cutting_board.dough_controls": ("Use the dough controls first.", "请先处理面团。"),
 "message.tfcagricultureplus.cutting_board.dough_not_formed": ("The dough is not formed yet.", "面团尚未成型。"),
 "message.tfcagricultureplus.cutting_board.empty": ("The board is empty.", "案板是空的。"),
 "message.tfcagricultureplus.cutting_board.worn": ("The board is worn out.", "案板已磨损。"),
 "message.tfcagricultureplus.cutting_board.rotten": ("The food is rotten.", "食物已腐烂。"),
 "message.tfcagricultureplus.cutting_board.no_recipe": ("No cutting recipe for this item.", "该物品没有切配配方。"),
 "message.tfcagricultureplus.mortar.full": ("The mortar is full.", "石臼已满。"),
 "message.tfcagricultureplus.mortar.empty": ("The mortar is empty.", "石臼是空的。"),
 "message.tfcagricultureplus.mortar.rotten": ("The content is rotten.", "内容物已腐烂。"),
 "message.tfcagricultureplus.mortar.no_recipe": ("No grinding recipe for this item.", "该物品没有研磨配方。"),
 "message.tfcagricultureplus.mortar.progress": ("Grinding %s / %s", "研磨 %s / %s"),
}
for lang, idx in (("en_us.json", 0), ("zh_cn.json", 1)):
 p = root / lang
 data = json.loads(p.read_text(encoding="utf-8"))
 for key, pair in keys.items():
  data[key] = pair[idx]
 p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
 print(lang, len(data))
