from pathlib import Path
old_size, old_hash = "2,968,028", "672E5A4528D4F9EB492E79AB97EACC8818D93193E0C77BF694DC8FD504482D65"
new_size, new_hash = "2,968,193", "B9EEE569957ED2F3764B9DA1FE19755A5413EF60E7BF1BCB64C18735A986160C"
for name in ("mod_rebuild/docs/最终审计与修复报告-20261031.md","mod_rebuild/docs/验证记录-20261031.md","mod_rebuild/README.md"):
 p=Path(name); t=p.read_text(encoding="utf-8")
 t=t.replace(old_size,new_size).replace(old_hash,new_hash)
 p.write_text(t,encoding="utf-8"); print(name)
p=Path("mod_rebuild/docs/最终审计与修复报告-20261031.md"); t=p.read_text(encoding="utf-8")
t=t.replace("- 蚕架内容物仍无 BER；\n","")
t=t.replace("- 干燥架/石臼/育苗盘/木料堆/可放置食物增加 BER，内容物客户端可见；","- 干燥架/石臼/育苗盘/木料堆/可放置食物/蚕架增加 BER，内容物客户端可见；")
p.write_text(t,encoding="utf-8"); print("report")
