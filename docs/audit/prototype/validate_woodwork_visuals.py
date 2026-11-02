import json
import zipfile
from pathlib import Path

mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
orig = mods / "tfcwoodwork-1.21.1-1.2.4.jar.disabled"
assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
woods = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow"]
kinds = ["debarked_log","debarked_half","debarked_quarter"]

problems = []
with zipfile.ZipFile(orig) as z:
    # shared models: geometry must match exactly
    for kind in kinds:
        b = json.loads((assets / "models/block/timber" / f"{kind}.json").read_text(encoding="utf-8"))
        o = json.loads(z.read(f"assets/tfcwoodwork/models/block/{kind}/{kind}.json").decode("utf-8"))
        if b.get("elements") != o.get("elements"):
            problems.append(f"shared {kind}: elements differ")
        if b.get("credit") != o.get("credit"):
            problems.append(f"shared {kind}: credit differ")

    for wood in woods:
        for kind in kinds:
            b_bs = json.loads((assets / "blockstates" / kind / f"{wood}.json").read_text(encoding="utf-8"))
            o_bs = json.loads(z.read(f"assets/tfcwoodwork/blockstates/{kind}/{wood}.json").decode("utf-8"))
            if set(b_bs.get("variants", {})) != set(o_bs.get("variants", {})):
                problems.append(f"{kind}/{wood}: blockstate variants differ")
            b_item = json.loads((assets / "models/item" / kind / f"{wood}.json").read_text(encoding="utf-8"))
            o_item = json.loads(z.read(f"assets/tfcwoodwork/models/item/{kind}/{wood}.json").decode("utf-8"))
            if b_item.get("parent") != o_item.get("parent"):
                problems.append(f"{kind}/{wood}: item parent differ")
            b_model = json.loads((assets / "models/block" / kind / f"{wood}.json").read_text(encoding="utf-8"))
            o_model = json.loads(z.read(f"assets/tfcwoodwork/models/block/{kind}/{wood}.json").decode("utf-8"))
            for key, value in o_model.get("textures", {}).items():
                bv = b_model.get("textures", {}).get(key)
                normalized = value.replace("tfcwoodwork:", "tfcagricultureplus:")
                if bv != normalized:
                    problems.append(f"{kind}/{wood}: texture {key} {bv} != {normalized}")

print("rows", len(woods) * len(kinds))
print("problems", len(problems))
for p in problems[:20]:
    print("BAD", p)
if not problems:
    print("PASS: TFC woodwork visual parity")
