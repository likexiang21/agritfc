from pathlib import Path
import json
import zipfile

# B local
patterns = {}
for p in Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe").rglob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("type") != "tfc:knapping":
        continue
    key = (d.get("knapping_type", "?"), tuple(d.get("pattern", [])))
    patterns.setdefault(key, []).append(("tfcagricultureplus", str(p), d.get("result")))

# TFC jar
jars = list(Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods").glob("TerraFirmaCraft-*.jar"))
for jar in jars:
    with zipfile.ZipFile(jar) as z:
        for n in z.namelist():
            if not n.startswith("data/tfc/recipe/") or not n.endswith(".json"):
                continue
            try:
                d = json.loads(z.read(n).decode("utf-8"))
            except Exception:
                continue
            if d.get("type") != "tfc:knapping":
                continue
            key = (d.get("knapping_type", "?"), tuple(d.get("pattern", [])))
            patterns.setdefault(key, []).append(("tfc", n, d.get("result")))

print("knapping pattern groups", len(patterns))
for key, refs in patterns.items():
    if len(refs) > 1:
        print("\nCOLLISION", key[0], key[1])
        for r in refs:
            print("  ", r[0], r[1], r[2])
