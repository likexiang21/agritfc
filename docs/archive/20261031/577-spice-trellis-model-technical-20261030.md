# 577 香料架占位模型替换技术分析

> 日期：2026-10-30
> 状态：**静态视觉修复；未实机**
> 约束：视觉可用，但不重绘贴图。

## 1. 问题

`spice_trellis` 模型：

```json
{"parent":"minecraft:block/cube_all","textures":{"all":"tfc:block/wood/planks/oak"}}
```

整块木板。

## 2. 修复

改为垂直棚架：

- 2 根外立柱：x 1–2 / 14–15，z 7–9；
- 4 根内竖条：x 4–5、7–8、10–11、13–14，z 7.5–8.5；
- 2 根横梁：y 4–5、9–10，x 2–14；
- 全部使用 `tfc:block/wood/planks/oak`；
- 没有新增贴图。

## 3. 边界

- `spice_trellis` 方块本身仍是完整碰撞箱（`Block`），模型变薄不影响碰撞；
- 这是视觉模型，不是新的攀爬逻辑。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / models 3690 / blockstates 539
final_static_audit problems 0
```

## 5. 未完成

- 未实机；
- 未做作物攀爬/附着逻辑（如需要，另批）；
- 未按木材变体区分（只有 oak 模型）。
