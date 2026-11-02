# 540 P1-2 扩展：水槽罐与家具掉落表复核技术分析

> 日期：2026-10-29
> 状态：**静态实现；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 水槽柜功能补充

之前 P1-2 只做到：

- 6 种家具不同过滤/堆叠；
- sink 只接受流体容器。

本轮补充：

- `KitchenStorageBlockEntity` 为 `SINK_CABINET` 增加 4000 mB 水罐；
- 只接受 `minecraft:water`；
- `saveAdditional` / `loadAdditional` 持久化；
- 注册 block capability：
  - `Capabilities.ItemHandler.BLOCK`；
  - `Capabilities.FluidHandler.BLOCK`（非 sink 返回 null）。

因此水槽柜现在可以被管道/外部容器注水/抽水；但**没有 GUI 水槽界面**，玩家不能直接用水桶交互。

## 2. 家具掉落表复核

原 D2 审计说“389 个方块无 loot table”，P0-3 文档据此写了“家具掉落表仍缺”。

实际复核：

```text
counter_cabinet 34
half_cabinet 34
sink_cabinet 34
spice_rack 34
food_display 34
fruit_bowl 34
```

= **204 个家具 loot table 已存在**，每个掉落自身。

因此修正：

- OPEN-004 的“家具掉落表仍缺”是**错误描述**；
- 家具掉落表应标为已存在；
- 仍需实机验证掉落。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6442 / bad 0
final_static_audit problems 0
furniture loot tables 204
```

## 4. 未完成

- 未实机验证 sink 水罐；
- 未实现水槽 GUI / 水桶交互 / 清洗逻辑；
- 未实机验证家具掉落；
- 未处理视觉。
