# 609 厨房家具配方/掉落静态验证脚本技术分析

> 日期：2026-10-30
> 状态：**静态验证 PASS；未实机**
> 约束：不实机、不推送。

## 1. 目的

为 OPEN-003/OPEN-004 的 204 个厨房家具建立可重复验证。

## 2. 检查项

`validate_kitchen_furniture.py`：

- 6 类 ×34 木材 = 204；
- 配方存在且类型为 `minecraft:crafting_shaped`；
- 配方结果 ID = `tfcagricultureplus:<family>/<wood>`；
- loot table 存在且掉落自身；
- 中英 block 名称键存在：
  `block.tfcagricultureplus.<family>.<wood>`。

## 3. 结果

```text
families 6
woods 34
expected 204
problems 0
PASS: kitchen furniture recipes/loot
```

## 4. 边界

- 只验证数据/引用；
- 不验证配方是否冲突、实机掉落、菜单；
- 未实机。
