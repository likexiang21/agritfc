import pathlib, re
p = pathlib.Path(r"mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
s = p.read_text(encoding="utf-8")
rows = {}
for line in s.splitlines():
    m = re.search(r"\|\s*`([a-z0-9_]+)`\s*\|[^\n]*?`tfc:compost_greens/(high|medium|low)`", line)
    if m:
        rows[m.group(1)] = m.group(2)
print(len(rows))
for k in sorted(rows):
    print(k, rows[k])
