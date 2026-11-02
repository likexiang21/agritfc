# 311 种子处理 P0-L 技术分析

> 日期：2026-10-28
> 目标：在不新增处理种子物品的前提下，给现有 A/TFC 种子增加“浸种 → 催芽 → 拌种”组件状态。
> 约束：不推送；不伪造。

## 1. 范围

- 新增 DataComponent：

```text
tfcagricultureplus:seed_treatment
```

- 阶段：

```text
soaked -> germinated -> dressed
```

- 操作：

```text
主手种子 + 副手 wet_grass + 右键
```

每次推进一阶段并消耗 1 个湿草（创造模式不消耗）。
- 处理状态存在**原种子物品**上，不新增 116 个处理种子物品。
- 不改变原种子 ID/栈。

## 2. 为什么用 DataComponent

- 116 个种子 × 新物品会爆炸；
- TFC 种子不可替换；
- 后续生长速度/育苗/移栽都能读同一个组件；
- 兼容现有种子栈与配方。

## 3. 代码

| 文件 | 作用 |
|---|---|
| `SeedTreatments` | 纯 Java 阶段推进 + 种子 ID 判断 |
| `AgricultureDataComponents.SEED_TREATMENT` | String 组件 |
| `SeedTreatmentHandler` | 右键种子 + 副手 wet_grass 推进阶段 |
| `TFCAgriculturePlus` | 注册 game-bus listener |

## 4. 测试

纯 Java：

```text
PASS: 271 crop P0 checks
```

新增：

- soaked / germinated / dressed 阶段；
- TFC/A 种子 ID 识别；
- 食物不误判为种子。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 5. 风险/未验证

- 未实机验证右键事件、组件同步、消耗；
- 处理阶段**尚未影响生长速度/育苗/移栽**；
- 没有“干燥→筛选→浸种”等完整 UI/工序；
- 没有处理后的 tooltip/模型差异；
- 没有防止重复使用/阶段上限之外的交互测试。
