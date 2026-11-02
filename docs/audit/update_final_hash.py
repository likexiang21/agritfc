from pathlib import Path
old_size, old_hash = "2,964,204", "D23DA4A7CD9A15106A634711A88D6D8A98E1AEDA563882881A511332B4AFB6B4"
new_size, new_hash = "2,964,868", "20D552970AEFBE29EBA127A20E52038DE8943709A2A1522EB6D9F24CF2E229AC"
for name in ("mod_rebuild/docs/最终审计与修复报告-20261031.md","mod_rebuild/docs/验证记录-20261031.md","mod_rebuild/README.md"):
 p=Path(name); t=p.read_text(encoding="utf-8")
 t=t.replace(old_size,new_size).replace(old_hash,new_hash)
 p.write_text(t,encoding="utf-8"); print(name)
