import json
import zipfile
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
assets = root / "assets/tfcagricultureplus"
mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
tfc = mods / "TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar"

lang = {name: json.loads((assets / "lang" / f"{name}.json").read_text(encoding="utf-8"))
        for name in ("en_us", "zh_cn")}
models = list((assets / "models/item/metal_can").glob("*.json"))
tag = json.loads((root / "data/tfcagricultureplus/tags/fluid/metal_can_fluids.json").read_text(encoding="utf-8"))

problems = []
with zipfile.ZipFile(tfc) as z:
    for p in models:
        metal = p.stem
        d = json.loads(p.read_text(encoding="utf-8"))
        if d.get("loader") != "tfc:fluid_container":
            problems.append(f"{metal}: loader {d.get('loader')}")
        base = d.get("textures", {}).get("base", "")
        overlay = d.get("textures", {}).get("fluid", "")
        if not base.endswith(f"metal/sheet/{metal}"):
            problems.append(f"{metal}: bad base {base}")
        if not base.startswith("tfc:"):
            problems.append(f"{metal}: base namespace {base}")
        if overlay != "tfc:item/metal/bucket/overlay":
            problems.append(f"{metal}: bad overlay {overlay}")
        base_path = "assets/tfc/textures/" + base.split(":", 1)[1] + ".png"
        overlay_path = "assets/tfc/textures/" + overlay.split(":", 1)[1] + ".png"
        if base_path not in z.namelist():
            problems.append(f"{metal}: missing base texture {base_path}")
        if overlay_path not in z.namelist():
            problems.append(f"{metal}: missing overlay {overlay_path}")
        for lang_name in ("en_us", "zh_cn"):
            for suffix in ("", ".filled"):
                key = f"item.tfcagricultureplus.metal_can.{metal}{suffix}"
                if key not in lang[lang_name]:
                    problems.append(f"{metal}: missing {lang_name} {key}")

print("metal can models", len(models))
print("tag values", len(tag.get("values", [])))
print("problems", len(problems))
for p in problems:
    print("BAD", p)
if not problems and len(models) == 19:
    print("PASS: metal can models")
