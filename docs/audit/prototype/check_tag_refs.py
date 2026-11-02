from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
data = root / "data/tfcagricultureplus"
assets = root / "assets/tfcagricultureplus"
items = {p.relative_to(assets / "models/item").with_suffix("").as_posix() for p in (assets / "models/item").rglob("*.json")}
blocks = {p.relative_to(assets / "blockstates").with_suffix("").as_posix() for p in (assets / "blockstates").rglob("*.json")}
problems = []
for kind, valid in (("item", items), ("block", blocks)):
    for p in (data / f"tags/{kind}").rglob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        for v in d.get("values", []):
            if isinstance(v, str) and v.startswith("tfcagricultureplus:"):
                rid = v.split(":", 1)[1]
                # block items use blockstate path; item tags may still use item model
                if rid not in valid:
                    problems.append((kind, p.relative_to(data).as_posix(), v))
print("B tag missing refs", len(problems))
for x in problems[:50]:
    print(x)
