from pathlib import Path
import json, zipfile

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
tfc_jar = sorted(Path("mods").glob("TerraFirmaCraft-NeoForge-*.jar"))[-1]

nuts = ["acorn", "chestnut", "pine_nut", "hickory_nut", "pistachio", "cashew", "macadamia", "beechnut"]
for nut in nuts:
    model = assets / "models/item" / (nut + ".json")
    model.parent.mkdir(parents=True, exist_ok=True)
    model.write_text(json.dumps({"parent": "minecraft:item/generated",
                                 "textures": {"layer0": "tfc:item/straw"}}, indent=2) + "\n", encoding="utf-8")
for lang, label in (("en_us", "Nut ({})"), ("zh_cn", "坚果（{}）")):
    path = assets / "lang" / (lang + ".json")
    data = json.loads(path.read_text(encoding="utf-8"))
    for nut in nuts:
        data["item.tfcagricultureplus." + nut] = label.format(nut)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

leaf_root = root / "assets/tfc/blockstates/wood/leaves"
leaf_root.mkdir(parents=True, exist_ok=True)
count = 0
with zipfile.ZipFile(tfc_jar) as z:
    names = [n for n in z.namelist() if n.startswith("assets/tfc/blockstates/wood/leaves/") and n.endswith(".json")]
    for name in sorted(names):
        original = json.loads(z.read(name).decode("utf-8"))
        if "variants" in original:
            expanded = {}
            for key, value in original["variants"].items():
                for nut_state in range(4):
                    expanded["nut_state=" + str(nut_state) if not key else key + ",nut_state=" + str(nut_state)] = value
            out = dict(original)
            out["variants"] = expanded
        elif "multipart" in original:
            parts = []
            for part in original["multipart"]:
                for nut_state in range(4):
                    copy = dict(part)
                    when = copy.get("when")
                    when = dict(when) if isinstance(when, dict) else {}
                    when["nut_state"] = str(nut_state)
                    copy["when"] = when
                    parts.append(copy)
            out = dict(original)
            out["multipart"] = parts
        else:
            continue
        (leaf_root / Path(name).name).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        count += 1
print(f"nuts {len(nuts)}, expanded TFC leaf blockstates {count}")
