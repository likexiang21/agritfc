# 306 B 香料作物 P0-H 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：20 种 B 香料的作物/种子/产物骨架；形态细分未完成。

## 1. 完成内容

### 1.1 20 种香料

```text
basil · bay_laurel · cardamom · cilantro · cumin · oregano · pimento · vanilla ·
black_pepper · cinnamon · clove · nutmeg · saffron · star_anise · rosemary ·
thyme · sage · dill · fennel · mustard
```

### 1.2 注册内容

每个香料：

- `spice_crop/<id>` CropBlock；
- `spice_seed/<id>` BlockItem；
- `spice/<id>` 产物；
- blockstate age 0..7；
- loot table：1 产物 + 1 种子；
- item model + 语言。

### 1.3 创造页/渲染层

- 创造页加入 20 seeds + 20 products；
- 客户端渲染层加入 20 spice crops。

## 2. 验证

### 纯 Java

```text
PASS: 222 crop P0 checks
```

覆盖 20 个 species、form、crop/seed/product 路径。

### 编译

```text
gradle compileJava
BUILD SUCCESSFUL
```

### 资源

```text
PASS: 99 item models, 2 lang files, 17 recipes, 82 crop_waste,
      15 wild mushrooms, 4-stage bag, 79 nut leaf states, 20 spice crops, tags valid
```

`processResources`：

```text
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机验证**；
- 20 种都使用普通 CropBlock，**树/藤/球茎形态未实现**；
- 没有香料加工链/配方；
- 没有 20 条 spice crop_waste，当前仍是 82/102；
- 贴图全部临时 TFC 资源；
- 不能宣称 B 香料内容已完成。

## 4. 下一步

1. 按 form 细分；
2. 香料加工链；
3. spice crop_waste 20 条；
4. 实机验证；
5. TFC 29 剩余覆盖。

## 5. P0-I：20 条香料废枝叶（追加）

- 新增 20 个 `spice_waste/<spice>` 物品；
- 草本类 9 条进 `compost_greens/high`；
- 其他 11 条进 `compost_greens/medium`；
- `CropWasteHandler` 已接 `tfcagricultureplus:spice_crop/<id>`；
- 只在该作物最大 age 掉落，不取消原破坏；
- crop_waste 总量达到 **102**。

验证：

```text
PASS: 242 crop P0 checks
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      15 wild mushrooms, 4-stage bag, 79 nut leaf states, 20 spice crops, tags valid
```

边界：未实机验证；香料形态仍未细分。

