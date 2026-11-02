from pathlib import Path
old_size, old_hash = "2,971,428", "4432EF5FAB636F54AAC1C84BF234784086EC36837A68B37CF701C3148E1DCDD9"
new_size, new_hash = "2,973,199", "210C5BEF309F8F68887F3B87BC14F7A6D9243D0F8340D8FDBA4BBAB1E64D704E"
for name in ("mod_rebuild/docs/最终审计与修复报告-20261031.md","mod_rebuild/docs/验证记录-20261031.md","mod_rebuild/README.md"):
 p=Path(name); t=p.read_text(encoding="utf-8")
 t=t.replace(old_size,new_size).replace(old_hash,new_hash)
 p.write_text(t,encoding="utf-8"); print(name)
p=Path("mod_rebuild/docs/最终审计与修复报告-20261031.md"); t=p.read_text(encoding="utf-8")
t=t.replace("- 静态视觉 P0：**仍未清零**：19 个香料/草莓/蘑菇方块模型仍复用 TFC wheat 贴图，103 个物品仍复用 `tfc:item/straw`，树叶 tint 已补但物种贴图仍为占位。","- 按用户要求**不绘制贴图**；视觉/贴图占位不作为本轮代码修复目标，仍记录为资源边界。")
p.write_text(t,encoding="utf-8"); print("report")
