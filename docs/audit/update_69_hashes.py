import pathlib
old_size, old_hash = "2,942,138", "38CD6A2E1366512C28A850E05C84A77341C53234D9D2A0A5AA6C4A619D69DD71"
new_size, new_hash = "2,948,127", "6C8C154D718617ECC0C5283A03660DE4D7871480E752DF172EF7BDE85EC39E7D"
for p in pathlib.Path("mod_rebuild/docs").glob("69*.md"):
 t=p.read_text(encoding="utf-8")
 if old_size in t or old_hash in t:
  p.write_text(t.replace(old_size,new_size).replace(old_hash,new_hash),encoding="utf-8"); print(p.name)
