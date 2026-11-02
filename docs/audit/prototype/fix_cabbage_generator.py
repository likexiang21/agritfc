from pathlib import Path
p = Path("mod_rebuild/docs/audit/prototype/generate_crop_waste_resources.py")
t = p.read_text(encoding="utf-8")
t = t.replace("assert len(rows) == 81, len(rows)", "rows.append((\"cabbage\", \"tfc:compost_greens/high\"))\nassert len(rows) == 82, len(rows)")
p.write_text(t, encoding="utf-8")
print("generator updated")
