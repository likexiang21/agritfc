import pathlib
old_size, old_hash = "2,953,314", "E0D82FEA3F446A98ECD5967A6A8621A85904F130F768DBAD1FF6B09D9AC0F312"
new_size, new_hash = "2,954,635", "0EFAF078B8BE4A30CF5D8997CB47DDAB293F33DF9C3B52B2F112CD4A97224E61"
for pattern in ("68*.md","69*.md"):
 for p in pathlib.Path("mod_rebuild/docs").glob(pattern):
  t=p.read_text(encoding="utf-8")
  if old_size in t or old_hash in t:
   p.write_text(t.replace(old_size,new_size).replace(old_hash,new_hash),encoding="utf-8"); print(p.name)
