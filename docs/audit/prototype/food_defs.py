import pathlib
base=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/tfc/food")
for key in ("nut","spice","mushroom","adult_silkworm","cocoon"):
 print("====",key, key in str([p.name for p in base.glob('*.json')]))
 print([p.name for p in base.glob('*.json') if key in p.name][:20])
