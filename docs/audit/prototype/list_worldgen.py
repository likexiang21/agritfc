import pathlib
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data")
for ns in ("tfcagricultureplus",):
    p = base / ns
    for sub in ("worldgen", "neoforge", "tags/worldgen"):
        q = p / sub
        print("===", q, q.exists())
        if q.exists():
            for f in q.rglob("*"):
                if f.is_file():
                    print(f.relative_to(base))
