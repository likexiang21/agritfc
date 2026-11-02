import pathlib

root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data"
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/java")

items = set()
for p in (assets / "models/item").rglob("*.json"):
    rel = p.relative_to(assets / "models/item").with_suffix("")
    items.add("tfcagricultureplus:" + str(rel).replace("\\", "/"))

data_files = [p for p in data.rglob("*.json") if "lang" not in str(p)]
data_blob = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in data_files)
java_blob = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in base.rglob("*.java"))

rows = []
for item in sorted(items):
    dn = data_blob.count(item)
    jn = java_blob.count(item)
    if dn == 0 and jn == 0:
        rows.append((item, dn, jn))
print("items with no data/java refs", len(rows))
for r in rows:
    print(r)
