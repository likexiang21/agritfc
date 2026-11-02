from pathlib import Path
import json

base = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe")
groups = {}
for p in base.rglob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("type") == "minecraft:crafting_shaped":
        key = (tuple(d.get("pattern", [])), json.dumps(d.get("key", {}), sort_keys=True))
        groups.setdefault(key, []).append((p, d.get("result")))
for key, refs in groups.items():
    if len(refs) > 1:
        print("SHAPED COLLISION", key)
        for p, res in refs:
            print("  ", p.name, res)
print("total shaped recipes", sum(len(v) for v in groups.values()), "groups", len(groups))
