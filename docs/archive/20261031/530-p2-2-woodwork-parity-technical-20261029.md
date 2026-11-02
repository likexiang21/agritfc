# 530 P2-2 木工内容与 TFC Woodworking 逐项对照技术分析

> 日期：2026-10-29
> 状态：**静态对照完成 + 一处真实错误修复；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 对照对象

- B：`data/tfcagricultureplus/recipe/crafting/woodwork/{tfc,afc}/...`
- 原版：`tfcwoodwork-1.21.1-1.2.4.jar.disabled`
  - `data/tfcwoodwork/recipe/crafting/wood/<wood>.json`
  - `data/tfcwoodwork/recipe/crafting/stripped_wood/<wood>.json`

## 2. 配方对照结果

对照脚本：`compare_woodwork_recipes.py`

```text
original recipes 40
B copied 40
problems 0
```

对比内容：

- `type`；
- `pattern`；
- `result`（id/count）；
- `key`（忽略预期命名空间替换：`tfcwoodwork:*` → `tfcagricultureplus:*`）。

结论：

- B 对 **TFC 20 木材 × 2 类木工配方（wood / stripped_wood）= 40 条**的复制是**结构一致的**；
- 仅做预期内的命名空间替换；
- AFC 14 木材的 28 条是 B 扩展，原版没有，不能算“原配方”。

## 3. 真实错误：`lumber_pile` 的错误自掉落表

P0-3 曾给 `tfcagricultureplus:lumber_pile` 补了一个标准“掉落自身”的 loot table。

但对照 docs/286 和代码：

- `lumber_pile` **没有方块物品**；
- 不能合成；
- 打掉时由 `LumberPileBlock.onRemove` → `LumberPileBlockEntity.dropContents()` 掉落**内部木材**；
- 不存在 `tfcagricultureplus:lumber_pile` 物品。

因此该 loot table 会尝试掉落一个不存在物品，是错误修复。

处置：

- 删除 `loot_table/blocks/lumber_pile.json`；
- P0-3 文档中的“174 个 loot table”修正为 **173**；
- 明确 `lumber_pile` 只能由 `TimberBlocks.registerPlacement()` 的潜行右键放置，不是 crafting 方块。

## 4. 仍未证明的“木工移植”

- 只对照了 **配方结构**；
- 未逐项对照 debarked block 的模型/碰撞/交互；
- 未验证 TFCW 原有的 in-world 去皮/劈木动作是否全部由 B 的 `TimberBlocks`/`InWorld` 处理；
- 未实机；
- B 是**独立迁移**（不前置 TFCW），不是直接依赖原模组；因此不能声称“原封不动”。

## 5. 校验

```text
gradle clean build BUILD SUCCESSFUL
json 6441 / bad 0
final_static_audit problems 0
woodwork recipe parity: 40/40, problems 0
```

## 6. 未完成

- 实机；
- 模型/交互/音效逐项对照；
- 木工配方与 TFC 基础木材配方的冲突扫描。
