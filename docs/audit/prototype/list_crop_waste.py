from pathlib import Path
import re

t = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md").read_text(encoding="utf-8")
s = t.find("#### 4.1.2")
e = t.find("#### 4.1.3")
names = []
for line in t[s:e].splitlines():
    m = re.match(r"\| `([^`]+)` \| (A·|TFC·)", line)
    if m:
        names.append(m.group(1))
print("count", len(names))
for i in range(0, len(names), 8):
    print("    " + ", ".join('"' + n + '"' for n in names[i:i+8]) + ",")
