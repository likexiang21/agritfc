import json
import zipfile
from pathlib import Path

B = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe/crafting/woodwork/tfc")
ORIG = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\tfcwoodwork-1.21.1-1.2.4.jar.disabled")

def normalize(d, namespace):
    # compare structure while treating expected namespace/material differences separately
    return {
        "type": d.get("type"),
        "pattern": d.get("pattern"),
        "result": d.get("result"),
    }

with zipfile.ZipFile(ORIG) as z:
    orig = {}
    for kind in ("wood", "stripped_wood"):
        for wood in [p.stem for p in (B / kind).glob("*.json")]:
            n = f"data/tfcwoodwork/recipe/crafting/{kind}/{wood}.json"
            if n in z.namelist():
                orig[(kind, wood)] = json.loads(z.read(n).decode("utf-8"))

problems = []
for (kind, wood), od in orig.items():
    bp = B / kind / f"{wood}.json"
    bd = json.loads(bp.read_text(encoding="utf-8"))
    if normalize(od, "tfcwoodwork") != normalize(bd, "tfcagricultureplus"):
        problems.append((kind, wood, normalize(od, "tfcwoodwork"), normalize(bd, "tfcagricultureplus")))
    # keys must match apart from material namespace
    okeys = json.dumps(od.get("key"), sort_keys=True).replace("tfcwoodwork:", "NS:")
    bkeys = json.dumps(bd.get("key"), sort_keys=True).replace("tfcagricultureplus:", "NS:")
    if okeys != bkeys:
        problems.append((kind, wood, "KEY", od.get("key"), bd.get("key")))

print("original recipes", len(orig), "B copied", len(list(B.rglob("*.json"))), "problems", len(problems))
for x in problems:
    print("PROBLEM", x)
