# 548 OPEN-008 手册可读性扩展：spotlight 页技术分析

> 日期：2026-10-29
> 状态：**静态内容补全；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 背景

P1-3 已为手册新增 7 个作物主题，但全部是纯文字页，缺少物品锚点。

本轮为每个主题追加 **patchouli:spotlight** 页，提供可点击/可查看的物品入口。

## 2. 新增页

| entry | spotlight |
|---|---|
| overview | `crop_waste/spinach` |
| nursery | `nursery_tray`, `seedling` |
| grain | `grain_bundle/wheat`, `wet_grass` |
| spices | `spice/basil`, `ground_spice/basil` |
| nuts | `pistachio`, `nut_sapling/pistachio` |
| mushrooms | `mushroom_bag`, `wild_mushroom/oyster` |
| bushes | `bush_waste/blackberry` |

中英双语，共 14 个 spotlight 页。

## 3. 校验

- `check_patchouli_spotlights.py`：bad spotlight items **0**
- `check_patchouli_icons.py`：bad icons **0**
- JSON 6484 / bad 0
- `final_static_audit` problems 0
- `gradle build` 成功

## 4. 未完成

- 没有 recipe pages（Patchouli 的 crafting 页不适用于 B 的自定义配方类型）；
- 未实机检查分页/点击；
- 旧三主题未重写；
- 视觉未处理。
