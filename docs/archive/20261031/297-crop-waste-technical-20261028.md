# 297 作物废枝叶 P0-C 技术分析

> 日期：2026-10-28
> 目标：实现真实产出的逐作物绿色废枝叶，不再使用通用 `green_waste`。
> 约束：不推送、不伪造、贴图暂用 TFC。

## 1. 范围

本轮只实现 **A/TFC 82 条实际有废枝叶的作物**：

- 来源：`291 §4.1.2` 实际表；
- 不含谷物、油料、纤维、坚果、蘑菇（它们走 straw/cake/shives/shell/spent substrate）；
- B 香料 20 条尚未注册为 B 作物，暂不生成 waste 物品；后续香料批次再加，最终目标 102。

每个作物注册：

```text
tfcagricultureplus:crop_waste/<crop>
```

## 2. 行为设计

`CropWasteHandler` 监听 `BlockEvent.BreakEvent`：

- 只处理精确的 `tfcfarmingplus:crop/<crop>` / `tfc:crop/<crop>`；
- 只处理在 `CropWasteCrops.ALL` 中的 82 条；
- 只有达到该方块真实最大 `age` 才产出；
- 双格作物只在 `part=bottom` 产一次，`top` 跳过；
- **不取消**原方块破坏，因此原 main/byproduct 掉落仍保留，waste 是额外副产；
- 不处理野生作物/未成熟/非作物方块。

最大 age 不硬编码，而是运行时从该方块 `getStateDefinition().getPossibleStates()` 计算并缓存，避免把 A 的 5/7 龄或 TFC 的 7 龄写死。

## 3. 堆肥

`data/tfc/tags/item/compost_greens/{high,medium,low}.json` 均：

- `replace:false`；
- 只追加 `tfcagricultureplus:crop_waste/*`；
- 按 291 表的实际高/中/低档分配；
- 82 条全部有且只在一个对应档中（校验脚本检查）。

## 4. 资源

- 82 个 `models/item/crop_waste/<crop>.json`；
- 临时 `layer0: tfc:item/straw`；
- `en_us`/`zh_cn` 各 82 个 key；
- 创造页加入全部 82 个 waste。

## 5. 原型/校验

纯 Java：

```text
PASS: 129 crop P0 checks
```

新增覆盖：

- 82 条 waste 数量；
- `spinach` 有、`wheat` 无；
- A/TFC 反查；
- 野生/非作物拒绝。

资源校验：

```text
PASS: 99 models, 2 lang files, 17 recipes, 82 crop_waste, tags valid
```

## 6. 风险

- 事件顺序/双格表现/最大 age 运行时值**未实机验证**；
- 原掉落保留，因此不是“替换主产物”，只是新增真实副产；
- B 香料 waste 尚未注册；
- 没有对每一种作物实机逐项收获。

## 7. 下一步

- 实机验证 82 条 waste；
- B 香料 20 条 waste；
- 完成 102 条最终目标；
- TFC 29 的完整 blockstate/model/种植行为覆盖；
- 蘑菇 worldgen；
- 坚果叶状态。
