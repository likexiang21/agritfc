import json
import pathlib

root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/tfc/food")
root.mkdir(parents=True, exist_ok=True)

nuts = ["acorn", "beechnut", "cashew", "chestnut", "hickory_nut", "macadamia", "pine_nut", "pistachio"]
mushrooms = ["oyster", "shiitake", "button", "enoki", "wood_ear", "reishi",
             "lions_mane", "maitake", "king_oyster", "shimeji", "turkey_tail",
             "porcini", "morel", "chanterelle", "black_truffle"]

def write(name, data):
    p = root / (name + ".json")
    p.write_text(json.dumps(data, ensure_ascii=False) + "\n", encoding="utf-8")
    print(p.name)

for nut in nuts:
    write(nut, {
        "decay_modifier": 1.2,
        "hunger": 4,
        "saturation": 0.5,
        "protein": 1.5,
        "ingredient": {"item": "tfcagricultureplus:" + nut},
    })
    write("ground_" + nut, {
        "decay_modifier": 1.0,
        "hunger": 2,
        "saturation": 0.5,
        "protein": 1.0,
        "ingredient": {"item": "tfcagricultureplus:ground_nut/" + nut},
    })

for mushroom in mushrooms:
    write("mushroom_" + mushroom, {
        "decay_modifier": 1.0,
        "hunger": 2,
        "saturation": 0.5,
        "protein": 1.0,
        "ingredient": {"item": "tfcagricultureplus:wild_mushroom/" + mushroom},
    })
