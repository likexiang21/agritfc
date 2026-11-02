import json
import re
import zipfile
from pathlib import Path

mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
jars = {
    "tfcfarmingplus": mods / "TFCFarmingPlus-NeoForge-1.21.1-0.1.0.jar",
    "tfc": mods / "TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar",
}
src = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop/CropWasteCrops.java").read_text(encoding="utf-8")
m = re.search(r"List\.of\((.*?)\);", src, re.S)
species = re.findall(r'"([^"]+)"', m.group(1))

with zipfile.ZipFile(jars["tfcfarmingplus"]) as a, zipfile.ZipFile(jars["tfc"]) as t:
    a_names = set(a.namelist())
    t_names = set(t.namelist())

    def best_tex(names, prefix, marker):
        best = None
        best_score = (-1, -1)
        for n in names:
            if not n.startswith(prefix) or not n.endswith(".png") or marker not in n:
                continue
            mm = re.search(marker + r"(\d+)(_top|_bottom)?\.png$", n)
            if not mm:
                continue
            age = int(mm.group(1))
            top = 1 if n.endswith("_top.png") else 0
            score = (age, top)
            if score > best_score:
                best_score = score
                best = n
        return best

    mapping = {}
    missing = []
    for sp in species:
        if sp == "strawberry":
            mapping[sp] = "tfc:block/berry_bush/strawberry_bush"
            continue
        n = best_tex(a_names, "assets/tfcfarmingplus/textures/block/crop/", f"/{sp}_age_")
        if n:
            mapping[sp] = "tfcfarmingplus:block/crop/" + Path(n).stem
            continue
        n = best_tex(t_names, "assets/tfc/textures/block/crop/", f"/{sp}_")
        if n:
            mapping[sp] = "tfc:block/crop/" + Path(n).stem
        else:
            missing.append(sp)

print("mapped", len(mapping), "missing", missing)
out = Path("mod_rebuild/docs/audit/prototype/crop_waste_texture_map.json")
out.write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")
for sp in ("spinach", "faba_bean", "strawberry", "potato"):
    print(sp, mapping.get(sp))
