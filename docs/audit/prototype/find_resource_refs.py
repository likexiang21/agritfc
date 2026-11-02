import pathlib, json, re
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus")
for key in ("sawdust", "wet_grass", "bark", "bast", "silk", "silkworm", "cocoon", "adult_silkworm", "propagation_stock", "spice_corm", "spice_root", "nut_shell"):
    print("====", key)
    for p in base.rglob("*.json"):
        s = p.read_text(encoding="utf-8", errors="ignore")
        if key in s:
            rel = p.relative_to(base)
            print(rel)
