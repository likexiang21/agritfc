from pathlib import Path
import json

problems = []
def hook(pairs):
    seen = {}
    for k, v in pairs:
        if k in seen:
            problems.append(("duplicate key", k))
        seen[k] = v
    return seen

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
for p in root.rglob("*.json"):
    try:
        json.loads(p.read_text(encoding="utf-8"), object_pairs_hook=hook)
    except Exception as e:
        problems.append((str(p), str(e)))
print("duplicate/json problems", len(problems))
for x in problems[:50]:
    print("PROBLEM", x)
