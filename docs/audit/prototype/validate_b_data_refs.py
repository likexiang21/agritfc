from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
models = {p.relative_to(assets / "models/item").as_posix()[:-5] for p in (assets / "models/item").rglob("*.json")}
states = {p.relative_to(assets / "blockstates").as_posix()[:-5] for p in (assets / "blockstates").rglob("*.json")}
# block items inherit the block's id; many block ids are also in states
blockitems = set()
for p in (assets / "blockstates").rglob("*.json"):
    rel = p.relative_to(assets / "blockstates").as_posix()[:-5]
    blockitems.add(rel)


def walk(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("name", "item", "id") and isinstance(v, str):
                yield v
            else:
                yield from walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v)


bad = {}
for p in list((data / "loot_table").rglob("*.json")) + list((data / "recipe").rglob("*.json")):
    for ref in set(walk(json.loads(p.read_text(encoding="utf-8")))):
        if not ref.startswith("tfcagricultureplus:"):
            continue
        path = ref.split(":", 1)[1]
        if path in models or path in states:
            continue
        bad.setdefault(ref, []).append(str(p.relative_to(root)))
print("BAD_REFS", len(bad))
for ref, where in sorted(bad.items()):
    print(ref, "->", where[:3])
