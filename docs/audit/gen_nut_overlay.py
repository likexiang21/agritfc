import json, pathlib
root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
species = ["cashew", "macadamia", "pistachio"]
for sp in species:
    for state in (1, 2, 3):
        size = 0.8 + state * 0.25
        a = 7.5 - size + state * 0.3
        b = 8.5 + size - state * 0.3
        model = {
            "textures": {"nut": "tfcagricultureplus:item/bark/chestnut", "particle": "tfcagricultureplus:item/bark/chestnut"},
            "elements": [
                {"from": [a, 9.0, 4.0], "to": [b, 10.0, 5.0],
                 "faces": {d: {"texture": "#nut"} for d in ("down","up","north","south","west","east")}},
                {"from": [11.0, 7.0, 8.0], "to": [12.0, 8.0, 9.0],
                 "faces": {d: {"texture": "#nut"} for d in ("down","up","north","south","west","east")}},
                {"from": [4.0, 6.0, 10.0], "to": [5.0, 7.0, 11.0],
                 "faces": {d: {"texture": "#nut"} for d in ("down","up","north","south","west","east")}},
            ],
        }
        (root / f"models/block/nut_leaves/{sp}_fruit_{state}.json").write_text(json.dumps(model, indent=2) + "\n", encoding="utf-8")
    multipart = {"multipart": [
        {"apply": {"model": f"tfcagricultureplus:block/nut_leaves/{sp}"}},
        {"when": {"nut_state": "1"}, "apply": {"model": f"tfcagricultureplus:block/nut_leaves/{sp}_fruit_1"}},
        {"when": {"nut_state": "2"}, "apply": {"model": f"tfcagricultureplus:block/nut_leaves/{sp}_fruit_2"}},
        {"when": {"nut_state": "3"}, "apply": {"model": f"tfcagricultureplus:block/nut_leaves/{sp}_fruit_3"}},
    ]}
    (root / f"blockstates/nut_leaves/{sp}.json").write_text(json.dumps(multipart, indent=2) + "\n", encoding="utf-8")
print("generated nut overlays")
