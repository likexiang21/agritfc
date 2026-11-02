# 654 代码筛查：育苗盘空盘拒绝所有种子

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`NurseryTrayBlockEntity.canAccept` 原来：

```java
if (seed.isEmpty() || stack.isEmpty()) {
    return false;
}
```

`seed` 是托盘当前库存种子；托盘新建时 `seed = ItemStack.EMPTY`，该条件直接返回 false。

结果：

- **空托盘永远不能放入任何种子**；
- 已经有种子的托盘反而能“接受”第二个种子（但 insert 会覆盖）。

这是条件写反：应当要求托盘为空，而不是要求托盘非空。

## 2. 修复

```java
if (!seed.isEmpty() || stack.isEmpty()) {
    return false;
}
```

- 空盘 + 非空手持种子 → 接受；
- 已有种子的盘 → 拒绝；
- 空手持 → 拒绝。

此前的 TFC 种子拒绝逻辑仍保留在后面。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,925 bytes
SHA-256 464B0A20A16472B75DB608D6A6519A5C79C0E6F6B4604C79B15212D29686BEFC
```

## 4. 未完成

- 未实机；
- 未验证育苗盘完整生长/取出流程。
