from pathlib import Path
import re

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop/CropWasteCrops.java")
t = p.read_text(encoding="utf-8")
m = re.search(r"List\.of\((.*?)\);", t, re.S)
names = re.findall(r'"([^"]+)"', m.group(1))
print("count", len(names))
print(names)
