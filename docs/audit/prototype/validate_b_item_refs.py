from pathlib import Path
import json
import re

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
valid = set()
for p in (assets / "models/item").rglob("*.json"):
    valid.add("tfcagricultureplus:" + p.relative_to(assets / "models/item").as_posix()[:-5])
for p in (assets / "blockstates").rglob("*.json"):
    rel = p.relative_to(assets / "blockstates").as_posix()[:-5]
    valid.add("tfcagricultureplus:" + rel)
    valid.add("tfcagricultureplus:" + rel.split("/")[-1])
# known block-only ids are valid block refs too
bad = {}
pat = re.compile(r"tfcagricultureplus:[a-z0-9_/.-]+")
files = list(data.rglob("*.json")) + list((assets / "blockstates").rglob("*.json")) + list((assets / "models").rglob("*.json"))
for p in files:
    text = p.read_text(encoding="utf-8")
    for ref in set(pat.findall(text)):
        if ref in valid:
            continue
        # block references may be in blockstates; item refs need models
        if ref.startswith("tfcagricultureplus:spice_crop/"):
            continue
        bad.setdefault(ref, []).append(str(p.relative_to(root)))
print("BAD_REFS", len(bad))
for ref, where in sorted(bad.items()):
    print(ref, "->", where[:2])
