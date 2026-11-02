import pathlib
old_size, old_hash = "2,948,863", "2614DC47667DDAC4FCBE4F2A9514841D8957543130757C1BBD67F2B7AA9CDEBF"
new_size, new_hash = "2,953,314", "E0D82FEA3F446A98ECD5967A6A8621A85904F130F768DBAD1FF6B09D9AC0F312"
for pattern in ("68*.md","69*.md"):
 for p in pathlib.Path("mod_rebuild/docs").glob(pattern):
  t=p.read_text(encoding="utf-8")
  if old_size in t or old_hash in t:
   p.write_text(t.replace(old_size,new_size).replace(old_hash,new_hash),encoding="utf-8"); print(p.name)
