from pathlib import Path
old_size, old_hash = "2,968,409", "D8F283B4DE00DD17103F209579CC44D8C602F74F8558B68B93CDF01068C6C5CA"
new_size, new_hash = "2,971,428", "4432EF5FAB636F54AAC1C84BF234784086EC36837A68B37CF701C3148E1DCDD9"
for name in ("mod_rebuild/docs/最终审计与修复报告-20261031.md","mod_rebuild/docs/验证记录-20261031.md","mod_rebuild/README.md"):
 p=Path(name); t=p.read_text(encoding="utf-8")
 t=t.replace(old_size,new_size).replace(old_hash,new_hash)
 t=t.replace("json 6563 / models 3737","json 6565 / models 3737")
 t=t.replace("lang en_us 1120 / zh_cn 1120","lang en_us 1125 / zh_cn 1125")
 p.write_text(t,encoding="utf-8"); print(name)
p=Path("mod_rebuild/docs/最终审计与修复报告-20261031.md"); t=p.read_text(encoding="utf-8")
t=t.replace("- 静态 P0：已清零（本轮修复了统一收获器 BlockEntity 参数、B 香料/草莓 TFC 耕地存活、世界生成 biome 过滤）。","- 静态逻辑 P0：已修复（统一收获器 BlockEntity 参数、B 香料/草莓 TFC 耕地存活、世界生成 biome 过滤、晾架批量产量、谷物年龄、树苗生长、pimento 贴图、A 纤维标签）。\n- 静态视觉 P0：**仍未清零**：19 个香料/草莓/蘑菇方块模型仍复用 TFC wheat 贴图，103 个物品仍复用 `tfc:item/straw`，树叶 tint 已补但物种贴图仍为占位。")
p.write_text(t,encoding="utf-8"); print("report")
