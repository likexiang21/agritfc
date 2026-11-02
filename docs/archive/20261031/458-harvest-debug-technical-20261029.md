# 458 玩家破坏收获链实机验证 P0-CG 技术分析

> 日期：2026-10-29
> 目标：用真实玩家 `ServerPlayerGameMode.destroyBlock` 触发 BlockEvent.BreakEvent，验证 UnifiedCropHarvestHandler 路径。
> 约束：不推送；不伪造；调试命令为临时测试入口。

## 1. 临时调试命令

```java
/tfcplusdebug_harvest <pos>
```

执行：

```java
player.gameMode.destroyBlock(pos);
```

这是真实玩家破坏路径，不是 `/setblock air destroy`。

## 2. 测试

干净存档：

- farmland + `spice_crop/basil[age=7]`；
- farmland + `crop/strawberry[age=7]`；
- 玩家生存模式；
- 100t 后调用调试命令；
- 100t 后检查。

## 3. 实机结果

```text
HARVEST_BASIL_PLACED
HARVEST_STRAWBERRY_PLACED
RUNTIME_HARVEST_BREAK
HARVEST_BASIL_GONE
HARVEST_STRAWBERRY_GONE
HARVEST_ITEM_NEAR
```

- 两个成熟作物都被玩家破坏；
- 方块变为空气；
- 附近出现 item 实体；
- 无崩溃/无相关 ERROR。

## 4. 结论

玩家破坏事件路径与 B 收获处理已实际执行，作物被移除并产生掉落物。

## 5. 未确认

- 掉落物具体 ID/数量；
- 种子/废枝叶 top-up 是否全部正确；
- 未成熟作物保护；
- 双作物顶部清理；
- creative 分支。

## 6. 风险

- 调试命令必须在发布前移除或加开关；
- 本轮只测 basil/strawberry，不是全部物种。
