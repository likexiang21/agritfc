# 587 交互去 UI 化：移除弹出式提示文本技术分析

> 日期：2026-10-30
> 状态：**静态实现；未实机**
> 用户要求：交互尽可能去 UI 化，减少弹出式提示文本。

## 1. 移除范围

全项目搜索 `displayClientMessage`，共 **13 处**，已全部移除：

| 文件 | 移除内容 |
|---|---|
| `KnifeRackBlock` | full / invalid / empty |
| `MushroomBagBlock` | natural_only / spent / too_cold / too_hot / growing |
| `DirectSeedPlantingGate` | planting.method |
| `CuttingBoardInteractions` | durability / occupied / dough_controls / dough_not_formed / empty / worn / rotten / no_recipe |
| `DryingRackInteractions` | empty / not_ready / rotten / no_recipe / full |
| `MortarInteractions` | full / empty / rotten / no_recipe / progress |
| `PanInteractions` | status / no_heat / no_oil / full / not_ready / not_ingredient |

## 2. 替代反馈

- 方块状态/物品状态本身体现结果：
  - 案板有/无物品、是否成型；
  - 石臼研磨进度；
  - 晾架完成/未完成；
  - 菌包 stage；
  - 平底锅内容物/油；
- 已有声音反馈保留：
  - `ITEM_PICKUP`、`WOOD_PLACE`、`BREWING_STAND_BREW` 等。

## 3. 保留的 UI

- 厨房家具的容器菜单/屏幕仍保留（存储需要容器界面）；
- 养蚕架复用 TFC 容器 UI；
- 其余设备（平底锅、案板、石臼、晾架、菌包、刀架、育苗盘）均为直接交互，无设备 UI。

## 4. 行为变化

- 无效操作现在**静默失败**，不再弹 action bar；
- 不再有育苗/种植方式的 action bar 提示；
- 玩家需要根据方块状态/物品状态判断。

## 5. 校验

```text
displayClientMessage files 0
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 6. 未完成

- 未实机验证“静默失败”是否造成玩家困惑；
- 未移除语言文件里已不再使用的 message keys；
- 未新增动作音效替代所有被移除提示。
