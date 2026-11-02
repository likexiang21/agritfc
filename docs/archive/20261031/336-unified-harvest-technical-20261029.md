# 336 统一收获替换 P0-X 技术分析

> 日期：2026-10-29
> 目标：让 B 逻辑真正控制 A/TFC/B 非谷物作物的收获结果，而不只是往原掉落上追加。
> 约束：不推送；不伪造；未实机。

## 1. 设计

`UnifiedCropHarvestHandler`：

- 只处理成熟、非 `top`、非谷物的 A/TFC/B 作物；
- 精确解析三类方块：
  - `tfcfarmingplus:crop/<crop>`
  - `tfc:crop/<crop>`
  - `tfcagricultureplus:spice_crop/<spice>`
- 取消原方块破坏；
- 用原方块自己的 loot table 生成**原产物**（带玩家/工具）；
- 若原掉落里没有种子，补 1 个 B 解析出的种子；
- 追加 1 个 crop_waste（存在时）；
- 移除方块。

`CropBItemResolver` 统一解析种子/废枝叶：

- A：`tfcfarmingplus:seeds/<crop>`；
- TFC：`tfc:seeds/<id>`；
- B 香料：`spice_seed/<id>`；
- 废枝叶：A/TFC `crop_waste/<crop>`，B `spice_waste/<spice>`。

## 2. 事件顺序

```text
GrainHarvestHandler
  -> UnifiedCropHarvestHandler
    -> CropWasteHandler (skip canceled)
      -> TfcSeedReturnHandler (skip canceled)
        -> ACropSeedReturnHandler (skip canceled)
```

- 谷物走 GrainHarvestHandler，统一 handler 跳过；
- 非谷物被统一 handler 取消后，旧的追加型 handler 全部跳过，避免重复；
- B 灌木/树叶不受影响。

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

- 未实机；
- 原 loot table 可能依赖玩家/工具/时运，现有调用已传玩家与主手，但未验证全部 A/TFC 作物；
- 双格 top/bottom 只处理一次；
- 去掉原方块可能影响依赖原方块状态的掉落；
- 取消后其他 mod 的 BlockEvent 监听可能被影响；
- 没有完整收获验收。
