# 614 剩余占位图标审计：103 个 `tfc:item/straw`

> 日期：2026-10-30
> 状态：**审计完成；未修改**
> 约束：不实机、不处理视觉、不推送。

## 1. 扫描结果

扫描 `assets/tfcagricultureplus/models/item/**`：

```text
仍然 layer0 = tfc:item/straw：103 个
```

分类：

| 类别 | 数量 |
|---|---:|
| `spice/*` | 20 |
| `ground_spice/*` | 20 |
| `spice_waste/*` | 20 |
| `spice_seed/*` | 15 |
| `ground_nut/*` | 8 |
| `nut_shell/*` | 8 |
| 坚果根物品（acorn 等） | 8 |
| `seedling`、`wet_grass` | 2 |
| `spice_corm/saffron`、`spice_root/cardamom` | 2 |
| **合计** | **103** |

## 2. 为什么没有继续映射

这些物品没有现成的、可区分的上游贴图：

- TFC/A 没有香料/坚果的独立 item texture；
- 香料作物方块贴图本身是 `tfc:block/crop/wheat_7` 占位；
- 继续复用 `tfc:item/straw` 或小麦贴图只会把“同一张图”问题换个名字。

要真正解决，需要：

- 小规模绘制 103 个 16×16 图标；或
- 用户明确接受占位。

## 3. 影响

- OPEN-005 的“名称”已修复；
- 图标仍有 103 个占位，不能声称视觉完成。

## 4. 未完成

- 未改任何图标；
- 未实机。
