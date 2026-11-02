from pathlib import Path
import json
import re
import sys

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
data = root / "data/tfcagricultureplus"
jsons = list(root.rglob("*.json"))
problems = []
for p in jsons:
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        problems.append(("json", str(p), str(e)))

models = {p.relative_to(assets / "models").with_suffix("").as_posix(): json.loads(p.read_text(encoding="utf-8"))
          for p in (assets / "models").rglob("*.json")}
textures = {p.relative_to(assets / "textures").with_suffix("").as_posix() for p in (assets / "textures").rglob("*.png")}
item_models = {p.relative_to(assets / "models/item").with_suffix("").as_posix() for p in (assets / "models/item").rglob("*.json")}
blockstates = {p.relative_to(assets / "blockstates").with_suffix("").as_posix() for p in (assets / "blockstates").rglob("*.json")}
langs = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in (assets / "lang").glob("*.json")}

# model parent/texture
for rel, d in models.items():
    parent = d.get("parent")
    if isinstance(parent, str) and parent.startswith("tfcagricultureplus:") and parent.split(":", 1)[1] not in models:
        problems.append(("model parent", rel, parent))
    for k, v in d.get("textures", {}).items():
        if isinstance(v, str) and v.startswith("tfcagricultureplus:") and v.split(":", 1)[1] not in textures:
            problems.append(("model texture", rel, v))

# lang parity and missing names
if len(langs) >= 2:
    base_name = "en_us.json"
    base = set(langs[base_name])
    for name, d in langs.items():
        if name == base_name:
            continue
        if set(d) != base:
            problems.append(("lang parity", name, f"missing={len(base-set(d))} extra={len(set(d)-base)}"))
for name, d in langs.items():
    for k, v in d.items():
        if isinstance(v, str) and not v.strip():
            problems.append(("empty lang", name, k))
for b in blockstates:
    if "block.tfcagricultureplus." + b not in langs.get("en_us.json", {}) and "block.tfcagricultureplus." + b.replace("/", ".") not in langs.get("en_us.json", {}):
        problems.append(("block lang", b))
for item in item_models:
    keys = []
    if item in blockstates:
        keys = ["block.tfcagricultureplus." + item, "block.tfcagricultureplus." + item.replace("/", ".")]
    else:
        keys = ["item.tfcagricultureplus." + item, "item.tfcagricultureplus." + item.replace("/", ".")]
    if not any(k in langs.get("en_us.json", {}) for k in keys):
        problems.append(("item lang", item))

# recipe refs
item_tags = {p.relative_to(data / "tags/item").with_suffix("").as_posix() for p in (data / "tags/item").rglob("*.json")}
block_tags = {p.relative_to(data / "tags/block").with_suffix("").as_posix() for p in (data / "tags/block").rglob("*.json")}
def walk_recipe(obj, where):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("item", "result") and isinstance(v, str):
                check_item(v, where)
            elif k == "id" and isinstance(v, str):
                check_item(v, where)
            elif k == "tag" and isinstance(v, str) and v.startswith("tfcagricultureplus:"):
                rid = v.split(":", 1)[1]
                if rid not in item_tags and rid not in block_tags:
                    problems.append(("recipe tag", where, v))
            elif k == "block" and isinstance(v, str) and v.startswith("tfcagricultureplus:"):
                if v.split(":", 1)[1] not in blockstates:
                    problems.append(("recipe block", where, v))
            walk_recipe(v, where)
    elif isinstance(obj, list):
        for v in obj:
            walk_recipe(v, where)

def check_item(ref, where):
    if ref.startswith("tfcagricultureplus:"):
        rid = ref.split(":", 1)[1]
        if rid not in item_models and rid not in blockstates:
            problems.append(("item ref", where, ref))

for p in (data / "recipe").rglob("*.json"):
    walk_recipe(json.loads(p.read_text(encoding="utf-8")), p.relative_to(data).as_posix())

# loot blocks plus item entries
for p in (data / "loot_table").rglob("*.json"):
    rel = p.relative_to(data / "loot_table").with_suffix("").as_posix()
    if rel.startswith("blocks/") and rel[7:] not in blockstates:
        problems.append(("loot blockstate", rel))
    text = p.read_text(encoding="utf-8")
    for ref in re.findall(r'"name"\s*:\s*"(tfcagricultureplus:[^"]+)"', text):
        rid = ref.split(":", 1)[1]
        if rid not in item_models and rid not in blockstates:
            problems.append(("loot item", rel, ref))

# worldgen configured block refs and placed feature refs
configured = {p.stem for p in (data / "worldgen/configured_feature").glob("*.json")}
placed = {p.stem for p in (data / "worldgen/placed_feature").glob("*.json")}
for p in (data / "worldgen/configured_feature").glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    text = json.dumps(d)
    for ref in re.findall(r'"tfcagricultureplus:(block/[^"]+|spice_crop/[^"]+|wild_mushroom/[^"]+)"', text):
        if ref not in blockstates:
            problems.append(("configured block", p.name, ref))
for p in (data / "worldgen/placed_feature").glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    feat = d.get("feature", "")
    if feat.startswith("tfcagricultureplus:") and feat.split(":", 1)[1] not in configured:
        problems.append(("placed feature", p.name, feat))

# tags
for kind, valid in (("block", blockstates), ("item", item_models)):
    for p in (data / f"tags/{kind}").rglob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        for v in d.get("values", []):
            if isinstance(v, str) and v.startswith("tfcagricultureplus:"):
                if v.split(":", 1)[1] not in valid:
                    problems.append((f"tag {kind}", p.name, v))

print("json", len(jsons), "models", len(models), "blockstates", len(blockstates), "item_models", len(item_models))
print("problems", len(problems))
for x in problems[:100]:
    print("PROBLEM", x)
sys.exit(1 if problems else 0)
