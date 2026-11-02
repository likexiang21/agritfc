# 389 菌包复用 P0-AY 技术分析

> 日期：2026-10-29
> 目标：收获后的 `stage=3` 菌包不再永久报废，可重新接种继续使用。
> 约束：不推送；不伪造；未实机。

## 1. 修改

`MushroomBagBlock.useItemOn`：

```java
if ((stage == 0 || stage == 3) && stack.getItem() instanceof BlockItem blockItem)
```

- stage 0：新菌包接种；
- stage 3：已收获菌包重新接种；
- 调用 `bag.inoculate(species)` 重置 progress；
- 设回 stage 1；
- 消耗 1 个野生蘑菇方块物品。

## 2. 效果

```text
空菌包 -> 接种 -> 生长 -> 收获 -> stage 3
stage 3 -> 再接种 -> 生长 -> 收获
```

不再需要破坏重放。

## 3. 测试

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 没有耐久/次数限制；
- 自然专用 4 种仍在接种时拒绝；
- stage 3 重新接种的视觉状态未验证；
- 可能与其他右键逻辑冲突。
