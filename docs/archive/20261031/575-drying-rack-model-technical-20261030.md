# 575 晾架占位模型替换技术分析

> 日期：2026-10-30
> 状态：**静态视觉修复；未实机**
> 约束：视觉可用，但不重绘贴图。

## 1. 问题

34 个 `drying_rack/<wood>` 模型全部是：

```json
{"parent":"minecraft:block/cube_all","textures":{"all":"tfc:block/wood/planks/oak"}}
```

每个都是一整块木板，与“晾架”无关。

## 2. 修复

新增共享模型 `block/drying_rack.json`：

- 四条腿：`1..2` / `14..15`，高 12；
- 顶部四边框：y 11–12；
- 6 根横条：y 11–11.5，x 3/5/7/9/11/13；
- 高度 12，与 `DryingRackBlock` 的 `box(1,0,1,15,12,15)` 一致。

34 个 per-wood 模型改为：

```json
{
  "parent": "tfcagricultureplus:block/drying_rack",
  "textures": { "wood": "tfc:block/wood/planks/<wood>" }
}
```

AFC 木材使用 `afc:block/wood/planks/<wood>`。

没有新增贴图。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / models 3690 / blockstates 539
final_static_audit problems 0
```

## 4. 未完成

- 未实机查看渲染；
- 未按 facing 做视觉旋转差异；
- 未处理 `spice_trellis` 占位模型。
