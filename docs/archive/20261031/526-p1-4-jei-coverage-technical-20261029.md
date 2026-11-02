# 526 P1-4 JEI 覆盖与可读性技术分析

> 日期：2026-10-29
> 状态：**部分静态修复；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

用户报告：

- JEI 可读性极差；
- 没有表现新添加的加工内容。

原状态：

- B 只有 3 个 JEI category：
  - mortar
  - cutting_board
  - in_world
- 烹饪锅、育苗盘、菌包、养蚕架、晾架、厨房家具没有任何 JEI 信息；
- B 的晾架使用 Firmalife `firmalife:drying` 配方，但没有作为 Firmalife drying category 的 catalyst 出现。

## 2. 本次修改

### 2.1 晾架 catalyst

把 B 的全部 34 个 `drying_rack/<wood>` 加入 Firmalife 的 `FLJEIPlugin.DRYING` 催化剂：

```java
for (Block block : AgricultureBlocks.DRYING_RACKS.values()) {
    registration.addRecipeCatalyst(new ItemStack(block), FLJEIPlugin.DRYING);
}
```

这样在 JEI 的 Firmalife drying 页能直接看到“哪些晾架可以执行该配方”。

### 2.2 设备信息页

新增 `addIngredientInfo` 信息页，共 10 项 × 中英：

- `cooking_pan`
- `nursery_tray`
- `mushroom_bag`
- `silkworm_rack`
- `drying_rack`
- `cutting_board`
- `log_cutting_board`
- `knife_block`
- `mortar`
- `kitchen_storage`

信息页内容是短句，说明：
- 放置条件；
- 输入/输出；
- 工具/耐久；
- 温度/次数/储存限制。

## 3. 语言键

新增：

```text
jei.tfcagricultureplus.info.<key>
```

中英各 10 个，语言文件 1086 → **1096**。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
final_static_audit problems 0
json 6442 / bad 0
lang 1096 / 1096
missing 0 / extra 0
```

## 5. 未完成

- 没有新增 B 自己的 recipe category；
- 烹饪锅仍是动态组合，无固定 JEI 配方页；
- 没有实机确认 JEI 信息页/催化剂显示；
- 没有 recipe pages 或图片；
- 未处理视觉。
