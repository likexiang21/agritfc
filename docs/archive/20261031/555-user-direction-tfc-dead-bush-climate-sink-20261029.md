# 555 用户方向调整：TFC 枯死灌木原版处理 / 气候接口 / 水槽范围

> 日期：2026-10-29
> 状态：**按用户新指令调整；未实机**
> 约束：视觉可用但不做大面积贴图重绘；暂不实机。

## 1. 枯死灌木：撤销 B 过滤，恢复 TFC 原版

用户指令：

> 枯死灌木读取 TFC 原版处理方式。

处置：

- 删除 `data/tfcagricultureplus/neoforge/biome_modifier/remove_duplicate_dead_bush.json`；
- 不再移除 `tfc:plant/dead_bush` / `dead_bush_patch`；
- TFC 世界生成恢复原版；
- A 的 `dead_cane` 仍按其自身逻辑产生；
- **不再由 B 做枯死灌木过滤**。

结论：OPEN-001 标记为“按用户方向恢复原版，未修复重复观感”。

## 2. 温湿度：对齐 TFC 现有接口

检查 `MushroomBagBlockEntity`：

```java
Climate.getAverageTemperature(level, pos)
Climate.fromVanilla(species.preferredTemperature())
```

已经使用 TFC 的 `Climate` 接口，不是自定义温度系统。

添加说明：

- 蘑菇菌包只使用 TFC 平均温度；
- 没有湿度阈值；如后续需要湿度，直接使用 `Climate.getAverageRainfall` / `ClimateRange`；
- 育苗盘暂不硬编码温湿度；移栽后由 TFC/A 作物自身气候逻辑接管。

## 3. 水槽范围

用户明确：

> 水槽不涉及“清洗”“保鲜”功能，水槽仅作为方便取用水的一个家具。

因此：

- 保留 4000 mB 水罐；
- 保留手持容器装水/倒水；
- 保留 block capability；
- **不实现**清洗、浸泡、洗碗、保鲜、GUI 水槽；
- 之前文档中的“未实现清洗/保鲜/GUI”从缺陷改为**范围外**。

## 4. 校验

```text
json 6483 / bad 0（删除 1 个 modifier 后）
final_static_audit problems 0
```

## 5. 未完成

- 未实机；
- 木工视觉对齐仍未做（用户允许视觉，但不做大面积贴图重绘；模型/贴图对齐方案另批）；
- OPEN-012 JEI 独立分类仍未新增。
