from pathlib import Path
p=Path("mod_rebuild/docs/audit/OPEN-ISSUES.md"); t=p.read_text(encoding="utf-8")
t += """

## OPEN-056 2026-11-02 低峰批次：作物/设备/数据代码修复

**状态：fixed-static / 待实机**

- 谷物 age：A 9 种 7、TFC maize 5，修复玉米包不可达与提前收获；
- 树苗：树干替换树苗、树叶非永久、空间检查、去日志；
- 晾架批量产量按输入数量放大；
- 刀架逐件取放；餐盘 1px 碰撞；晾架/石臼/案板 actionbar；
- 育苗盘 BE 同步、完成态破坏掉幼苗；
- 可放置食物满份掉落保留新鲜度，BER 不再重复渲染；
- `TimberBlocks.ALL` 补 lumber_pile；
- 补 `tfcfarmingplus:materials/plant_fibers` tag；
- pimento 贴图路径修复；坚果/香料叶草色 tint；
- 香料链 ground_spice 消费端 + black_pepper 配方；
- 世界生成 rarity + climate；
- TFC 草莓右键补 B 种子/废枝叶；
- 证据：最终审计报告 §6；构建成功；jar 见验证记录。
"""
p.write_text(t,encoding="utf-8"); print("OPEN-056 appended")
# mark OPEN-049 partially fixed with note
t=p.read_text(encoding="utf-8")
t=t.replace("**状态：部分修复 / 仍待处理**","**状态：部分修复 / TFC 草莓右键已补，TFC/AFC 叶视觉与工业作物废料仍按边界保留**")
p.write_text(t,encoding="utf-8"); print("OPEN-049 updated")
