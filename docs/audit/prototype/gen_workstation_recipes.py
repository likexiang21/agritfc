import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe/workstations")
base.mkdir(parents=True, exist_ok=True)

TFC_WOODS = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow"]
AFC_WOODS = ["araucaria","baobab","beech","cypress","eucalyptus","fig","ginkgo","hevea","ipe","ironwood","mahoe","mahogany","teak","tualang"]
ROCKS = ["andesite","basalt","chalk","chert","claystone","conglomerate","dacite","diorite","dolomite","gabbro","gneiss","granite","limestone","marble","phyllite","quartzite","rhyolite","schist","shale","slate","tuff"]
MORTAR_ROCKS = ["basalt","andesite","dacite","rhyolite","granite","diorite","gabbro","tuff","gneiss","schist","phyllite","slate","marble","quartzite","chert"]

def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def shapeless_damage(ingredients, primary, result_id, count=1):
    return {
        "type": "tfc:advanced_shapeless_crafting",
        "ingredients": ingredients,
        "primary_ingredient": primary,
        "remainder": {"modifiers": [{"type": "tfc:damage_crafting_remainder"}]},
        "result": {"count": count, "id": result_id},
    }

def shaped(pattern, key, result_id, count=1):
    return {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": key,
        "pattern": pattern,
        "result": {"count": count, "id": result_id},
    }

for wood, namespace in [(w, "tfc") for w in TFC_WOODS] + [(w, "afc") for w in AFC_WOODS]:
    write(base / "log_cutting_board" / f"{wood}.json", shapeless_damage(
        [{"tag": "minecraft:axes"}, {"item": f"{namespace}:wood/log/{wood}"}],
        {"tag": "minecraft:axes"}, f"tfcagricultureplus:log_cutting_board/{wood}"))
    write(base / "cutting_board" / f"{wood}.json", shapeless_damage(
        [{"tag": "c:tools/saw"}] + [{"item": f"{namespace}:wood/lumber/{wood}"} for _ in range(4)],
        {"tag": "c:tools/saw"}, f"tfcagricultureplus:cutting_board/{wood}"))
    write(base / "knife_block" / f"{wood}.json", shaped(
        ["PPP", " S ", "PPP"],
        {"P": {"item": f"{namespace}:wood/lumber/{wood}"}, "S": {"tag": "c:rods/wooden"}},
        f"tfcagricultureplus:knife_block/{wood}"))
    write(base / "drying_rack" / f"{wood}.json", shaped(
        ["PPP", "S S", "S S"],
        {"P": {"item": f"{namespace}:wood/lumber/{wood}"}, "S": {"tag": "c:rods/wooden"}},
        f"tfcagricultureplus:drying_rack/{wood}"))

for rock in ROCKS:
    write(base / "cutting_board" / f"{rock}.json", shapeless_damage(
        [{"tag": "c:tools/hammer"}, {"item": f"tfc:rock/raw/{rock}"}],
        {"tag": "c:tools/hammer"}, f"tfcagricultureplus:cutting_board/{rock}"))

for rock in MORTAR_ROCKS:
    write(base / "mortar" / f"{rock}.json", shapeless_damage(
        [{"tag": "c:tools/hammer"}, {"item": f"tfc:rock/raw/{rock}"}, {"item": f"tfc:rock/raw/{rock}"}],
        {"tag": "c:tools/hammer"}, f"tfcagricultureplus:mortar/{rock}"))

write(base / "cooking_pan.json", shapeless_damage(
    [{"tag": "c:tools/hammer"}] + [{"item": "tfc:metal/sheet/wrought_iron"} for _ in range(3)],
    {"tag": "c:tools/hammer"}, "tfcagricultureplus:cooking_pan"))

write(base / "silkworm_rack.json", shaped(
    ["PPP", "S S", "P P"],
    {"P": {"item": "tfc:wood/lumber/oak"}, "S": {"tag": "c:rods/wooden"}},
    "tfcagricultureplus:silkworm_rack"))

print("generated recipes under", base)
