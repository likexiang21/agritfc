import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfc/patchouli_books/field_guide")
pages = {
    "en_us": [
        {"item": "tfcagricultureplus:debarked_log/oak", "title": "Debarked log",
         "text": "Strip the bark and bast from a compatible log. A full debarked log is the 4-unit input to the timber pile."},
        {"item": "tfcagricultureplus:debarked_half/oak", "title": "Half log",
         "text": "Split a debarked log into halves. A half counts as 2 units in a pile and is placed with the facing you choose."},
        {"item": "tfcagricultureplus:debarked_quarter/oak", "title": "Quarter log",
         "text": "Split a half into quarters. A quarter counts as 1 unit and is the smallest pile piece."},
        {"item": "tfcagricultureplus:bark/oak", "title": "Bark",
         "text": "Bark is a B-owned byproduct with its own fuel and compost uses; it is not the same item as TFC Woodworking bark."},
        {"item": "tfcagricultureplus:bast/oak", "title": "Bast",
         "text": "Bast is removed before splitting. It is a B-owned fiber byproduct; keep it for its own uses."},
    ],
    "zh_cn": [
        {"item": "tfcagricultureplus:debarked_log/oak", "title": "去木原木",
         "text": "先用斧去掉兼容原木的树皮和韧皮。完整去木原木在木料堆中占 4 单位。"},
        {"item": "tfcagricultureplus:debarked_half/oak", "title": "半木",
         "text": "把去木原木劈成两半。半木在木料堆中占 2 单位，朝向由放置时决定。"},
        {"item": "tfcagricultureplus:debarked_quarter/oak", "title": "四分木",
         "text": "再把半木劈成四分之一。四分木占 1 单位，是木料堆最小单位。"},
        {"item": "tfcagricultureplus:bark/oak", "title": "树皮",
         "text": "树皮是 B 自己的副产物，可作燃料/堆肥；不是 TFC Woodworking 的树皮物品。"},
        {"item": "tfcagricultureplus:bast/oak", "title": "韧皮",
         "text": "韧皮在劈木前取下，是 B 自己的纤维副产物；不要和 TFCW 的韧皮混用。"},
    ],
}
for lang, extra in pages.items():
    p = root / lang / "entries/agriculture_plus_woodwork/intro.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    existing = {page.get("item") for page in d["pages"] if page.get("type") == "patchouli:spotlight"}
    for page in extra:
        if page["item"] not in existing:
            d["pages"].append({"type": "patchouli:spotlight", **page})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("woodwork pages updated")
