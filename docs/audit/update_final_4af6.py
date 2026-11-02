from pathlib import Path
old_size, old_hash = "2,973,199", "210C5BEF309F8F68887F3B87BC14F7A6D9243D0F8340D8FDBA4BBAB1E64D704E"
new_size, new_hash = "2,973,658", "4AF65C57A47C7D43550E3165D0D80B159D9CD2FA71A3D929EFF5C42B643FFAA0"
for name in ("mod_rebuild/docs/最终审计与修复报告-20261031.md","mod_rebuild/docs/验证记录-20261031.md","mod_rebuild/README.md"):
 p=Path(name); t=p.read_text(encoding="utf-8")
 t=t.replace(old_size,new_size).replace(old_hash,new_hash)
 p.write_text(t,encoding="utf-8"); print(name)
p=Path("mod_rebuild/docs/最终审计与修复报告-20261031.md"); t=p.read_text(encoding="utf-8")
t += """

## 6. 2026-11-02 低峰批次（继续 P0→P1→P2）

本轮按 OPEN-ISSUES/510/511 教训继续，只修代码/数据，不绘制贴图。

### 作物
- `GrainCrop` 年龄修正：A 9 个谷物最大 age=7，TFC maize=5；
- 树苗生成：树干替换树苗、树叶非永久、空间检查、移除每树 INFO 日志；
- TFC 草莓右键采摘补 B 种子/废枝叶；
- 香料链：`foods/ground_spices` 加入 20 个 ground_spice，新增 `food/ground_black_pepper` 研磨配方；
- 世界生成：23 个 placed feature 增加 `rarity_filter` 与 `tfc:climate`。

### 设备/数据
- 晾架批量产量按输入数量放大，修复 8 件进 1 件出；
- 刀架破坏改为逐件取放，修复非玩家破坏丢物品；
- 餐盘碰撞箱改为 1px 薄板；
- 晾架/石臼/切割板补齐 action bar 提示和语言键；
- 育苗盘增加 BE 同步；完成态破坏掉幼苗而不是只掉种子；
- 可放置食物满份掉落保留 `pieFood` 新鲜度；BER 不再重复渲染方块自身；
- `TimberBlocks.ALL` 补 `lumber_pile`；
- 新增 `tfcfarmingplus:materials/plant_fibers` B 侧 tag；
- pimento 树叶 `palm_fluff` 改为存在的 `mangrove_fluff`；
- 坚果/香料叶注册客户端草色 tint。

### 仍未修/未验证
- 视觉占位（按用户要求不绘制贴图）；
- 运行期全部未验证；
- TFC/AFC 坚果叶仍只有数据状态，无 TFC/AFC 专属视觉挂果。
"""
t=t.replace("当前 jar：\n\n```text\n2,973,199 bytes","当前 jar：\n\n```text\n2,973,658 bytes")
p.write_text(t,encoding="utf-8"); print("report")
