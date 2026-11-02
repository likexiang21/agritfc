from pathlib import Path

p = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("``", "`")
p.write_text(t, encoding="utf-8")
print("remaining double", t.count("``"))
