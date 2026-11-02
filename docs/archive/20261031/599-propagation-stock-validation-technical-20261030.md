# 599 繁殖材料链静态验证脚本技术分析

> 日期：2026-10-30
> 状态：**静态验证 PASS；未实机**
> 约束：不实机、不推送。

## 1. 目的

为 P2-1 的 21 个繁殖材料建立可重复验证，避免只靠人工计数。

## 2. 检查项

脚本 `validate_propagation_stock.py`：

- `PropagationStock.java` 解析 21 条记录；
- 物种不重复；
- 6 种方法均出现：
  `CORM / CROWN / DIVISION / RHIZOME / RUNNER / TUBER`；
- 每个物种：
  - item model 存在；
  - recipe 存在；
  - recipe 输入 = 对应产品；
  - recipe 输出 = `tfcagricultureplus:propagation_stock/<species>`；
  - 中英 lang 键存在；
  - 产品模型在对应 A/TFC/B jar 中存在；
  - 作物 blockstate 在对应 jar 中存在。

## 3. 结果

```text
rows 21
methods CORM, CROWN, DIVISION, RHIZOME, RUNNER, TUBER
problems 0
PASS: propagation stock chain
```

## 4. 边界

- 只验证资源/数据存在与引用；
- 不验证实际放置、水温、母株性状；
- 未实机。
