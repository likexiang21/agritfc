# 304 坚果叶状态 P0-F 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：TFC 树叶 `nut_state`、4 种树→坚果映射、8 个坚果物品、随机掉落。

## 1. 完成内容

### 1.1 Mixin

- `TFCLeavesNutStateMixin`；
- 给 `TFCLeavesBlock` 加 `nut_state=0..3`；
- 按 TFC 季节更新：
  - 春 1 / 夏 2 / 秋 3 / 冬 0；
- 秋熟后随机刻 3% 掉落坚果。

### 1.2 树→坚果

| 树叶 | 坚果 |
|---|---|
| `tfc:wood/leaves/oak` | acorn |
| `tfc:wood/leaves/chestnut` | chestnut |
| `tfc:wood/leaves/pine` | pine_nut |
| `tfc:wood/leaves/hickory` | hickory_nut |

### 1.3 物品

注册 8 个坚果：

```text
acorn · chestnut · pine_nut · hickory_nut ·
pistachio · cashew · macadamia · beechnut
```

其中前 4 个本轮已接到叶状态掉落；后 4 个等待新树/后续树接口。

### 1.4 树叶 blockstate

- 从 TFC jar 读取全部 20 个树叶 blockstate；
- 每个 `variants` 展开 `nut_state=0..3`；
- chestnut 的 `multipart` 也按 4 个 nut_state 展开；
- 不替换 TFC 模型，只扩展状态覆盖。

### 1.5 资源

- 8 个 nut item model；
- en/zh 各 8 个 key；
- 创造页加入。

## 2. 验证

### 纯 Java

```text
PASS: 140 crop P0 checks
```

新增：

- 4 个 TFC nut 树叶映射；
- oak → acorn；
- beech 不是 TFC 树叶映射。

### 编译

```text
gradle compileJava --rerun-tasks
BUILD SUCCESSFUL
```

### 资源

```text
PASS: 99 item models, 2 lang files, 17 recipes, 82 crop_waste,
      15 wild mushrooms, 4-stage bag, 20 nut leaf states, tags valid
```

`processResources`：

```text
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机验证 mixin**；
- `nut_state` 当前没有坚果 overlay 模型，外观不随状态变化；
- 只覆盖 TFCLeavesBlock；A/AFC 单独树叶类/资源未覆盖；
- beech 没有 TFC 树叶，未映射；
- 后 4 个坚果物品暂未接树；
- 3% 掉落概率未平衡；
- 贴图仍为 TFC 临时代用。

## 4. 下一批

1. 实机验证；
2. A/AFC 树叶；
3. 坚果 overlay 模型；
4. beech 映射；
5. TFC 29 剩余覆盖；
6. 最终全量验收。

## 5. P0-G：AFC 树叶扩展（追加）

- `NutBearingTree` 支持多树叶 ID；
- 5 个坚果组：
  - oak：TFC oak + AFC black_oak/live_oak；
  - chestnut：TFC chestnut + AFC hardy_chestnut/chinquapin；
  - pine：TFC pine + AFC red_pine/stone_pine/huangshan_pine；
  - hickory：TFC hickory + AFC scrub_hickory；
  - beech：AFC beech/black_beech/rauli_beech；
- AFC 59 个树叶 blockstate 已展开 `nut_state=0..3`；
- TFC 20 + AFC 59 = 79 个树叶状态；
- 纯 Java 检查 141 通过；
- 资源校验 79 nut leaf states 通过。

⚠️ 边界：AFC 树叶是否全部使用 `TFCLeavesBlock` 尚未实机确认；若不是，mixin 属性不会应用，必须实机优先检查。

