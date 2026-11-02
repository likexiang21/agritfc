import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe/kitchen")
if base.exists():
    for p in base.rglob("*.json"):
        p.unlink()

TFC_WOODS = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow"]
AFC_WOODS = ["araucaria","baobab","beech","cypress","eucalyptus","fig","ginkgo","hevea","ipe","ironwood","mahoe","mahogany","teak","tualang"]

def shaped(pattern, key, result_id):
    return {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": key,
        "pattern": pattern,
        "result": {"count": 1, "id": result_id},
    }

for wood, namespace in [(w, "tfc") for w in TFC_WOODS] + [(w, "afc") for w in AFC_WOODS]:
    lumber = {"item": f"{namespace}:wood/lumber/{wood}"}
    rod = {"tag": "c:rods/wooden"}
    sheet = {"item": "tfc:metal/sheet/wrought_iron"}
    glass = {"item": "minecraft:glass"}
    recipes = {
        "counter_cabinet": shaped(["LLL", "L L", "LLL"], {"L": lumber},
            f"tfcagricultureplus:counter_cabinet/{wood}"),
        "half_cabinet": shaped(["LLL", "L L"], {"L": lumber},
            f"tfcagricultureplus:half_cabinet/{wood}"),
        "sink_cabinet": shaped(["LLL", "LML", "LLL"], {"L": lumber, "M": sheet},
            f"tfcagricultureplus:sink_cabinet/{wood}"),
        "spice_rack": shaped(["LLL", "R R"], {"L": lumber, "R": rod},
            f"tfcagricultureplus:spice_rack/{wood}"),
        "food_display": shaped(["LLL", "LGL", "LLL"], {"L": lumber, "G": glass},
            f"tfcagricultureplus:food_display/{wood}"),
        "fruit_bowl": shaped(["L L", "LLL"], {"L": lumber},
            f"tfcagricultureplus:fruit_bowl/{wood}"),
    }
    for family, recipe in recipes.items():
        p = base / family / f"{wood}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(recipe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("generated", len(list(base.rglob("*.json"))), "kitchen recipes")
