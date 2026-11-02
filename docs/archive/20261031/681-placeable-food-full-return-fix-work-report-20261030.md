# 681 满份摆盘食物返还整块修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `PlaceableFoodBlockEntity` 增加 `isFull()` 与公开 `maxServings()`；
- `PlaceableFoodBlock.getDrops` 对满份食物返回方块物品；
- `PlaceableFoodBlock.onRemove` 只在非满份时 dropContents；
- 满份不再只掉切片，部分份仍只掉切片，无整块 + 切片双掉；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,927,122 bytes
SHA-256 AF14CE68AB82CDE93290AEC322A1F9ABF08233439632EE5C72307B552DBAE61D
```

## 3. 未做

- 未实机；
- 未验证活塞/命令替换满份食物。
