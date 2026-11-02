from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
data = root / "data/tfcagricultureplus"
assets = root / "assets/tfcagricultureplus"
item_models = {p.relative_to(assets / "models/item").with_suffix("").as_posix() for p in (assets / "models/item").rglob("*.json")}
blockstates = {p.relative_to(assets / "blockstates").with_suffix("").as_posix() for p in (assets / "blockstates").rglob("*.json")}
item_tags = {p.relative_to(data / "tags/item").with_suffix("").as_posix() for p in (data / "tags/item").rglob("*.json")}
block_tags = {p.relative_to(data / "tags/block").with_suffix("").as_posix() for p in (data / "tags/block").rglob("*.json")}

problems = []
def check_item(ref, where):
    if not ref.startswith("tfcagricultureplus:"):
        return
    rid = ref.split(":", 1)[1]
    if rid in item_models or rid in blockstates:
        return
    problems.append((where, "missing item", ref))

def check_tag(ref, where):
    if not ref.startswith("tfcagricultureplus:"):
        return
    rid = ref.split(":", 1)[1]
    if rid in item_tags or rid in block_tags:
        return
    problems.append((where, "missing tag", ref))

def walk(obj, where):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("item", "result") and isinstance(v, str):
                check_item(v, where)
            elif k == "id" and isinstance(v, str):
                check_item(v, where)
            elif k == "tag" and isinstance(v, str):
                check_tag(v, where)
            elif k == "block" and isinstance(v, str):
                if v.startswith("tfcagricultureplus:") and v.split(":", 1)[1] not in blockstates:
                    problems.append((where, "missing block", v))
            walk(v, where)
    elif isinstance(obj, list):
        for v in obj:
            walk(v, where)

for p in (data / "recipe").rglob("*.json"):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        problems.append((str(p), "bad json", str(e)))
        continue
    walk(d, p.relative_to(data).as_posix())

print("recipe reference problems", len(problems))
for x in problems[:80]:
    print("PROBLEM", x)
