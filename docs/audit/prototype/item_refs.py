import pathlib, json, re

root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data"

# item model paths -> item ids
items = set()
for p in (assets / "models/item").rglob("*.json"):
    rel = p.relative_to(assets / "models/item").with_suffix("")
    items.add("tfcagricultureplus:" + str(rel).replace("\\", "/"))

# collect all text references in data + assets except item models/lang
blob_files = []
for p in data.rglob("*.json"):
    blob_files.append(p)
for p in (assets / "blockstates").rglob("*.json"):
    blob_files.append(p)
for p in (assets / "models/block").rglob("*.json"):
    blob_files.append(p)
for p in (assets / "lang").glob("*.json"):
    blob_files.append(p)

blob = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in blob_files)
refs = {}
for item in sorted(items):
    refs[item] = blob.count(item)

print("item models", len(items))
zero = [i for i, c in refs.items() if c == 0]
print("zero references", len(zero))
for i in zero[:100]:
    print("ZERO", i)
