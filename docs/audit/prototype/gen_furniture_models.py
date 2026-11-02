import json
from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/block/kitchen_storage")

def faces():
    return {d: {"texture": "#all"} for d in ("north", "south", "east", "west", "up", "down")}

def box(fr, to):
    return {"from": list(fr), "to": list(to), "faces": faces()}

models = {
    "counter_cabinet": [box((0, 0, 0), (16, 13, 16)), box((0, 13, 0), (16, 16, 16))],
    "half_cabinet": [box((0, 0, 0), (16, 8, 16)), box((0, 8, 0), (16, 10, 16))],
    "sink_cabinet": [
        box((0, 0, 0), (16, 13, 16)),
        box((0, 13, 0), (16, 15, 2)), box((0, 13, 14), (16, 15, 16)),
        box((0, 13, 2), (2, 15, 14)), box((14, 13, 2), (16, 15, 14)),
        box((2, 13, 2), (14, 13.3, 14)),
    ],
    "spice_rack": [
        box((0, 0, 0), (16, 12, 2)), box((0, 0, 0), (2, 12, 16)), box((14, 0, 0), (16, 12, 16)),
        box((2, 4, 2), (14, 5, 14)), box((2, 9, 2), (14, 10, 14)),
    ],
    "food_display": [
        box((0, 0, 0), (16, 2, 16)), box((0, 2, 0), (2, 13, 16)), box((14, 2, 0), (16, 13, 16)),
        box((0, 2, 0), (16, 13, 2)), box((0, 2, 14), (16, 13, 16)),
        box((2, 7, 2), (14, 8, 14)), box((0, 13, 0), (16, 14, 16)),
    ],
    "fruit_bowl": [
        box((2, 0, 2), (14, 2, 14)),
        box((1, 2, 1), (2, 4, 15)), box((14, 2, 1), (15, 4, 15)),
        box((2, 2, 1), (14, 4, 2)), box((2, 2, 14), (14, 4, 15)),
        box((2, 2, 2), (14, 2.5, 14)),
    ],
}

for name, elements in models.items():
    p = base / f"{name}.json"
    p.write_text(json.dumps({"elements": elements}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", p)
