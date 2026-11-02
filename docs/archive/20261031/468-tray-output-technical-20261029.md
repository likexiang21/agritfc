# 468 育苗盘输出实机验证 P0-CL 技术分析

> 日期：2026-10-29
> 目标：确认育苗盘 stage2 右键把 seedling 放进玩家背包。
> 约束：不推送；不伪造；调试命令为临时测试入口。

## 1. 测试

干净存档：

- `nursery_tray[stage=2]`，data merge seed=seeds/strawberry；
- 玩家生存；
- 100t 后 `tfcplusdebug_use`；
- 5t 后读玩家背包。

## 2. 实机结果

```text
TRAY_STAGE2_PLACED
RUNTIME_TRAY_USE
RUNTIME_TRAY_LOG

inventory tfcagricultureplus:seedling x1

TRAY_RESET0
```

- 育苗盘 stage2 右键后产出 **1 个 seedling**；
- 直接进入玩家背包；
- 育苗盘重置为 stage0；
- 无 ERROR。

## 3. 结论

育苗盘“stage2 → seedling 进背包 → 重置”链路实机生效。

## 4. 未确认

- 不同种子/种子的 NBT 是否随 seedling 保留；
- 移栽到耕地后的生长；
- 处理时间/温度；
- 旧存档。
