# 537 OPEN-002/013 配方书警告与 pestle 消歧工作报告

> 日期：2026-10-29
> 状态：**静态修复/静态排障完成；未实机**
> 范围：OPEN-002、OPEN-013。

## 1. 完成

- 为 `MortarRecipe`、`FoodMixingBowlRecipe` 补 `isSpecial() = true`；
- 新增 `check_recipe_is_special.py`，4/4 自定义配方通过；
- 新增 `check_pestle_disambiguation.py`，7/7 pestle ingredients 唯一；
- 确认 TFC `KnappingRecipe.matches` 按 ingredient 消歧。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
json 6442 / bad 0
final_static_audit problems 0
custom recipe isSpecial 4/4
pestle unique 7/7
```

## 3. 未做

- 未实机确认日志；
- 未实机研磨；
- 未处理视觉。
