# 523 P1-2 厨房家具功能分化工作报告

> 日期：2026-10-29
> 状态：**部分静态修复；未实机**
> 范围：P1-2。

## 1. 完成

- 6 种家具按 `StorageKind` 区分槽位过滤/堆叠上限；
- 6 种独立 `getDisplayName()`；
- 新增 40 项香料 tag；
- `gradle build` 成功。

## 2. 规则

```text
counter_cabinet : 任意物品 / 64
half_cabinet    : 任意物品 / 16
sink_cabinet    : 仅流体容器 / 1
spice_rack      : 仅 #tfcagricultureplus:spices / 64
food_display    : 仅食物 / 64
fruit_bowl      : 仅食物 / 1
```

## 3. 明确未做

- 未实机；
- 未改 GUI 布局；
- 未实现水箱/保鲜/可视化；
- 未改 204 个家具占位配方。

## 4. 证据

- `KitchenStorageBlockEntity`
- `tags/item/spices.json`
- 522 技术分析
