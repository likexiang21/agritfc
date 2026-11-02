# 303 坚果叶状态 P0-F 技术分析

> 日期：2026-10-28
> 目标：在已有 TFC 乔木叶上增加 `nut_state`，按季节挂果并随机掉落坚果。
> 约束：不推送；不伪造；贴图暂时指向 TFC。

## 1. 范围

本轮实现：

- TFC 树叶 mixin：`TFCLeavesNutStateMixin`；
- 新 blockstate 属性 `nut_state=0..3`：
  - 0 无
  - 1 花
  - 2 青
  - 3 熟
- 季节映射：
  - 春 → 1
  - 夏 → 2
  - 秋 → 3
  - 冬 → 0
- 成熟后随机刻概率掉落坚果；
- 坚果物品 8 个：
  - acorn · chestnut · pine_nut · hickory_nut · pistachio · cashew · macadamia · beechnut
- 已有 TFC 树叶映射 4 种：
  - oak → acorn
  - chestnut → chestnut
  - pine → pine_nut
  - hickory → hickory_nut

## 2. Mixin 设计

`@Mixin(TFCLeavesBlock.class)`：

- `createBlockStateDefinition` TAIL 注入 `nut_state`；
- `randomTick` HEAD 注入：
  - 按 `Calendars.get(level).getHemispheralCalendarMonthOfYear(false).getSeason()` 更新状态；
  - 秋且随机 < 0.03 时掉落对应坚果物品；
- 不改 TFC 原方块类 ID；
- 所有 TFC 树叶 blockstate JSON 已经展开 `nut_state=0..3`，包括 chestnut 的 multipart。

## 3. 物品/资源

- 8 个 nut item；
- 临时 `tfc:item/straw` 贴图；
- `en_us`/`zh_cn` 各 8 个 key；
- 创造页加入；
- 不新增树方块，只复用已有树叶。

## 4. 测试

纯 Java：

```text
PASS: 140 crop P0 checks
```

新增：

- 4 个 TFC nut leaf 映射；
- oak → acorn；
- `tfc:wood/leaves/beech` 不作为 TFC leaf 映射（AFC 另行处理）。

编译：

```text
gradle compileJava --rerun-tasks
BUILD SUCCESSFUL
```

资源：

```text
PASS: 99 item models, 2 lang files, 17 recipes, 82 crop_waste,
      15 wild mushrooms, 4-stage bag, 20 nut leaf states, tags valid
```

## 5. 风险/未验证

- **未实机验证 mixin 注入、季节状态、掉落**；
- 只处理 TFCLeavesBlock；A/AFC 单独的树叶类/资源尚未覆盖；
- 没有坚果 overlay 模型，当前 `nut_state` 只改变状态/掉落，不改变叶模型外观；
- beech 没有 TFC leaf，暂未映射；
- 掉落概率 3% 未平衡；
- 所有坚果贴图暂用 TFC 临时图。

## 6. 下一步

1. 实机验证 mixin；
2. A/AFC 树叶扩展；
3. 坚果 overlay 模型；
4. beech 映射；
5. 掉落概率/季节窗口调参。

## 7. P0-G：AFC 树叶扩展（追加）

已完成：

- `NutBearingTree` 改为**一个坚果组可挂多个树叶 ID**；
- 覆盖：
  - oak：TFC oak + AFC black_oak/live_oak；
  - chestnut：TFC chestnut + AFC hardy_chestnut/chinquapin；
  - pine：TFC pine + AFC red_pine/stone_pine/huangshan_pine；
  - hickory：TFC hickory + AFC scrub_hickory；
  - beech：AFC beech/black_beech/rauli_beech；
- AFC 59 个树叶 blockstate 全部展开 `nut_state=0..3`；
- TFC 20 + AFC 59 = **79 个树叶状态覆盖**；
- 纯 Java 检查 **141**；
- 资源校验通过。

仍需注意：AFC 树叶方块类是否全部继承 `TFCLeavesBlock` 未实机确认；如果不是，mixin 属性不会应用到 AFC 方块。该风险必须在实机测试时优先检查。

