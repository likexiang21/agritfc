import pathlib
base=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/models/item")
for pat in ("crop_waste/*", "spice_waste/*"):
 print(pat, len(list(base.glob(pat))))
for p in base.glob("crop_waste/*"):
 if any(x in p.name for x in ("cocoa","fig","grape","pineapple","nightshade")):
  print(p.name)
