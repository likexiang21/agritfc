import pathlib
new_size, new_hash = "2,948,127", "6C8C154D718617ECC0C5283A03660DE4D7871480E752DF172EF7BDE85EC39E7D"
old = [
 ("2,942,138","38CD6A2E1366512C28A850E05C84A77341C53234D9D2A0A5AA6C4A619D69DD71"),
 ("2,942,463","C40DAA1A5E9BB10118C7F96E8041D76A3ED08E29BCB97051B1B2B0CBDC657F43"),
]
for p in pathlib.Path("mod_rebuild/docs").glob("68*.md"):
 t=p.read_text(encoding="utf-8"); changed=False
 for osz,oh in old:
  if osz in t or oh in t:
   t=t.replace(osz,new_size).replace(oh,new_hash); changed=True
 if changed: p.write_text(t,encoding="utf-8"); print(p.name)
