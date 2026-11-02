# 542 P2-1 扩展：无性繁殖物品链技术分析

> 日期：2026-10-29
> 状态：**静态实现；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 目标

291 要求非种子繁殖：

- 种薯 / 块茎；
- 球茎 / 种球；
- 根茎；
- 匍匐茎；
- 冠芽 / 分株。

此前 P2-1 只做了分类和播种门，没有物品链。本轮补 21 个无性繁殖物品。

## 2. 新增物品

统一 ID：

```text
tfcagricultureplus:propagation_stock/<species>
```

覆盖：

| 方法 | 物种 |
|---|---|
| CORM | shallot / garlic / taro / water_chestnut / water_caltrop / arrowhead / gorgon_nut |
| TUBER | sunchoke / yacon / potato / yam |
| RHIZOME | ginger / turmeric / lotus |
| CROWN | artichoke / cardoon / rhubarb / asparagus |
| DIVISION | chive / cassava |
| RUNNER | strawberry |

共 **21** 个。

## 3. 来源与放置

### 来源

每个物品由对应作物产品合成：

```text
1 份作物产品 → 2 个繁殖材料
```

使用 `minecraft:crafting_shapeless`。

### 放置

`PropagationStockItem`：

- 只在耕地上使用；
- 目标上方必须为空；
- 查找对应 A/TFC/B 作物方块；
- 找 `age` IntegerProperty 并设 0；
- 调用 `canSurvive` 校验；
- 成功后放置、播放 `CROP_PLANTED`、消耗 1。

## 4. 资源复用

不新增任何贴图：

- item model 使用对应作物产品的现有纹理：
  - A：`tfcfarmingplus:item/food/<species>`；
  - TFC：`tfc:item/food/<species>`；
- 因此没有“批量生成占位贴图”。

## 5. 校验

```text
propagation stock recipes 21
product item refs bad 0
crop block refs bad 0
json 6484 / bad 0
item_models 943
final_static_audit problems 0
validate_crop_p0a PASS
```

## 6. 明确未完成

- `hops` 没有对应 food 产品纹理，未纳入；
- 水生作物（taro/water_chestnut/water_caltrop/lotus 等）目前只尝试耕地，水田放置未实现；
- 没有母株性状 DataComponent；
- 没有育苗/缓苗阶段；
- 未实机；
- 未处理视觉。
