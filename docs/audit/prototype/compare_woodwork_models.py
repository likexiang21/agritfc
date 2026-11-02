import json
import zipfile
from pathlib import Path

mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
orig = mods / "tfcwoodwork-1.21.1-1.2.4.jar.disabled"
assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
woods = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow"]
kinds = ["debarked_log","debarked_half","debarked_quarter"]

def load_orig(name):
    with zipfile.ZipFile(orig) as z:
        if name in z.namelist():
            return json.loads(z.read(name).decode("utf-8"))
    return None

rows = []
for kind in kinds:
    for wood in woods:
        b_bs = json.loads((assets / "blockstates" / kind / f"{wood}.json").read_text(encoding="utf-8"))
        o_bs = load_orig(f"assets/tfcwoodwork/blockstates/{kind}/{wood}.json")
        b_model = json.loads((assets / "models/block" / kind / f"{wood}.json").read_text(encoding="utf-8"))
        o_model = load_orig(f"assets/tfcwoodwork/models/block/{kind}/{wood}.json")
        b_item = json.loads((assets / "models/item" / kind / f"{wood}.json").read_text(encoding="utf-8"))
        o_item = load_orig(f"assets/tfcwoodwork/models/item/{kind}/{wood}.json")
        rows.append({
            "kind": kind, "wood": wood,
            "b_blockstate_keys": sorted(b_bs.get("variants", {}).keys()),
            "o_blockstate_keys": sorted((o_bs or {}).get("variants", {}).keys()),
            "b_model_parent": b_model.get("parent"),
            "o_model_parent": (o_model or {}).get("parent"),
            "b_textures": b_model.get("textures"),
            "o_textures": (o_model or {}).get("textures"),
            "b_item_parent": b_item.get("parent"),
            "o_item_parent": (o_item or {}).get("parent"),
        })

# summarize differences
diff_bs = [r for r in rows if r["b_blockstate_keys"] != r["o_blockstate_keys"]]
diff_parent = [r for r in rows if r["b_model_parent"] != r["o_model_parent"]]
diff_tex = [r for r in rows if r["b_textures"] != r["o_textures"]]
diff_item = [r for r in rows if r["b_item_parent"] != r["o_item_parent"]]
print("rows", len(rows))
print("blockstate key differences", len(diff_bs), "sample", diff_bs[0] if diff_bs else None)
print("model parent differences", len(diff_parent), "sample", diff_parent[0] if diff_parent else None)
print("texture differences", len(diff_tex), "sample", diff_tex[0] if diff_tex else None)
print("item parent differences", len(diff_item), "sample", diff_item[0] if diff_item else None)
