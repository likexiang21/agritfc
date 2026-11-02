# 522 P1-2 厨房家具功能分化技术分析

> 日期：2026-10-29
> 状态：**部分静态修复；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

用户报告：

- 厨房家具全部是几乎完全相同的套皮容器；
- 6 个种类共用同一 BE/Menu/Screen，功能无差异。

确认：

- 6 种全部使用 `KitchenStorageBlockEntity`；
- 全部 9 格；
- 全部接受任意物品；
- 全部堆叠上限 64；
- 除名称/模型外没有功能区别。

## 2. 本次分化

仍保留 **9 格统一菜单/屏幕**（避免引入未验证的 GUI 布局），但 BE 按
`KitchenStorageBlock.StorageKind` 实施不同规则：

| 家具 | 槽位过滤 | 堆叠上限 |
|---|---|---:|
| counter_cabinet | 任意物品 | 64 |
| half_cabinet | 任意物品 | 16 |
| sink_cabinet | 只接受带 `Capabilities.FluidHandler.ITEM` 的容器 | 1 |
| spice_rack | 只接受 `#tfcagricultureplus:spices` | 64 |
| food_display | 只接受带 `minecraft:food` 组件的食物 | 64 |
| fruit_bowl | 只接受食物 | 1 |

同时：

- `getDisplayName()` 按种类返回不同名称；
- 新增 6 × 2 个 `block_entity.tfcagricultureplus.kitchen_storage.<kind>` 语言键；
- 新增 `data/tfcagricultureplus/tags/item/spices.json`，40 项：
  - 20 个 `spice/*`
  - 20 个 `ground_spice/*`

## 3. 这仍然不是完整方案

- 6 种仍然共用同一个 9 格菜单与同一个屏幕，UI 没有差异化；
- sink 只接受流体容器，**没有实现水槽水箱/清洗交互**；
- food_display 没有保鲜逻辑；
- spice_rack 没有可视化调料摆放；
- 因此状态只能是 **partially-fixed-static**，不能声称家具已经“功能完成”。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
check_tag_refs: B tag missing refs 0
final_static_audit problems 0
lang en_us 1086 / zh_cn 1086
```

## 5. 未完成

- 实机；
- 独立 GUI/容量布局；
- sink 水箱；
- 食物保鲜；
- 香料架可视化；
- 家具配方仍为 204 个占位配方（另案）。
