import json
import re
import zipfile
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus")
src = root / "src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop/PropagationStock.java"
assets = root / "src/main/resources/assets/tfcagricultureplus"
data = root / "src/main/resources/data/tfcagricultureplus"
mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
jars = {
    "tfc": mods / "TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar",
    "tfcfarmingplus": mods / "TFCFarmingPlus-NeoForge-1.21.1-0.1.0.jar",
    "tfcagricultureplus": mods / "TFCAgriculturePlus-NeoForge-1.21.1-0.1.0.jar",
}

rows = []
for line in src.read_text(encoding="utf-8").splitlines():
    m = re.search(r'c\("([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\)', line)
    if m:
        rows.append(m.groups())

problems = []
if len(rows) != 21:
    problems.append(f"expected 21 rows, got {len(rows)}")
if len({r[0] for r in rows}) != len(rows):
    problems.append("duplicate species")

lang = {}
for lang_name in ("en_us", "zh_cn"):
    lang[lang_name] = json.loads((assets / "lang" / f"{lang_name}.json").read_text(encoding="utf-8"))

for species, crop, product in rows:
    model = assets / "models/item/propagation_stock" / f"{species}.json"
    recipe = data / "recipe/crafting/propagation_stock" / f"{species}.json"
    if not model.exists():
        problems.append(f"{species}: missing model")
    if not recipe.exists():
        problems.append(f"{species}: missing recipe")
        continue
    d = json.loads(recipe.read_text(encoding="utf-8"))
    if d.get("ingredients") != [{"item": product}]:
        problems.append(f"{species}: recipe input != {product}")
    if d.get("result", {}).get("id") != f"tfcagricultureplus:propagation_stock/{species}":
        problems.append(f"{species}: recipe output mismatch")
    key = f"item.tfcagricultureplus.propagation_stock.{species}"
    if key not in lang["en_us"] or key not in lang["zh_cn"]:
        problems.append(f"{species}: missing lang")
    ns, path = product.split(":", 1)
    with zipfile.ZipFile(jars[ns]) as z:
        if f"assets/{ns}/models/item/{path}.json" not in z.namelist():
            problems.append(f"{species}: missing product model {product}")
    ns, path = crop.split(":", 1)
    with zipfile.ZipFile(jars[ns]) as z:
        if f"assets/{ns}/blockstates/{path}.json" not in z.namelist():
            problems.append(f"{species}: missing crop blockstate {crop}")

methods = {}
for species, _, _ in rows:
    # parse method from the section comment above each row block
    pass
blocks = re.findall(r"//\s*([A-Z]+)\n((?:\s*c\([^\n]+\n)+)", src.read_text(encoding="utf-8"))
for name, body in blocks:
    for species in re.findall(r'c\("([^"]+)"', body):
        methods[species] = name
    # allow inline rows following the same section until next comment
for species, _, _ in rows:
    if species not in methods:
        problems.append(f"{species}: no method section")

print("rows", len(rows), "methods", sorted(set(methods.values())))
print("problems", len(problems))
for p in problems:
    print("BAD", p)
if not problems:
    print("PASS: propagation stock chain")
