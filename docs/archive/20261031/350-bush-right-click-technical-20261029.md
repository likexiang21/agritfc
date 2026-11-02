# 350 TFC 灌木右键采收 P0-AE 技术分析

> 日期：2026-10-29
> 目标：把 10 种 TFC 灌木的右键采摘也纳入 B 控制，而不只是破坏采收。
> 约束：不推送；不伪造；未实机。

## 1. 实现

`BushRightClickHarvestHandler`：

- `PlayerInteractEvent.RightClickBlock`；
- 仅服务端；
- 仅空手；
- 目标方块必须是 10 种 TFC bush 之一；
- 必须是 `SeasonalPlantBlock`；
- 必须 `Lifecycle.FRUITING`；
- 取消事件；
- 掉 1–2 个 `getProductItem`；
- 用 `stateAfterPicking(state)` 保留灌木进入已采状态。

## 2. 与破坏采收

- 破坏：`BushHarvestHandler`；
- 右键：本 handler；
- 两者都走 TFC 的 `stateAfterPicking`，不重复 B 废枝（废枝只在破坏时追加）。

## 3. 测试

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 320 crop P0 checks
```

## 4. 风险

- 未实机；
- 与 TFC 原 `useItemOn` 的事件顺序未验证；
- 只处理空手；
- 可能影响其他 mod 对右键的监听；
- 没有完整 10 种实机回归。
