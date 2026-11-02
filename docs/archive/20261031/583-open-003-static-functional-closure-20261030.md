# 583 OPEN-003 静态功能收口评估

> 日期：2026-10-30
> 状态：**静态功能达到用户限定范围；未实机**
> 约束：不实机、不推送。

## 1. 已实现

6 种家具按 `StorageKind` 分流：

| 家具 | 过滤 | 堆叠 |
|---|---|---:|
| counter_cabinet | 任意 | 64 |
| half_cabinet | 任意 | 16 |
| sink_cabinet | 仅流体容器 | 1 |
| spice_rack | 仅 `#tfcagricultureplus:spices` | 64 |
| food_display | 仅食物 | 64 |
| fruit_bowl | 仅食物 | 1 |

独立名称：

```text
block_entity.tfcagricultureplus.kitchen_storage.<kind>
```

水槽：

- 4000 mB 水罐；
- 只接受水；
- block fluid capability；
- 手持容器装水/倒水。

视觉：

- 6 种共享模型轮廓不同；
- 不再全是同一立方体。

## 2. 用户限定

用户明确：

> 水槽不涉及“清洗”“保鲜”功能，水槽仅作为方便取用水的一个家具。

因此以下不再算缺陷：

- 无清洗；
- 无保鲜；
- 无水槽 GUI；
- 共用 9 格菜单/屏幕。

## 3. 结论

OPEN-003 的“家具功能分化”在静态层面已达到用户限定范围：

- 过滤不同；
- 堆叠不同；
- sink 有独立水罐；
- 视觉有差异。

剩余只有实机验证。

## 4. 未完成

- 未实机；
- 未做每种家具独立槽位数；
- 未做保鲜/清洗（范围外）。
