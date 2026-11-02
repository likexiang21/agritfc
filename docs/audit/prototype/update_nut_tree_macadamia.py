from pathlib import Path

for name in ("generate_nut_tree_resources.py", "generate_nut_tree_worldgen.py"):
    p = Path("mod_rebuild/docs/audit/prototype") / name
    t = p.read_text(encoding="utf-8")
    t = t.replace('("pistachio", "cashew")', '("pistachio", "cashew", "macadamia")')
    p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/audit/prototype/validate_crop_p0a.py")
t = p.read_text(encoding="utf-8")
t = t.replace('nut_trees = ["pistachio", "cashew"]', 'nut_trees = ["pistachio", "cashew", "macadamia"]')
p.write_text(t, encoding="utf-8")
print("updated")
