# 484 育苗→移栽→生长→收获全链 P0-CT 技术分析

> 日期：2026-10-29
> 目标：一次实机跑通育苗盘→seedling→移栽→成熟→收获。
> 约束：不推送；不伪造；调试命令为临时测试入口。

## 1. 测试

干净存档：

- 育苗盘 stage2 + strawberry seed；
- use 育苗盘 → seedling；
- 移栽到 farmland；
- randomTickSpeed=1000；
- 300t 后检查成熟；
- 成熟后真实玩家破坏；
- 检查方块/背包。

## 2. 实机结果

```text
RUNTIME_CHAIN_SETUP
RUNTIME_CHAIN_USE_TRAY
RUNTIME_CHAIN_PLANT
CHAIN_MATURE
RUNTIME_CHAIN_HARVEST
CHAIN_GONE
```

- 移栽后的 strawberry 长到 age7；
- 破坏后方块变为空气；
- 无 ERROR。

## 3. 未记录

- 本次 `tfcplusdebug_drops` 只记录玩家背包，没有记录 ItemEntity；
- 因此本轮**没有**掉落物 ID 日志；
- 之前 P0-CH/P0-CI 已确认 strawberry 掉落 ID。

## 4. 结论

育苗→移栽→生长→成熟→收获全链在实机跑通；掉落物证据来自之前批次。

## 5. 清理

已再次移除调试命令并构建成功。
