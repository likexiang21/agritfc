# 332 直播替换 P0-V 技术分析

> 日期：2026-10-29
> 目标：用 B 育苗/移栽流程替换 A/TFC/B 种子的原地直播，让“育苗 → 移栽”成为唯一种植入口。
> 约束：不推送；不伪造；未实机。

## 1. 行为

`DirectSeedPlantingGate`：

- 监听 `PlayerInteractEvent.RightClickBlock`；
- 只对 `SeedTreatments.isSeedItemId` 的种子生效：
  - A：`tfcfarmingplus:seeds/*`
  - TFC：`tfc:seeds/*`
  - B 香料：`tfcagricultureplus:spice_seed/*`
- 目标方块为 `FarmBlock` 或 ID 以 `farmland` 结尾；
- 取消直接种植；
- 提示玩家使用育苗盘；
- 不影响右键种子处理（副手湿草）和幼苗移栽。

## 2. 为什么可以这样做

- A `MySeedItem extends ItemNameBlockItem`；
- TFC `SeedItem extends ItemNameBlockItem`；
- B 香料种子是 `BlockItem`；
- 三者都能用 `SeedlingItem` 的 BlockItem 路径移栽。
- 因此取消直播后，种子 → 育苗盘 → 幼苗 →  farmland 移栽仍是完整可走通的代码路径。

## 3. 处理状态迁移

- 育苗盘取出幼苗时，把种子上的 `SEED_TREATMENT` 复制到幼苗；
- 幼苗移栽后按 soaked/germinated/dressed 做 1/2/3 次受限 `BonemealableBlock` 推进；
- 原先 P0-N 的“直播后推进”不再触发，因为直播已被取消。

## 4. 测试

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有纯 Java：

```text
PASS: 283 crop P0 checks
```

## 5. 风险

- 未实机验证；
- 没有直播后处理，玩家必须先做育苗盘；
- TFC/A 作物是否实现 `BonemealableBlock` 仍未确认；
- 可能影响依赖直接种植的自动化/脚本；
- 需要实机确认取消事件不会误伤其他种子交互。
