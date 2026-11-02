# 317 TFC 灌木采收替换 P0-O 技术分析

> 日期：2026-10-29
> 目标：破坏结果的 TFC 浆果灌木时，不再直接移除方块，而是采收浆果并让灌木进入已采状态，保留再生能力。
> 约束：不推送；不伪造；未实机。

## 1. 范围

只处理 10 种 TFC 灌木：

```text
blackberry · blueberry · bunchberry · cloudberry · cranberry ·
elderberry · gooseberry · raspberry · snowberry · wintergreen
```

精确 ID：

```text
tfc:plant/<species>_bush
```

草莓排除（A 普通作物）。

## 2. 行为

`BushHarvestHandler` 监听 `BlockEvent.BreakEvent`：

- 方块必须是 `SeasonalPlantBlock`；
- 必须是 `Lifecycle.FRUITING`；
- 取消原破坏；
- 调用 `getProductItem(random)` 取浆果；
- 掉落 1–2 个浆果；
- 用 `stateAfterPicking(state)` 把灌木留在原地，进入已采状态；
- 非结果状态保持 TFC 原行为。

`BushWasteHandler` 仍会追加废枝。

## 3. API

- TFC `SeasonalPlantBlock.LIFECYCLE`；
- `Lifecycle.FRUITING`；
- `getProductItem(RandomSource)`；
- `stateAfterPicking(BlockState)`。

## 4. 测试

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有纯 Java：

```text
PASS: 274 crop P0 checks
```

## 5. 风险

- 未实机验证事件顺序/取消；
- 只处理破坏，不处理 TFC 原右键采摘；
- 不保证所有 10 个 TFC 灌木都使用 `SeasonalPlantBlock` 的同一具体子类；
- 与 `BushWasteHandler` 的监听顺序未实测；
- 没有完整 B 灌木方块/育苗/扦插。
