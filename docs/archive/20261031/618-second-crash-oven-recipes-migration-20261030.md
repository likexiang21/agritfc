# 618 二次崩溃修复：本模组烤箱配方迁移出 Firmalife JEI 分类

> 日期：2026-10-30
> 状态：**代码/数据已修复；未实机**
> 日志：`crash-reports/crash-2026-10-30_22.13.48-client.txt`、`logs/latest.log`

## 1. 崩溃

```text
Description: Rendering screen
java.lang.NoClassDefFoundError: net/dries007/tfc/config/TemperatureDisplayStyle
at com.eerussianguy.firmalife.compat.jei.OvenCategory.draw(OvenCategory.java:55)
```

## 2. 与本模组的关系

本模组有 15 条：

```text
data/tfcagricultureplus/recipe/oven/*.json
type = firmalife:oven
```

这些配方把 B 的 `raw_*` 面团送进 Firmalife 的 **OvenCategory**。
在 JEI 打开这些配方时，OvenCategory 绘制路径执行到 TFC 类
`net.dries007.tfc.config.TemperatureDisplayStyle`，当前依赖组合下该类不可用，导致客户端崩溃。

因此这不是“玩家操作问题”，也不是“别的模组单独负责”：
**本模组自己的 15 条 oven 配方触发了这条 JEI 绘制路径**。

## 3. 修复

把 15 条 `firmalife:oven` 配方迁移为 TFC 原生加热配方：

```text
data/tfcagricultureplus/recipe/heating/*.json
type = tfc:heating
temperature = 400.0
result_item = 原烤箱产物
```

- 不再有 `firmalife:oven` 配方；
- B 的 raw 面团仍可通过 TFC 加热链加工；
- 不再把 B 配方塞进 Firmalife OvenCategory；
- 已删除 `recipe/oven/` 目录。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
firmalife:oven refs in B data = 0
heating recipes = 16
```

## 5. JEI 兼容保护

AgricultureJeiPlugin.onRuntimeAvailable 会检测 TFC 该类是否存在；不存在时隐藏 irmalife:oven 分类，避免任何烤箱配方绘制时再次崩溃。

## 6. 边界

- 这只修复**本模组配方触发的路径**；
- 未实机；
- 如果仍出现同一路径崩溃，继续按本模组数据/兼容层排查，不把责任推给用户或其它模组。
