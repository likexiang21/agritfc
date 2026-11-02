import zipfile, json
from pathlib import Path

p = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\TFCFarmingPlus-NeoForge-1.21.1-0.1.0.jar")
with zipfile.ZipFile(p) as z:
    d = json.loads(z.read("assets/tfcfarmingplus/lang/zh_cn.json").decode("utf-8"))
out = {}
for k, v in d.items():
    if k.startswith("item.tfcfarmingplus.food."):
        out[k.rsplit(".", 1)[1]] = v
Path("mod_rebuild/docs/audit/prototype/a_food_names.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("count", len(out))
