import pathlib
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus")
for key in ("ground_spice", "spice/", "nut/", "ground_nut", "mushroom"):
    print("====", key)
    count=0
    for p in base.rglob("*.json"):
        s=p.read_text(encoding="utf-8", errors="ignore")
        if key in s:
            count += 1
            if count <= 12: print(p.relative_to(base))
    print("files",count)
