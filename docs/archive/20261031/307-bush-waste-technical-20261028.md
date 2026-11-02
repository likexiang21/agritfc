# 307 TFC 灌木废枝 P0-J 技术分析

> 日期：2026-10-28
> 目标：为剩余 10 种 TFC 浆果灌木加入真实废枝副产。
> 约束：不推送；不伪造；贴图暂时指向 TFC。

## 1. 范围

- 草莓已由 A 迁移，排除；
- 10 种 TFC 灌木：
  blackberry · blueberry · bunchberry · cloudberry · cranberry ·
  elderberry · gooseberry · raspberry · snowberry · wintergreen；
- 每种新增 `bush_waste/<species>`；
- 新方块 ID 使用精确的 `tfc:plant/<species>_bush`；
- 破坏时追加 1 个废枝；
- **不取消**原方块破坏，TFC 原浆果/生命周期掉落保留。

本轮不是完整的“替换 TFC 灌木采收/再生流程”，只是先补真实副产。完整替换仍需单独批次。

## 2. 代码

- `BushSpecies`：10 条，TFC block ID 与 waste path；
- `AgricultureShrubs`：独立 DeferredRegister.Items；
- `BushWasteHandler`：监听 `BlockEvent.BreakEvent`，精确 ID 匹配，追加废枝；
- 主入口注册 items + game-bus listener；
- 创造页加入 10 个废枝。

## 3. 堆肥

10 条全部加入 `tfc:compost_greens/high`，`replace:false`。

## 4. 测试

纯 Java：

```text
PASS: 245 crop P0 checks
```

新增：

- 10 个 TFC bush；
- blackberry 映射；
- strawberry 不再作为 TFC bush。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

资源：

```text
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, tags valid
```

## 5. 风险/未验证

- 未实机验证；
- 只追加废枝，没有替换 TFC 灌木的采收/再生；
- 没有 B 灌木方块/育苗；
- 废枝贴图临时 TFC；
- 10 条 bush_waste 不包含在原 102 crop_waste 统计中，单独统计。
