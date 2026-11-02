# 559 P1-2 家具共享模型差异化技术分析

> 日期：2026-10-29
> 状态：**静态视觉修复；未实机**
> 约束：视觉可用，但不做大面积贴图重绘。

## 1. 问题

6 种厨房家具的共享模型原来都是同一个立方体：

```json
{"elements":[{"from":[0,0,0],"to":[16,16,16],"faces":{"all":"#all"}}]}
```

`fruit_bowl` 只是高度不同（0→8），整体仍是方块，和家具名称无关。

## 2. 修复

6 个共享模型改为不同轮廓，全部使用子模型传入的 `#all` 木材纹理：

| 家具 | 轮廓 |
|---|---|
| counter_cabinet | 柜体 + 台面 |
| half_cabinet | 低柜 + 顶板 |
| sink_cabinet | 柜体 + 四周水槽边 + 浅槽底 |
| spice_rack | 背板 + 两侧立柱 + 两层搁板 |
| food_display | 底座 + 四边框 + 中层搁板 + 顶框 |
| fruit_bowl | 浅碗底 + 四边碗沿 |

没有新增任何 PNG；每个变体继续继承 `tfc:block/wood/planks/<wood>` / `afc` 纹理。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6483 / models 3689 / blockstates 539
final_static_audit problems 0
static_resource_audit problems 0
```

## 4. 未完成

- 未实机查看渲染/旋转；
- 未做门板、把手、水龙头等更细的几何；
- 未处理功能 GUI。
