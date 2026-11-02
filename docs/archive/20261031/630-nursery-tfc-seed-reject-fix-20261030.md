# 630 代码筛查：育苗盘接受 TFC 种子但无法移栽

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`NurseryTrayBlockEntity.canAccept` 原来只检查：

```java
SeedTreatments.isSeedItemId(itemId)
```

TFC 种子（如 `tfc:seeds/wheat`）也满足该检查，因此可以被放进育苗盘。

但 `SeedlingItem.useOn` 只接受：

```java
if (!(seed instanceof BlockItem blockItem)) {
    return InteractionResult.FAIL;
}
```

TFC 种子不是 B 的作物 BlockItem，取出幼苗后移栽会失败，形成无法完成的操作链。

## 2. 修复

`canAccept` 明确拒绝 TFC 命名空间：

```java
if (id.startsWith("tfc:")) {
    return false;
}
```

理由：

- TFC 作物保持原版直播路径；
- 育苗盘只服务 A/B 种子；
- 避免玩家放入 TFC 种子后拿到无法移栽的幼苗。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,883 bytes
SHA-256 AA959B2FD4B64C4C985B57F69569BD3F257776E5FD345D5C2CCF3D17848B7168
```

## 4. 未完成

- 未实机；
- 未验证 A 种子全部为 BlockItem（当前 A 的 `MySeedItem` 继承 `ItemNameBlockItem`，可移栽）。
