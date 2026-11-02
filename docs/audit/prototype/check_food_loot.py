import pathlib
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/loot_table/blocks")
for name in ("whole_pie", "cream_cake", "chocolate_cake", "whole_cheese", "butter_block", "jelly_block", "sugar_block"):
    p = base / (name + ".json")
    print(name, p.exists())
    if p.exists(): print(p.read_text(encoding="utf-8")[:500])
