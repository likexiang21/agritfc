from pathlib import Path
import json, zipfile

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
afc_jar = sorted(Path("mods").glob("afc-*.jar"))[-1]
leaf_root = root / "assets/afc/blockstates/wood/leaves"
leaf_root.mkdir(parents=True, exist_ok=True)
count = 0
with zipfile.ZipFile(afc_jar) as z:
    names = [n for n in z.namelist() if n.startswith("assets/afc/blockstates/wood/leaves/") and n.endswith(".json")]
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
print("expanded AFC leaf blockstates", count)
