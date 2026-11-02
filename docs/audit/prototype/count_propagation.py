import re
from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop/CropPropagation.java")
t = p.read_text(encoding="utf-8")
for m in re.finditer(r"add\(Method\.(\w+),\s*(.*?)\);", t, re.S):
    method = m.group(1)
    names = re.findall(r'"([^"]+)"', m.group(2))
    print(method, len(names))
