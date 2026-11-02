import pathlib
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus")
for key in ("crop_waste", "bush_waste", "nut_shell", "wet_grass"):
    print("====", key)
    for p in base.rglob("*.json"):
        if "lang" in p.parts: continue
        s = p.read_text(encoding="utf-8", errors="ignore")
        if key in s:
            print(p.relative_to(base))
