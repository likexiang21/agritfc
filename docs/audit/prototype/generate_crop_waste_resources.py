from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
doc = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md").read_text(encoding="utf-8")
s = doc.find("#### 4.1.2")
e = doc.find("#### 4.1.3")
rows = []
for line in doc[s:e].splitlines():
    if not line.startswith("| `"):
        continue
    parts = [p.strip() for p in line.strip().strip("|").split("|")]
    if len(parts) < 6 or "crop_waste/" not in parts[2]:
        continue
    crop = parts[0].strip("`")
    tag = parts[4].strip("`")
    rows.append((crop, tag))
rows.append(("cabbage", "tfc:compost_greens/high"))
assert len(rows) == 82, len(rows)

for crop, tag in rows:
    model = assets / "models/item/crop_waste" / (crop + ".json")
    model.parent.mkdir(parents=True, exist_ok=True)
    model.write_text(json.dumps({
        "parent": "minecraft:item/generated",
        "textures": {"layer0": "tfc:item/straw"}
    }, indent=2) + "\n", encoding="utf-8")

for lang, label in (("en_us", "Crop Waste ({})"), ("zh_cn", "作物废枝叶（{}）")):
    path = assets / "lang" / (lang + ".json")
    data = json.loads(path.read_text(encoding="utf-8"))
    for crop, _ in rows:
        data["item.tfcagricultureplus.crop_waste." + crop] = label.format(crop)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

tag_root = root / "data/tfc/tags/item/compost_greens"
tag_root.mkdir(parents=True, exist_ok=True)
by_tag = {}
for crop, tag in rows:
    name = tag.rsplit("/", 1)[-1]
    by_tag.setdefault(name, []).append("tfcagricultureplus:crop_waste/" + crop)
for level, values in by_tag.items():
    path = tag_root / (level + ".json")
    existing = []
    if path.exists():
        payload = json.loads(path.read_text(encoding="utf-8"))
        existing = [v for v in payload.get("values", []) if isinstance(v, str)]
    merged = sorted(set(existing + values))
    path.write_text(json.dumps({"replace": False, "values": merged}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("crop_waste models", len(rows), "tag levels", {k: len(v) for k, v in by_tag.items()})
