import json
import shutil
import zipfile
from pathlib import Path

mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
src = mods / "tfcwoodwork-1.21.1-1.2.4.jar.disabled"
assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
TFC = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow"]
AFC = ["araucaria","baobab","beech","cypress","eucalyptus","fig","ginkgo","hevea","ipe","ironwood","mahoe","mahogany","teak","tualang"]
KINDS = ["debarked_log", "debarked_half", "debarked_quarter"]

# backup affected assets
backup_dir = Path("mod_rebuild/backups/woodwork-visual-20261029")
if not backup_dir.exists():
    backup_dir.mkdir(parents=True, exist_ok=True)
    for kind in KINDS:
        for sub in (assets / "blockstates" / kind, assets / "models/block" / kind, assets / "models/item" / kind):
            if sub.exists():
                dst = backup_dir / sub.relative_to(assets)
                shutil.copytree(sub, dst, dirs_exist_ok=True)
    for kind in KINDS:
        p = assets / "models/block/timber" / f"{kind}.json"
        if p.exists():
            dst = backup_dir / p.relative_to(assets)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dst)

with zipfile.ZipFile(src) as z:
    # shared block models (original geometry)
    for kind in KINDS:
        n = f"assets/tfcwoodwork/models/block/{kind}/{kind}.json"
        data = json.loads(z.read(n).decode("utf-8"))
        p = assets / "models/block/timber" / f"{kind}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # TFC per-wood block models + item models + copied textures
    for wood in TFC:
        for kind in KINDS:
            n = f"assets/tfcwoodwork/models/block/{kind}/{wood}.json"
            data = json.loads(z.read(n).decode("utf-8"))
            data["parent"] = f"tfcagricultureplus:block/timber/{kind}"
            textures = data.get("textures", {})
            if "inner" in textures:
                textures["inner"] = f"tfcagricultureplus:block/log_inner/{wood}"
            data["textures"] = textures
            p = assets / "models/block" / kind / f"{wood}.json"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

            # item model: original generated icon
            n_item = f"assets/tfcwoodwork/models/item/{kind}/{wood}.json"
            item = json.loads(z.read(n_item).decode("utf-8"))
            item["textures"]["layer0"] = f"tfcagricultureplus:item/{kind}/{wood}"
            p = assets / "models/item" / kind / f"{wood}.json"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

            # blockstate: no facing property
            bs = {"variants": {"": {"model": f"tfcagricultureplus:block/{kind}/{wood}"}}}
            p = assets / "blockstates" / kind / f"{wood}.json"
            p.write_text(json.dumps(bs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        # copied TFCW item icon textures (existing art, not redrawn)
        for kind in KINDS:
            n = f"assets/tfcwoodwork/textures/item/{kind}/{wood}.png"
            out = assets / "textures/item" / kind / f"{wood}.png"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(z.read(n))
        inner = f"assets/tfcwoodwork/textures/block/log_inner/{wood}.png"
        out = assets / "textures/block/log_inner" / f"{wood}.png"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(z.read(inner))

    # AFC: original-style models with AFC wood textures; no item icons available -> block parent
    template = json.loads(z.read("assets/tfcwoodwork/models/block/debarked_log/oak.json").decode("utf-8"))
    parent_map = { "debarked_log": "debarked_log", "debarked_half": "debarked_half", "debarked_quarter": "debarked_quarter" }
    for wood in AFC:
        for kind in KINDS:
            model = {
                "parent": f"tfcagricultureplus:block/timber/{kind}",
                "textures": {
                    "side": f"afc:block/wood/sheet/{wood}",
                    "top": f"afc:block/wood/log_top/{wood}",
                    "inner": f"afc:block/wood/sheet/{wood}",
                    "particle": f"afc:block/wood/sheet/{wood}",
                },
            }
            p = assets / "models/block" / kind / f"{wood}.json"
            p.write_text(json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            p = assets / "models/item" / kind / f"{wood}.json"
            p.write_text(json.dumps({"parent": f"tfcagricultureplus:block/{kind}/{wood}"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            bs = {"variants": {"": {"model": f"tfcagricultureplus:block/{kind}/{wood}"}}}
            p = assets / "blockstates" / kind / f"{wood}.json"
            p.write_text(json.dumps(bs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("woodwork assets aligned; backup at", backup_dir)
