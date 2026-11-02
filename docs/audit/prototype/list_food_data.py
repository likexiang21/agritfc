import pathlib
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data")
for p in base.rglob("*.json"):
    s=p.read_text(encoding="utf-8", errors="ignore")
    if "food" in str(p).lower() or "FoodData" in s:
        pass
print("food dirs/files")
for p in base.rglob("*.json"):
    if "food" in str(p).lower():
        print(p.relative_to(base))
