# 358 种子处理 tooltip P0-AI 技术分析

> 日期：2026-10-29
> 目标：让玩家在原版种子栈上直接看到处理阶段，而不是盲猜组件状态。
> 约束：不推送；不伪造；未实机。

## 1. 实现

`SeedTreatmentTooltip`：

- 监听 `ItemTooltipEvent`；
- 读 `SEED_TREATMENT`；
- 有值才追加：
  - `tooltip.tfcagricultureplus.seed_treatment.soaked`
  - `...germinated`
  - `...dressed`

语言：

```text
Soaked / Germinated / Dressed
已浸种 / 已催芽 / 已拌种
```

## 2. 为什么

- 处理状态存在组件里，玩家看不到；
- 不新增物品；
- 不改变任何数值；
- 便于实机验证组件是否保留。

## 3. 测试

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 343 crop P0 checks
```

资源：

```text
processResources BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 只显示阶段，不显示剩余时间/效果；
- 其他 mod 的 tooltip 顺序未验证；
- 语言 key 只覆盖三阶段。
