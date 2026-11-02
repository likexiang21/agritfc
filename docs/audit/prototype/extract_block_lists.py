import re
from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/registry/AgricultureBlocks.java")
t = p.read_text(encoding="utf-8")
for name in ("TFC_WOODS", "AFC_WOODS", "MORTAR_ROCKS", "TFC_ROCKS"):
    m = re.search(r"(?:List<String>|Set<String>)\s+" + name + r"\s*=\s*List\.of\((.*?)\);", t, re.S)
    if not m:
        m = re.search(name + r"\s*=\s*(?:Set\.of|List\.of)\((.*?)\);", t, re.S)
    if not m:
        print(name, "NOT FOUND")
        continue
    vals = re.findall(r'"([^"]+)"', m.group(1))
    print(name, len(vals))
    print(vals)
