from pathlib import Path
old_size, old_hash = "2,964,868", "20D552970AEFBE29EBA127A20E52038DE8943709A2A1522EB6D9F24CF2E229AC"
new_size, new_hash = "2,968,028", "672E5A4528D4F9EB492E79AB97EACC8818D93193E0C77BF694DC8FD504482D65"
for name in ("mod_rebuild/docs/最终审计与修复报告-20261031.md","mod_rebuild/docs/验证记录-20261031.md","mod_rebuild/README.md"):
 p=Path(name); t=p.read_text(encoding="utf-8")
 t=t.replace(old_size,new_size).replace(old_hash,new_hash).replace("json 6560 / models 3734","json 6563 / models 3737")
 p.write_text(t,encoding="utf-8"); print(name)
p=Path("mod_rebuild/docs/最终审计与修复报告-20261031.md"); t=p.read_text(encoding="utf-8")
t=t.replace("- 菌包/育苗盘按 stage 使用不同模型；","- 菌包/育苗盘按 stage 使用不同模型；\n- 干燥架/石臼/育苗盘/木料堆/可放置食物增加 BER，内容物客户端可见；")
t=t.replace("- 15 个香料作物 + 草莓的 8 个 age 使用不同模型（复用 TFC wheat age 贴图，暂无物种专属贴图）；","- 15 个香料作物 + 草莓的 8 个 age、15 个野生蘑菇的 3 个 age 使用不同模型；")
t=t.replace("  - 干燥架/石臼/育苗盘/菌包/木料堆/可放置食物无 BER，内容物客户端不可见；\n","  - 蚕架内容物仍无 BER；\n")
p.write_text(t,encoding="utf-8"); print("report updated")
