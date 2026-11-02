# 319 育苗盘处理加速 P0-P 技术分析

> 日期：2026-10-29
> 目标：让种子处理阶段影响育苗盘生长时间，把 P0-L/P0-M 连成一条可用链。
> 约束：不推送；不伪造；未实机。

## 1. 设计

`SeedTreatments.nurseryTicks(stage)`：

| 阶段 | 育苗 tick |
|---|---:|
| 未处理 | 1200 |
| soaked | 1000 |
| germinated | 800 |
| dressed | 600 |

- 下限 600；
- `NurseryTrayBlockEntity.insert` 读取种子 `SEED_TREATMENT` 并保存 `requiredTicks`；
- `ready()` 使用该值；
- 存档保存/读取 `required_ticks`。

## 2. 为什么不是直接改生长

- 育苗盘是 B 自己的 BE，可以直接控制计时；
- 不触碰 TFC/A 作物生长；
- 处理阶段与育苗链形成闭环；
- 大田生长效果仍由 P0-N 的 Bonemealable 尝试负责。

## 3. 测试

纯 Java：

```text
PASS: 278 crop P0 checks
```

新增 4 个育苗时间检查。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 4. 风险

- 未实机验证；
- 处理状态组件是否在种子入槽时保留需要实机确认；
- 数值未平衡；
- 不支持无性苗；
- 没有育苗 GUI。
