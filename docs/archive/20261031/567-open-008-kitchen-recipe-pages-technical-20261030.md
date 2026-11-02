# 567 OPEN-008 扩展：厨房手册 recipe/spotlight 页技术分析

> 日期：2026-10-30
> 状态：**静态内容补全；未实机**
> 约束：不实机、不推送。

## 1. 背景

厨房手册 `agriculture_plus_kitchen/intro` 只有文字页，没有配方页。
玩家无法在手册里看到 6 种家具的合成图案、金属罐与陶盘的用途。

## 2. 新增页

### patchouli:crafting ×6

| 家具 | recipe |
|---|---|
| counter_cabinet | `tfcagricultureplus:kitchen/counter_cabinet/oak` |
| half_cabinet | `tfcagricultureplus:kitchen/half_cabinet/oak` |
| sink_cabinet | `tfcagricultureplus:kitchen/sink_cabinet/oak` |
| spice_rack | `tfcagricultureplus:kitchen/spice_rack/oak` |
| food_display | `tfcagricultureplus:kitchen/food_display/oak` |
| fruit_bowl | `tfcagricultureplus:kitchen/fruit_bowl/oak` |

这些是原版 `crafting_shaped`，Patchouli crafting 页可以直接显示。

### spotlight ×2

- `metal_can/copper`：500 mB、图标显示液体、桶/罐装取；
- `plate/ceramic`：打制→烧制→放置装菜，保存菜品。

中英双语。

## 3. 校验

- 6 个 recipe ID 全部存在；
- `final_static_audit` problems 0；
- `gradle build` 成功。

## 4. 未完成

- 未实机检查 recipe 页渲染；
- 未给所有 34 木材家具各做一页（只展示 oak 代表）；
- 未处理视觉。
