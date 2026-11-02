from pathlib import Path
p = Path("mod_rebuild/docs/audit/prototype/build_agriculture_name_map.py")
t = p.read_text(encoding="utf-8")
t = t.replace('return (manual_zh if lang == "zh" else manual_en).get(species) or (a[lang].get(species))',
              'return (manual_zh if lang == "zh" else manual_en).get(species) or (a["zh_cn" if lang == "zh" else "en_us"].get(species))')
p.write_text(t, encoding="utf-8")
print("fixed")
