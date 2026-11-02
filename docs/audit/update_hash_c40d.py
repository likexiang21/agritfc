import pathlib
old_size, old_hash = "2,942,138", "38CD6A2E1366512C28A850E05C84A77341C53234D9D2A0A5AA6C4A619D69DD71"
new_size, new_hash = "2,942,463", "C40DAA1A5E9BB10118C7F96E8041D76A3ED08E29BCB97051B1B2B0CBDC657F43"
for p in pathlib.Path("mod_rebuild/docs").glob("68*.md"):
    t = p.read_text(encoding="utf-8")
    if old_hash in t or old_size in t:
        t = t.replace(old_size, new_size).replace(old_hash, new_hash)
        p.write_text(t, encoding="utf-8")
        print(p.name)
