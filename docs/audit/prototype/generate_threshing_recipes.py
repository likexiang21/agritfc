from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe/crafting")
root.mkdir(parents=True, exist_ok=True)
crops = [
    ("millet", "tfcfarmingplus:food/millet"),
    ("foxtail_millet", "tfcfarmingplus:food/foxtail_millet"),
    ("fonio", "tfcfarmingplus:food/fonio"),
    ("spelt", "tfcfarmingplus:food/spelt"),
    ("emmer", "tfcfarmingplus:food/emmer"),
    ("einkorn", "tfcfarmingplus:food/einkorn"),
    ("pearl_millet", "tfcfarmingplus:food/pearl_millet"),
    ("finger_millet", "tfcfarmingplus:food/finger_millet"),
    ("sorghum", "tfcfarmingplus:food/sorghum"),
    ("jobs_tears", "tfcfarmingplus:food/jobs_tears"),
    ("barley", "tfc:food/barley_grain"),
    ("oat", "tfc:food/oat_grain"),
    ("rice", "tfc:food/rice_grain"),
    ("rye", "tfc:food/rye_grain"),
    ("wheat", "tfc:food/wheat_grain"),
    ("maize", "tfc:food/maize_grain"),
]
for crop, grain in crops:
    data = {
        "type": "tfc:advanced_shapeless_crafting",
        "ingredients": [
            {"item": "tfcagricultureplus:grain_bundle/" + crop},
            {"tag": "c:tools/knife"},
        ],
        "primary_ingredient": {"tag": "c:tools/knife"},
        "remainder": {
            "modifiers": [
                {"type": "tfc:damage_crafting_remainder"},
                {
                    "type": "tfc:extra_products",
                    "stack": {"count": 1, "id": "tfcagricultureplus:wet_grass"},
                },
            ]
        },
        "result": {"stack": {"count": 1, "id": grain}},
    }
    path = root / ("grain_bundle_" + crop + ".json")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote {len(crops)} threshing recipe prototypes")
