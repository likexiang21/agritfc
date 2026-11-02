# 518 P0-4 逐物种人工名称技术分析

> 日期：2026-10-29
> 状态：**静态修复完成；未实机；不改贴图**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

用户报告：

- 农业内容名称不可读；
- 大量 `作物废枝叶（ID）`、`谷物捆（ID）`、`香料（ID）`、`坚果（ID）`；
- 存在未翻译片段；
- 创造页整页同名同贴图。

## 2. 本次原则

- **不再拼接原始 ID**；
- 逐物种使用 TFC/A 已有中文名，人工补充 B 独有物种；
- 中英双语同步；
- **不重画贴图**（用户已明确暂不处理视觉）；
- 不改变物品注册 ID/数量，仅改 lang 与显示名。

## 3. 名称覆盖

### 3.1 农业物品（246 键/语言）

- `crop_waste` 82：
  - 例：`faba_bean` → 蚕豆废枝叶 / Faba Bean Waste Leaves；
- `spice_waste` 20：
  - 例：basil → 罗勒废枝叶；
- `bush_waste` 10：
  - 例：blackberry → 黑莓灌木废枝；
- `grain_bundle` 16：
  - 例：wheat → 小麦捆 / Wheat Bundle；
- `spice_seed` / `spice` / `ground_spice`：
  - 例：vanilla → 香荚兰 / 香荚兰种子 / 香荚兰粉；
- `ground_nut` / `nut_shell` / 直接坚果：
  - 例：pistachio → 开心果 / 开心果粉 / 开心果壳；
- 坚果/香料树：
  - `nut_sapling` / `nut_leaves`；
  - `spice_sapling` / `spice_leaves`；
  - `spice_crop`。

### 3.2 木材/家具/木工名称（510 键/语言）

- 10 个木材家具族 × 34 木材；
- 5 个木工部件族（bark/bast/debarked log/half/quarter）× 34；
- TFC 20 木材 + AFC 14 木材；
- 例：
  - `fruit_bowl/oak` → 橡木果盘 / Oak Fruit Bowl；
  - `bark/chestnut` → 栗木树皮 / Chestnut Bark；
  - `drying_rack/teak` → 柚木干燥架 / Teak Drying Rack。

## 4. 校验

```text
lang en_us 1061 / zh_cn 1061
missing 0 / extra 0
中文 item/block 名称含 ASCII ID: 0
json 6425 / bad 0
final_static_audit problems 0
gradle build BUILD SUCCESSFUL
```

## 5. 明确未做

- **未改任何贴图**：`crop_waste` 仍共用 `tfc:item/straw`，属于视觉问题；
- 未改物品/方块注册 ID；
- 未实机打开创造页逐项检查；
- 部分翻译依赖 TFC/A 既有译名，仍需用户目视确认术语偏好。
