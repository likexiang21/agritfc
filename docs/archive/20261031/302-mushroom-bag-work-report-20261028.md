# 302 蘑菇菌包 P0-E 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：11 种可栽培蘑菇的四阶段菌包；自然专用 4 种拒绝接种。

## 1. 完成内容

### 1.1 方块

- `tfcagricultureplus:mushroom_bag`；
- stage 0 空包 / 1 走菌 / 2 出菇 / 3 枯竭；
- BlockItem 可放置。

### 1.2 状态

`MushroomBagBlockEntity`：

- 保存 species id；
- 保存 progress；
- stage 1 每 tick +1，1200 tick 后 stage 2；
- stage 2 收获后 stage 3；
- stage 3 不自动恢复。

### 1.3 接种规则

- 手持 `wild_mushroom/<species>` BlockItem 右键空包；
- 只接受 11 种可栽培候选；
- 自然专用 4 种：
  - porcini
  - morel
  - chanterelle
  - black_truffle
  - `naturalOnly()` 直接失败，不消耗物品。

### 1.4 收获

- stage 2 右键空手；
- 掉落 2–4 个对应 wild mushroom 物品；
- 变 stage 3。

### 1.5 资源

- blockstate 4 variants；
- block model + item model；
- loot table；
- 语言 key；
- 配方：`tfc:straw` + `minecraft:dirt` → mushroom bag；
- 临时 TFC 木板贴图。

## 2. 验证

### 纯 Java 原型

```text
PASS: 137 crop P0 checks
```

新增：

- `fromBlockId("...oyster")` → OYSTER；
- `fromBlockId("...porcini")` → PORCINI；
- 未知 ID → null。

### 编译

```text
gradle compileJava
BUILD SUCCESSFUL
```

### 资源

```text
PASS: 99 item models, 2 lang files, 17 recipes, 82 crop_waste, 15 wild mushrooms, 4-stage bag, tags valid
```

## 3. 边界

- **未实机验证**接种、走菌、收获、掉落；
- 1200 tick 是原型值，未平衡；
- 未检查温度/湿度；
- 自然专用目前只在接种入口拒绝；未来其它入口也必须检查；
- 菌包使用临时 TFC 模板贴图；
- TFC 29 完整覆盖、坚果叶状态仍未完成。

## 4. 下一批

1. 实机验证菌包；
2. 温湿度/时长/产量调参；
3. 自然专用全入口硬拒绝；
4. TFC 29 完整种植/收获覆盖；
5. 坚果 `nut_state`；
6. 全作物验收。
