from pathlib import Path
import json

assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
models = {}
for p in (assets / "models").rglob("*.json"):
    rel = p.relative_to(assets / "models").with_suffix("").as_posix()
    models[rel] = json.loads(p.read_text(encoding="utf-8"))

referenced = set()
def add_ref(ref):
    if isinstance(ref, str) and ref.startswith("tfcagricultureplus:"):
        referenced.add(ref.split(":", 1)[1])

for p in (assets / "blockstates").rglob("*.json"):
    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ("model",):
                    add_ref(v)
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(json.loads(p.read_text(encoding="utf-8")))

# item models are roots; their parent refs are dependencies
for rel, d in models.items():
    if rel.startswith("item/"):
        referenced.add(rel)

# all parent refs from all models
for rel, d in models.items():
    add_ref(d.get("parent"))

# transitively mark parents
changed = True
while changed:
    changed = False
    for rel, d in models.items():
        if rel in referenced:
            parent = d.get("parent")
            before = len(referenced)
            add_ref(parent)
            if len(referenced) != before:
                changed = True

orphans = sorted(set(models) - referenced)
print("models", len(models), "referenced", len(referenced), "orphans", len(orphans))
for x in orphans[:100]:
    print("ORPHAN", x)
