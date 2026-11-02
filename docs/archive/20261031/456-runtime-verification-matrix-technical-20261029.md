# 456 作物系统实机验证矩阵 P0-CF 技术分析

> 日期：2026-10-29
> 目标：把当前全部实机证据与未完成项整理成一张验收矩阵。
> 约束：不推送；不伪造。

## 1. 已验证

| 项目 | 证据 | 状态 |
|---|---|---|
| 客户端加载/worldgen codec | 410/411 | ✅ |
| 注册表计数 spiceCrops15/spiceTrees5/cropWaste82/wildMushrooms15 | 414/415 | ✅ |
| 方块放置（nursery/strawberry/leaves/mushroom/trellis/sapling/bag） | 412/413 | ✅ |
| 玩家支撑放置（basil/cardamom/strawberry/tree saplings） | 416/417 | ✅ |
| basil 生长 age7 | 418/419 | ✅ |
| mushroom bag stage2 | 418/419 | ✅ |
| nursery tray stage2 | 418/419 | ✅ |
| nut tree 3 种 | 446/447 + 450/451 | ✅ |
| spice tree 5 种 | 448/449 + 450/451 | ✅ |
| 树叶 persistent=true 保留 | 452-455 | ✅ |
| 玩家破坏收获（basil/strawberry/TFC wheat/A napa） | 458-463 | ✅ |
| 收获掉落物 ID（grain_bundle/crop_waste/spice 等） | 460/461 | ✅ |
| 未成熟作物不掉产品/种子 | 464/465 | ✅ |
| 菌包右键采集 | 466/467 | ✅ |
| 育苗盘右键产出 seedling | 466-469 | ✅ |
| seedling 移栽到耕地 | 480/481 | ✅ |
| 3 个蘑菇 worldgen feature 执行 | 474/475 | ✅ |
| 最终 jar 加载 + 旧存档 smoke | 472-477, 482/483 | ✅ |

## 2. 部分验证

- 树叶 non-persistent 衰减：有 nut drop 线索，方块状态未确认；
- 树冠位置遍历：只确认存在，不保证所有位置；
- 部分树种 LEAF1-3 检查未命中外，leaves 计数已确认；
- 自然世界生成（非 /place feature）未验证；
- 移栽后的生长/成熟/收获未验证。

## 3. 未验证

- 自然蘑菇/树木群系分布；
- 育苗移栽后完整生长→收获；
- 树叶掉落物 ID/数量；
- 全量 159 行验收；
- 视觉/平衡；
- 长时间稳定性。

## 4. 结论

代码已具备注册/资源/生长/收获/育苗/树/菌包交互的主链实机证据。
**自然生成、移栽后全链、视觉/平衡与全量验收仍未完成，不能宣称目标完成。**
