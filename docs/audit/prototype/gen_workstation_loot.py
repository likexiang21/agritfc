import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/loot_table/blocks")
base.mkdir(parents=True, exist_ok=True)

TFC_WOODS = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow"]
AFC_WOODS = ["araucaria","baobab","beech","cypress","eucalyptus","fig","ginkgo","hevea","ipe","ironwood","mahoe","mahogany","teak","tualang"]
ROCKS = ["andesite","basalt","chalk","chert","claystone","conglomerate","dacite","diorite","dolomite","gabbro","gneiss","granite","limestone","marble","phyllite","quartzite","rhyolite","schist","shale","slate","tuff"]
MORTAR_ROCKS = ["basalt","andesite","dacite","rhyolite","granite","diorite","gabbro","tuff","gneiss","schist","phyllite","slate","marble","quartzite","chert"]

def loot(block_id):
    return {
        "type": "minecraft:block",
        "pools": [{
            "rolls": 1,
            "bonus_rolls": 0,
            "entries": [{"type": "minecraft:item", "name": block_id}],
            "conditions": [{"condition": "minecraft:survives_explosion"}],
        }],
    }

def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

written = 0
for wood in TFC_WOODS + AFC_WOODS:
    for kind in ("log_cutting_board", "cutting_board", "knife_block", "drying_rack"):
        write(base / kind / f"{wood}.json", loot(f"tfcagricultureplus:{kind}/{wood}"))
        written += 1
for rock in ROCKS:
    write(base / "cutting_board" / f"{rock}.json", loot(f"tfcagricultureplus:cutting_board/{rock}"))
    written += 1
for rock in MORTAR_ROCKS:
    write(base / "mortar" / f"{rock}.json", loot(f"tfcagricultureplus:mortar/{rock}"))
    written += 1
write(base / "cooking_pan.json", loot("tfcagricultureplus:cooking_pan")); written += 1
write(base / "lumber_pile.json", loot("tfcagricultureplus:lumber_pile")); written += 1
print("loot files written", written)
