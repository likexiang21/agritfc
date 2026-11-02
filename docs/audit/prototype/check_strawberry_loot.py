import pathlib
base=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/loot_table/blocks")
for n in ("crop/strawberry.json","crop","strawberry.json"):
 p=base/n
 print(n,p.exists())
if (base/"crop/strawberry.json").exists(): print((base/"crop/strawberry.json").read_text(encoding="utf-8"))
