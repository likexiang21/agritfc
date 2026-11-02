from pathlib import Path

p = Path("mod_rebuild/docs/audit/prototype/generate_nut_tree_resources.py")
t = p.read_text(encoding="utf-8")
t = t.replace('species = ["pistachio", "cashew"]', 'species = ["pistachio", "cashew", "macadamia"]')
p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/audit/prototype/generate_nut_tree_worldgen.py")
t = p.read_text(encoding="utf-8")
t = t.replace(
    '["tfcagricultureplus:nut_sapling_pistachio", "tfcagricultureplus:nut_sapling_cashew"]',
    '["tfcagricultureplus:nut_sapling_pistachio", "tfcagricultureplus:nut_sapling_cashew", "tfcagricultureplus:nut_sapling_macadamia"]'
)
p.write_text(t, encoding="utf-8")
print("scripts fixed")
