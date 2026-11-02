from pathlib import Path

p = Path("mod_rebuild/docs/audit/prototype/validate_crop_p0a.py")
if "PASS: spice root resources" not in p.read_text(encoding="utf-8"):
    p.write_text(p.read_text(encoding="utf-8") + '''
# P0-AU root-form spice propagule (cardamom).
assert (assets / "models/item/spice_root/cardamom.json").is_file()
for lang in ("en_us.json", "zh_cn.json"):
    lang_data = json.loads((assets / "lang" / lang).read_text(encoding="utf-8"))
    assert "item.tfcagricultureplus.spice_root.cardamom" in lang_data
print("PASS: spice root resources")
''', encoding="utf-8")
print("validator appended")
