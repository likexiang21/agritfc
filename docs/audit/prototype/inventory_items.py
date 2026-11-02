import pathlib, re
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/java")
items = []
for p in base.rglob("*.java"):
    s = p.read_text(encoding="utf-8")
    for m in re.finditer(r'register(?:SimpleItem|Item|SimpleBlockItem)?\s*\(\s*"([^"]+)"', s):
        items.append((m.group(1), p.name))
for name, f in sorted(items):
    print(name, '|', f)
print('count', len(items))
