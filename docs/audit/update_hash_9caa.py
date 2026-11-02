import pathlib
old_size, old_hash = "2,954,635", "0EFAF078B8BE4A30CF5D8997CB47DDAB293F33DF9C3B52B2F112CD4A97224E61"
new_size, new_hash = "2,954,689", "9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A"
for pattern in ("68*.md","69*.md","70*.md"):
 for p in pathlib.Path("mod_rebuild/docs").glob(pattern):
  t=p.read_text(encoding="utf-8")
  if old_size in t or old_hash in t:
   p.write_text(t.replace(old_size,new_size).replace(old_hash,new_hash),encoding="utf-8"); print(p.name)
