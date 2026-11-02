# 301 蘑菇菌包 P0-E 技术分析

> 日期：2026-10-28
> 目标：为可栽培 11 种蘑菇实现四阶段菌包；自然专用 4 种拒绝接种。
> 约束：不推送；不伪造；贴图暂时指向 TFC。

## 1. 范围

本轮实现：

- 单一 `tfcagricultureplus:mushroom_bag` 方块；
- 4 个 blockstate stage：
  - 0 空包
  - 1 走菌
  - 2 出菇
  - 3 枯竭
- 单一 BlockItem；
- `MushroomBagBlockEntity` 保存：
  - species id
  - progress；
- 接种：
  - 手持 B 的 `wild_mushroom/<species>` BlockItem 右键空包；
  - 只接受 11 种可栽培候选；
  - 自然专用 4 种 `naturalOnly()` 直接失败。
- 生长：
  - stage 1 每 tick progress +1；
  - 1200 tick 后 stage 2；
- 收获：
  - stage 2 右键空手/任意物品 → 收 2–4 个对应 wild mushroom 物品，stage 3；
- 枯竭：
  - stage 3 保留，不自动恢复。

## 2. 为什么用 BE

菌包只有 stage 是 blockstate，但需要记录：

- 种了哪一种蘑菇；
- 走菌进度。

所以使用 `MushroomBagBlockEntity`，而不是 11 个物种专用菌包方块。这样：

- 方块 ID 固定为 `mushroom_bag`；
- 11 种共用一套 blockstate/model；
- 自然专用拒绝逻辑在一处；
- 未来可扩到不同培养时长/产量。

## 3. API 评估

- `MushroomBagBlock extends Block implements EntityBlock`；
- 必须实现 `codec()`；
- `newBlockEntity` + `getTicker`；
- `ItemInteractionResult` 处理接种/收获；
- `BlockEntity.saveAdditional/loadAdditional` 保存 species/progress；
- `BlockEntityType` 通过 `RegistrationHelpers.register` 注册，validBlocks 只包含 `MUSHROOM_BAG`；
- `MushroomSpecies.fromBlockId` 从 `wild_mushroom/<id>` 反查，自然专用拒绝。

## 4. 资源

- blockstate stage 0–3；
- 单一 block model（临时 TFC 木板贴图）；
- item model；
- loot table；
- 语言 key；
- 配方：`tfc:straw` + `minecraft:dirt` → mushroom bag。

## 5. 原型/校验

纯 Java：

```text
PASS: 137 crop P0 checks
```

新增：

- `fromBlockId` 正查 oyster/porcini；
- 未知蘑菇拒绝。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

资源：

```text
PASS: 99 item models, 2 lang files, 17 recipes, 82 crop_waste, 15 wild mushrooms, 4-stage bag, tags valid
```

## 6. 风险/未验证

- 未实机验证接种/生长/收获/掉落；
- 空手收获与物品交互的事件顺序未验证；
- 1200 tick 为原型值，未平衡；
- 菌包不检查温度/湿度；
- 自然专用 4 种只在接种入口被拒绝，配方/其它入口未来也必须检查；
- 临时贴图与真实模型未完成。

## 7. 下一步

1. 实机验证菌包；
2. 温湿度/培养时长调参；
3. 自然专用所有入口的硬拒绝；
4. TFC 29 完整覆盖；
5. 坚果叶状态。
