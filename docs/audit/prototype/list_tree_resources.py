import pathlib
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus")
for d in ("loot_table", "recipe"):
    p = base / d
    print("===", d)
    if p.exists():
        for f in p.rglob("*.json"):
            n = f.name.lower()
            if any(k in n for k in ("spice", "sapling", "nut")):
                print(f.relative_to(base))
