from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
lang = json.loads((root / "assets/tfcagricultureplus/lang/en_us.json").read_text(encoding="utf-8"))
missing = []
for p in (root / "assets/tfcagricultureplus/blockstates").rglob("*.json"):
    rel = p.relative_to(root / "assets/tfcagricultureplus/blockstates").with_suffix("").as_posix()
    keys = ["block.tfcagricultureplus." + rel, "block.tfcagricultureplus." + rel.replace("/", ".")]
    if not any(k in lang for k in keys):
        missing.append(rel)
print("missing block lang using slash/dot:", len(missing))
for x in missing[:50]:
    print(x)
