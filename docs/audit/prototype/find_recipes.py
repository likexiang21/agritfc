import pathlib
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus")
for key in ("mushroom_bag", "nursery_tray", "spice_trellis", "silkworm_rack"):
 print("====", key)
 for p in base.rglob("*.json"):
  s=p.read_text(encoding="utf-8", errors="ignore")
  if key in s:
   print(p.relative_to(base))
