from pathlib import Path
p = Path(r"mod_rebuild/tfcagricultureplus/src/main/templates/META-INF/neoforge.mods.toml")
t = p.read_text(encoding="utf-8")
t = t.replace("102 crop-waste", "82 crop-waste")
p.write_text(t, encoding="utf-8")
print("updated")
