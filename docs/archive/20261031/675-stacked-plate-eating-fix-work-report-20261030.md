# 675 堆叠盘子食用修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `DishEating.finishItemUse` 对堆叠盘子改为拆分单盘；
- 原 stack 只 `shrink(1)`，不再 `setCount(1)` 清空整堆；
- 拆分盘单独写入 `servings - 1` 或清空 dish；
- 拆分盘放入玩家背包，满则掉落；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,532 bytes
SHA-256 73E06DAF486E81958B26F44FB6E581DD9317AB667B3E9C375C3D267429094F38
```

## 3. 未做

- 未实机；
- 未验证不同菜/背包满/创造模式。
