from pathlib import Path

p = Path("mod_rebuild/docs/audit/prototype/validate_crop_p0a.py")
t = p.read_text(encoding="utf-8")
old = '''# 20 spice crops: real CropBlock age 0..7, seed item places it, product/seed loot.
spices = ["basil", "bay_laurel", "cardamom", "cilantro", "cumin", "oregano", "pimento", "vanilla",
          "black_pepper", "cinnamon", "clove", "nutmeg", "saffron", "star_anise", "rosemary",
          "thyme", "sage", "dill", "fennel", "mustard"]
with zipfile.ZipFile(tfc_jar) as z:
    assert "assets/tfc/textures/block/crop/wheat_7.png" in set(z.namelist())
for spice in spices:
    crop_path = "spice_crop/" + spice
'''
new = '''# 15 crop-form spices + 5 tree-form spices.
spices = ["basil", "bay_laurel", "cardamom", "cilantro", "cumin", "oregano", "pimento", "vanilla",
          "black_pepper", "cinnamon", "clove", "nutmeg", "saffron", "star_anise", "rosemary",
          "thyme", "sage", "dill", "fennel", "mustard"]
tree_spices = {"pimento", "cinnamon", "clove", "nutmeg", "star_anise"}
crop_spices = [s for s in spices if s not in tree_spices]
with zipfile.ZipFile(tfc_jar) as z:
    assert "assets/tfc/textures/block/crop/wheat_7.png" in set(z.namelist())
for spice in crop_spices:
    crop_path = "spice_crop/" + spice
'''
if old not in t:
    raise SystemExit("anchor crop loop not found")
t = t.replace(old, new, 1)
t = t.replace('f"20 spice crops, 20 ground spices, 8 ground nuts, 8 nut shells, tags valid")',
              'f"15 spice crops, 5 spice trees, 20 ground spices, 8 ground nuts, 8 nut shells, tags valid")')
p.write_text(t, encoding="utf-8")
print("validator crop count updated")
