from pathlib import Path
import json
import sys

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
bad = []
count = 0
for p in root.rglob("*.json"):
    count += 1
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        bad.append((str(p), str(e)))
print("json files", count, "bad", len(bad))
for p, e in bad[:30]:
    print("BAD", p, e)

# lang key counts and parity
lang_dir = root / "assets/tfcagricultureplus/lang"
langs = {}
for p in sorted(lang_dir.glob("*.json")):
    langs[p.name] = json.loads(p.read_text(encoding="utf-8"))
    print("lang", p.name, len(langs[p.name]))
names = list(langs)
if len(names) >= 2:
    base = set(langs[names[0]])
    for n in names[1:]:
        other = set(langs[n])
        print("lang missing in", n, len(base - other))
        print("lang extra in", n, len(other - base))
        for k in sorted(base - other)[:20]:
            print("  missing", k)
        for k in sorted(other - base)[:20]:
            print("  extra", k)
