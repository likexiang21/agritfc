from pathlib import Path
import json
import zipfile

candidates = {
    "candidate_a": [" ### ", "#####", " ### ", "     ", "     "],
    "candidate_b": ["#####", "#   #", "#   #", "#   #", "#####"],
    "candidate_c": [" ### ", "#####", "#####", " ### ", "     "],
}

patterns = set()

# B local
for p in Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe").rglob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("type") == "tfc:knapping":
        patterns.add((d.get("knapping_type"), tuple(d.get("pattern", []))))

# TFC + A jars
mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
for jar in mods.glob("*.jar"):
    try:
        with zipfile.ZipFile(jar) as z:
            for n in z.namelist():
                if not n.endswith(".json") or "/recipe/" not in n:
                    continue
                try:
                    d = json.loads(z.read(n).decode("utf-8"))
                except Exception:
                    continue
                if d.get("type") == "tfc:knapping":
                    patterns.add((d.get("knapping_type"), tuple(d.get("pattern", []))))
    except Exception:
        pass

for name, pat in candidates.items():
    key = ("tfc:clay", tuple(pat))
    print(name, "collision" if key in patterns else "FREE")
