import pathlib
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/loot_table/blocks")
for d in ("spice_leaves", "nut_leaves", "spice_sapling", "nut_sapling"):
 p=base/d
 print(d, [f.name for f in p.glob("*.json")] if p.exists() else "MISSING")
