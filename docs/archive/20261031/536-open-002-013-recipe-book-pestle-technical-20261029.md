# 536 OPEN-002/013 配方书警告与 pestle 消歧技术分析

> 日期：2026-10-29
> 状态：**静态修复/静态排障完成；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. OPEN-002：Unknown recipe category

### 原因

1.21.1 `ClientRecipeBook.categorizeAndGroupRecipes` 的行为：

```java
if (recipe.isSpecial()) continue;
...
if (unknown type) LOGGER.warn("Unknown recipe category: {}/{}", ...)
```

B 的 4 个自定义 Recipe 类：

- `InWorldRecipe`：原本已有 `isSpecial() = true`；
- `CuttingBoardRecipe`：已有；
- `MortarRecipe`：**缺**；
- `FoodMixingBowlRecipe`：**缺**。

后两者会被客户端配方书当作普通配方，于是尝试分类并产生 warning。

### 修复

为缺的两个类增加：

```java
@Override
public boolean isSpecial() {
    return true;
}
```

静态检查：

```text
custom recipe classes 4
missing isSpecial=true 0
```

### 说明

18:28 的日志是在旧 jar 下生成的；当前源码/构建已经让 4 个自定义配方全部 `isSpecial=true`。
本轮新增 `check_recipe_is_special.py` 防止回归。

未实机确认日志是否完全消失；这是 **fixed-static / runtime-unverified**。

## 2. OPEN-013：7 个 pestle 共用 pattern

静态检查：

```text
pestle recipes 7
unique knapping_type+pattern+ingredient 7
```

每个 pestle 的 `ingredient` 都不同：

- basalt / diorite / gabbro / granite / quartzite / slate → `tfc:rock/loose/<rock>`；
- obsidian → `tfc:groundcover/obsidian_shard`。

TFC `KnappingRecipe.matches` 同时检查：

```java
input.getKnappingType() == this.knappingType.get()
&& input.getPattern().matches(this.getPattern())
&& this.matchesItem(input.getOriginalStack())
```

因此同 pattern 会被不同的 `ingredient` 消歧，**不存在实际冲突**。
OPEN-013 从“高风险未验证”降为 **resolved-static**。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6442 / bad 0
final_static_audit problems 0
custom recipe isSpecial 4/4
pestle unique 7/7
```

## 4. 未完成

- 未实机确认 recipe book 日志；
- 未实机研磨 pestle；
- 未处理视觉。
