# 464 未成熟作物掉落修复 P0-CJ 技术分析

> 日期：2026-10-29
> 目标：修复未成熟 B 作物被破坏仍掉落产品/种子的问题。
> 约束：不推送；不伪造。

## 1. 发现

P0-CI 测试中 immature basil age0 被破坏后仍出现产品掉落。

根因：

- `UnifiedCropHarvestHandler` 对未成熟作物返回，不接管；
- 但 B 的 `spice_crop/*` / `crop/strawberry` 战利品表**无条件**掉落产品+种子；
- 未成熟方块走原版 block loot，所以仍掉产品。

## 2. 修复

给 16 个战利品表（15 香料 + 草莓）每个 pool 加：

```json
"conditions": [
  {
    "condition": "minecraft:block_state_property",
    "block": "tfcagricultureplus:spice_crop/basil",
    "properties": { "age": "7" }
  }
]
```

未成熟状态条件不成立 → 不掉落。

## 3. 构建/校验

```text
gradle build BUILD SUCCESSFUL
validate_crop_p0a.py PASS
```

## 4. 复测

干净存档：

- immature basil age0；
- immature strawberry age0；
- mature basil age7。

真实玩家破坏后：

```text
IMMATURE_BASIL_GONE
IMMATURE_STRAWBERRY_GONE
MATURE_BASIL_GONE

dropped spice_waste/basil
dropped spice/basil
dropped spice_seed/basil
```

只有 mature basil 掉落；未成熟两个没有掉落。

## 5. 结论

未成熟作物不再掉产品/种子。

## 6. 未验证

- 其他 14 个香料作物逐一；
- 概率/数量；
- creative；
- 旧存档。
