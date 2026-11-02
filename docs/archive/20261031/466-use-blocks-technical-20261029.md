# 466 菌包/育苗盘球员交互验证 P0-CK 技术分析

> 日期：2026-10-29
> 目标：用真实玩家 `gameMode.useItemOn` 调用 B 方块 use 逻辑。
> 约束：不推送；不伪造；调试命令为临时测试入口。

## 1. 调试命令

```text
/tfcplusdebug_use <pos>
```

执行：

```java
player.gameMode.useItemOn(player, level, mainHand, MAIN_HAND, hitResult);
```

## 2. 测试

干净存档：

- `mushroom_bag[stage=2]` + `{species:"oyster",uses:0}`；
- `nursery_tray[stage=2]` + `{seed:{id:"tfcagricultureplus:seeds/strawberry",count:1},...}`；
- 玩家生存；
- 100t 后 use 两个方块；
- 5t 后读 ItemEntity。

## 3. 实机结果

```text
USE_BAG_PLACED
USE_TRAY_PLACED
RUNTIME_USE_USE
RUNTIME_USE_LOG

dropped tfcagricultureplus:wild_mushroom/oyster x4

USE_TRAY_RESET0
```

- 菌包右键产出 **4 个 oyster 蘑菇**；
- 育苗盘从 stage2 重置为 stage0；
- 没有 B 相关 ERROR。

## 4. 结论

菌包采集与育苗盘交互的玩家 use 路径实机生效。

## 5. 未确认

- 育苗盘是否把 seedling 放进玩家背包（本轮只读 ItemEntity，未读背包）；
- 菌包 uses 递增；
- 温度错误提示；
- 自然生成；
- 所有菌种/种子。
