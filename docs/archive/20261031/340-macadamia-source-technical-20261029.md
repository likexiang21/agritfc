# 340 澳洲坚果来源 P0-Z 技术分析

> 日期：2026-10-29
> 目标：让 B 的 `macadamia` 坚果从现有 A 澳洲坚果树叶获得真实来源。
> 约束：不推送；不伪造；additive。

## 1. 背景

- A 已有 `tfcfarmingplus:plant/macadamia_leaves`；
- 该叶方块不是 `TFCLeavesBlock`，现有 `TFCLeavesNutStateMixin` 覆盖不到；
- 因此单独加 `MacadamiaDropHandler`，不改 A 方块。

## 2. 行为

`BlockEvent.BreakEvent`：

- 精确匹配 `tfcfarmingplus:plant/macadamia_leaves`；
- 5% 概率掉：
  - 1 个 `tfcagricultureplus:macadamia`；
  - 1 个 `tfcagricultureplus:nut_shell/macadamia`；
- 不取消原 A 树叶掉落。

## 3. 测试

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有：

```text
PASS: 283 crop P0 checks
```

## 4. 风险

- 未实机验证；
- 5% 与 A 树叶季节/结果状态无关，属临时来源；
- pistachio/cashew 仍无树；
- 没有真正新增澳洲坚果树。
