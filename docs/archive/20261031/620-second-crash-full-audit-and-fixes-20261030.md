# 620 二次崩溃彻查：日志中的本模组问题与修复

> 日期：2026-10-30
> 状态：**代码/数据已修复；未实机**
> 日志：`crash-reports/crash-2026-10-30_22.13.48-client.txt`、`logs/latest.log`

## 1. 崩溃主因

```text
Description: Rendering screen
java.lang.NoClassDefFoundError: net/dries007/tfc/config/TemperatureDisplayStyle
at com.eerussianguy.firmalife.compat.jei.OvenCategory.draw(OvenCategory.java:55)
```

本模组有 15 条 `firmalife:oven` 配方，把 B 的 `raw_*` 面团放进 Firmalife 的
OvenCategory；JEI 绘制这些配方时执行到缺失类，导致客户端崩溃。

### 修复

1. 15 条 `firmalife:oven` 全部迁移为 `tfc:heating`（400°C，result_item 保持）；
2. 删除 `recipe/oven/`；
3. `AgricultureJeiPlugin.onRuntimeAvailable` 检测到该类缺失时隐藏 `firmalife:oven` 分类，避免任何烤箱配方绘制路径崩溃。

## 2. 日志中的其它本模组问题

### 2.1 方块标签拼写错误

```text
tfcagricultureplus:log_pile
Couldn't load tag minecraft:mineable/axe
```

实际方块 ID 是 `lumber_pile`，标签写错。

修复：`minecraft/tags/block/mineable/axe.json` 改为 `tfcagricultureplus:lumber_pile`。

### 2.2 配方 pattern 解析错误

```text
Failed to parse recipe 'tfcagricultureplus:crafting/materials/plant_fiber_rope'
Invalid component key: pattern<optional_ingredient>
```

原配方：

```json
"pattern": ["F ", " F"]
```

KubeJS/解析器对含空格的 shaped pattern 报错。

修复：改为 `crafting_shapeless`：

```json
ingredients: [2 × #tfcfarmingplus:materials/plant_fibers]
result: tfc:rope ×2
```

### 2.3 Patchouli 图标无效

```text
Invalid icon item stack: 未知的物品“tfcagricultureplus:crop/strawberry”
```

`crop/strawberry` 是方块，没有对应物品，不能作为 Patchouli icon。

修复：分类与 overview 的 icon 改为 `tfcagricultureplus:seeds/strawberry`。

并修正验证脚本：icon 必须是 **item model**，不能只凭 blockstate 通过。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
B tag missing refs 0
firmalife:oven refs 0
heating recipes 16
bad Patchouli icons 0
json 6484 / bad 0
final_static_audit problems 0
```

## 4. 未完成

- 未实机；
- 需要用户启动确认 OvenCategory 不再被绘制、无新的本模组错误。
