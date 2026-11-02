# 330 野草香料种子来源 P0-U 技术分析

> 日期：2026-10-29
> 目标：在野生香料植物/worldgen 完成前，给 20 种 B 香料一个非创造的初始种子来源。
> 约束：不推送；不伪造；additive。

## 1. 设计

`SpiceSeedDropHandler`：

- 监听 `BlockEvent.BreakEvent`；
- 只处理 `minecraft:short_grass` / `minecraft:tall_grass`；
- 5% 概率掉落随机一种 `spice_seed/<species>`；
- 不取消原草方块破坏；
- 不影响 TFC 草/作物。

## 2. 为什么先这样做

- 20 种香料种子目前只有创造页来源；
- 完整野生香料 worldgen 需要独立方块/模型/群系，工作量大；
- 先用低概率草种子来源让种植链可启动；
- 后续仍应补正式野生香料植物，替换这个临时来源。

## 3. 测试

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有纯 Java：

```text
PASS: 283 crop P0 checks
```

## 4. 风险

- 未实机验证；
- 5% 随机总池，单一种子概率低；
- 只是临时来源，不是正式生态；
- 没有保底；
- 可能被玩家视为刷种子途径，需后续平衡/限制。
