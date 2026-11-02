import zipfile, json
from pathlib import Path

mods = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods")
out = {}
for jar_name in ["TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar", "afc-2.1.3-1.21.1.jar"]:
    p = mods / jar_name
    if not p.exists():
        continue
    with zipfile.ZipFile(p) as z:
        langs = [n for n in z.namelist() if n.endswith("lang/zh_cn.json")]
        for lang_path in langs:
            try:
                d = json.loads(z.read(lang_path).decode("utf-8"))
            except Exception as e:
                print("skip", lang_path, e)
                continue
            for k, v in d.items():
                if k.startswith("block.") and (".wood.log." in k or ".wood.planks." in k):
                    species = k.rsplit(".", 1)[-1]
                    out.setdefault(species, v)
Path("mod_rebuild/docs/audit/prototype/wood_names.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("count", len(out))
