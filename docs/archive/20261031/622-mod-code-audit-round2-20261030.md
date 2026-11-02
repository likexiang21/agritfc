# 622 模组代码问题筛查报告（第二轮）

> 日期：2026-10-30
> 状态：**静态筛查完成；未实机、未启动客户端**
> 范围：注册/初始化、JEI 兼容、数据/配方、资源引用、日志错误。

## 1. 本轮筛查方法

- 逐项读取最新 `crash-reports/crash-2026-10-30_22.13.48-client.txt` 与 `logs/latest.log`；
- 扫描全部 Java 源码的：
  - `registerDefaultState(...setValue(...))`；
  - 静态初始化/注册 lambda 中的 `DeferredHolder.get()`；
  - `displayClientMessage`；
- 运行静态验证：
  - `static_audit.py`
  - `final_static_audit.py`
  - `check_tag_refs.py`
  - `check_recipe_refs.py`
  - `check_patchouli_icons.py`
  - `validate_kitchen_furniture.py`
  - `validate_woodwork_visuals.py`
  - `validate_patchouli_entries.py`

## 2. 已修复的问题

### 2.1 注册期崩态属性（OPEN-014）

根因：

- `TimberPieceBlock` 在 `super()` 期间调用 `createBlockStateDefinition`；
- 子类字段 `directional` 尚未初始化，`facing` 没有进入状态定义；
- 构造函数随后 `setValue(FACING)` 抛出 `IllegalArgumentException`。

修复：

- 拆为 `TimberPieceBlock`（无 facing）与 `DirectionalTimberPieceBlock`（有 facing）；
- `TimberBlocks` 按 part 选择类；
- `weight()`、`canSurvive` 同时支持两种类。

### 2.2 本模组烤箱配方触发 JEI 崩溃（OPEN-015）

日志：

```text
NoClassDefFoundError: net/dries007/tfc/config/TemperatureDisplayStyle
at Firmalife OvenCategory.draw
```

本模组 15 条 `firmalife:oven` 配方进入该 JEI 分类，触发绘制路径。

修复：

- 15 条全部迁移为 `tfc:heating`；
- 删除 `recipe/oven/`；
- JEI 插件检测该类缺失时隐藏 `firmalife:oven` 分类。

### 2.3 `log_pile` 标签拼写

- 标签中写的是 `tfcagricultureplus:log_pile`；
- 实际方块 ID 为 `tfcagricultureplus:lumber_pile`；
- 已改正。

### 2.4 `plant_fiber_rope` 配方解析

- 原 `crafting_shaped` pattern 含空格，KubeJS 报
  `pattern<optional_ingredient> is not allowed to be empty`；
- 改为 `crafting_shapeless`，2 个植物纤维 → 2 个 `tfc:rope`。

### 2.5 Patchouli 图标

- `tfcagricultureplus:crop/strawberry` 是方块，不是物品；
- 分类/overview icon 改为 `tfcagricultureplus:seeds/strawberry`；
- 验证脚本改为 icon 必须是 item model。

### 2.6 缺失方块语言

- 补 `crop/strawberry`、`nut_leaves/*`、`nut_sapling/*`、`spice_crop/*` 的中英 block 名称；
- 语言总数 1092/1092，missing/extra 0。

## 3. 静态校验结果

```text
json 6484 / bad 0
lang 1092 / 1092 / missing 0 / extra 0
models 3690 / blockstates 539 / item_models 943
final_static_audit problems 0
B tag missing refs 0
recipe reference problems 0
bad Patchouli icons 0
kitchen furniture 204 PASS
TFC woodwork visual parity 60 PASS
firmalife:oven refs 0
heating recipes 16
```

## 4. 注册/初始化扫描结果

- 其余方块构造函数的 `registerDefaultState` 属性均在静态字段或父类状态中定义；
- 未发现第二个“构造期使用未初始化实例字段决定状态定义”的模式；
- 静态初始化中的 `DeferredHolder.get()` 仅用于运行时 BlockEntity 构造或已绑定注册表之后；
- `displayClientMessage` 全项目 0；
- 未发现客户端专用类被 common 初始化直接引用。

## 5. 当前 jar

```text
2,922,025 bytes
SHA-256 3809EF4E55819812E982DDBB39231CC1CFEEEC31F746C2F79812F61F795403B1
```

`mods` 中仅保留当前 jar，没有旧版前缀 jar。

## 6. 边界

- 本轮没有实机、没有启动客户端、没有通知玩家测试；
- 静态验证不能证明所有运行时路径；
- 需要继续静态审查时，优先关注 BlockEntity/Menu/事件处理的边界，而不是再改数据表现。
