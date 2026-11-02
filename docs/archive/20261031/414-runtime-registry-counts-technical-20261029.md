# 414 实机注册计数验证 P0-BK 技术分析

> 日期：2026-10-29
> 目标：用真实客户端日志确认 B 的香料/蘑菇/废枝叶注册表实际大小，区分“注册失败”与“setblock 放置失败”。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 新增日志

`TFCAgriculturePlus` 构造器在注册后输出：

```text
[TFC Agriculture Plus] registries: spiceCrops=15, spiceTrees=5, cropWaste=82, wildMushrooms=15
```

## 2. 实机结果

真实客户端日志：

```text
[03:54:49] [TFC Agriculture Plus/]: [TFC Agriculture Plus] registries:
  spiceCrops=15, spiceTrees=5, cropWaste=82, wildMushrooms=15
[03:55:11] [IntegratedServer]: Starting integrated minecraft server version 1.21.1
```

结论：

- 15 crop-form 香料已注册；
- 5 tree-form 香料树已注册；
- 82 A/TFC crop_waste 已注册；
- 15 野生蘑菇已注册。

## 3. 与烟测的关系

之前的 setblock 烟测中 `spice_crop/basil`、`spice_crop/cardamom`、`spice_sapling/cinnamon` 未通过。

现在注册日志证明它们**不是注册失败**；更可能是：

- load function 时区块未完全加载；
- 作物/树苗 `canSurvive` 在 setblock 后立即被移除；
- 支撑方块（farmland/dirt）在同一 load function 中未稳定。

需要后续用真实放置/支撑重测，而不是用注册数当玩法成功。

## 4. 证据

```text
mod_rebuild/docs/audit/runtime-registry-counts-20261029.log
```

## 5. 风险

- 只证明注册表大小；
- 没有证明每个 blockstate/model 正确；
- 没有证明放置/生长/收获；
- 测试后已恢复旧 jar/options。
