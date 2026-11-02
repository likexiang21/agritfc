import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfc/patchouli_books/field_guide")
repl = {
    "en_us": {
        "title": "Direct sowing and nursery",
        "text": "TFC seeds keep TFC direct sowing. A and B seeds follow their species propagation method:$(br2)$(li)seed-direct species can be sown on farmland normally;$(li)nursery, runner, tuber, rhizome, corm, crown and division species must go through the nursery tray.$(br2)The planted seed still needs a valid seedling transplant for non-direct species.",
    },
    "zh_cn": {
        "title": "直播与育苗",
        "text": "TFC 种子保留 TFC 直接播种。A/B 种子按物种繁殖方式处理：$(br2)$(li)种子直播型可直接种在耕地上；$(li)育苗、匍匐茎、块茎、根茎、球茎、冠芽、分株型必须经过育苗盘。$(br2)非直播型种子仍需育苗后移栽。",
    },
}
for lang, data in repl.items():
    p = root / lang / "entries/crops/nursery.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    d["pages"][0]["title"] = data["title"]
    d["pages"][0]["text"] = data["text"]
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("updated nursery pages")
