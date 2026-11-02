from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
data = root / "data/tfcagricultureplus"
assets = root / "assets/tfcagricultureplus"
blockstates = {p.relative_to(assets / "blockstates").with_suffix("").as_posix() for p in (assets / "blockstates").rglob("*.json")}
configured = {p.stem for p in (data / "worldgen/configured_feature").glob("*.json")}
placed = {p.stem for p in (data / "worldgen/placed_feature").glob("*.json")}
problems = []

for p in (data / "loot_table").rglob("*.json"):
    rel = p.relative_to(data / "loot_table").with_suffix("").as_posix()
    if rel.startswith("blocks/"):
        bid = rel[len("blocks/"):]
        if bid not in blockstates:
            problems.append(("loot missing blockstate", rel))
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        problems.append(("bad loot json", str(p), str(e)))

for p in (data / "worldgen/placed_feature").glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    feat = d.get("feature", "")
    if feat.startswith("tfcagricultureplus:") and feat.split(":", 1)[1] not in configured:
        problems.append(("placed missing configured", p.name, feat))

for p in (data / "worldgen/configured_feature").glob("*.json"):
    text = p.read_text(encoding="utf-8")
    for token in ("tfcagricultureplus:"):
        pass

# B tags values that point to missing B block/item
for tag_root, kind in ((data / "tags/block", "block"), (data / "tags/item", "item")):
    for p in tag_root.rglob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        for v in d.get("values", []):
            if isinstance(v, str) and v.startswith("tfcagricultureplus:"):
                rid = v.split(":", 1)[1]
                if kind == "block" and rid not in blockstates:
                    problems.append(("tag missing block", p.name, v))
                if kind == "item" and rid not in {x.name for x in []}:
                    pass

print("problems", len(problems))
for x in problems[:50]:
    print("PROBLEM", x)
