import pathlib
p=pathlib.Path(r"mod_rebuild/docs")
files=sorted(p.glob("*.md"))
print(len(files))
for f in files[:10]: print(f.name)
print('...')
for f in files[-10:]: print(f.name)
