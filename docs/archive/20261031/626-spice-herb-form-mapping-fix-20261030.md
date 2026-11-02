# 626 代码筛查：香料草本形态映射缺失

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`SpiceSpecies` 有 20 种香料，其中 `herb` 形态包括：

```text
basil / cilantro / cumin / oregano / thyme / sage / dill / fennel / mustard
```

`AgricultureSpices.newSpiceCrop` 的 switch：

```java
case "tree" -> ...
case "vine" -> ...
case "shrub" -> ...
case "root" -> ...
case "corm" -> ...
default -> new CropBlock(...)
```

**没有 `"herb"` 分支**，所以所有草本香料都落入 `default`，使用 vanilla `CropBlock`；
`SpiceCropBlocks.Herb` 成为未使用类。

## 2. 修复

增加：

```java
case "herb" -> new SpiceCropBlocks.Herb(properties);
```

使 9 种草本香料使用 `SpiceCropBlocks.Herb` 的 2..14 / 高 10 形状，而不是 vanilla 默认形状。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,587 bytes
SHA-256 DCCECB1C97E2909D9B44856B3C39D30309EB1E094E26410D6E6EF4D1F01CEC2D
```

## 4. 未完成

- 未实机；
- 未检查其它 form 的形状/行为差异。
