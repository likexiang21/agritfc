from pathlib import Path
old_size, old_hash = "2,968,409", "D8F283B4DE00DD17103F209579CC44D8C602F74F8558B68B93CDF01068C6C5CA"
# docs currently have 2,968,193/B9EE... or 2,968,193? replace both
pairs = [("2,968,193","B9EEE569957ED2F3764B9DA1FE19755A5413EF60E7BF1BCB64C18735A986160C"), ("2,968,409","D8F283B4DE00DD17103F209579CC44D8C602F74F8558B68B93CDF01068C6C5CA")]
for name in ("mod_rebuild/docs/最终审计与修复报告-20261031.md","mod_rebuild/docs/验证记录-20261031.md","mod_rebuild/README.md"):
 p=Path(name); t=p.read_text(encoding="utf-8")
 for osz,oh in pairs[:1]: t=t.replace(osz,old_size).replace(oh,old_hash)
 t=t.replace("lang en_us 1107 / zh_cn 1107","lang en_us 1120 / zh_cn 1120")
 p.write_text(t,encoding="utf-8"); print(name)
p=Path("mod_rebuild/docs/最终审计与修复报告-20261031.md"); t=p.read_text(encoding="utf-8")
t=t.replace("- 锅/水槽破坏时把油/水转为可回收流体容器（金属罐/水桶），不再静默清空；\n","")
t=t.replace("- **仍存在 P2**：\n","- **设计边界**：破坏锅/水槽时内部流体随容器消失（按用户确认，不视为缺陷）；\n- **仍存在 P2**：\n")
p.write_text(t,encoding="utf-8"); print("report")
