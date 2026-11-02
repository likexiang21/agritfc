# 422 树木生长失败定位 P0-BO 技术分析

> 日期：2026-10-29
> 目标：定位 P0-BN 中树苗没有生成树冠的原因。
> 约束：不推送；不伪造；未完成树生长验证。

## 1. 代码审查发现的 bug

`NutTreeSaplingBlock.growTree` / `SpiceTreeSaplingBlock` 末尾：

```java
level.removeBlock(pos, false);
```

而 `growTree` 已经在 `pos` 放了第一根树干原木；末尾 remove 会删掉底部原木，留下悬空树干。

修复：删除这两行。

## 2. 测试结果仍无证据

绝对坐标测试：

```text
OK_ABS_NUT_SAPLING_PLACED
OK_ABS_SPICE_SAPLING_PLACED
RUNTIME_TREE_ABS_CHECK
```

没有：

```text
OK_ABS_NUT_TRUNK
OK_ABS_SPICE_TRUNK
OK_ABS_NUT_CANOPY
OK_ABS_SPICE_CANOPY
```

## 3. 测试设计问题

- 使用 `forceload` 的区块可能没有正常 random tick；
- 检查函数里 `forceload remove` 又在检查前，导致后续 sapling 检查在已卸载区块执行；
- 没有先确认树苗在 15 秒后是否仍存在；
- 玩家相对坐标测试可能受玩家位移影响。

## 4. 下一步

1. 玩家传送到固定平台；
2. 用玩家区块 random tick；
3. 检查树苗 stage 0/1/2 是否推进；
4. 再检查树干/树冠绝对坐标。

## 5. 结论

- 修复了一个确凿的树生成 bug；
- 但**树生成仍未实机验证**；
- 不能宣称树木功能完成。
