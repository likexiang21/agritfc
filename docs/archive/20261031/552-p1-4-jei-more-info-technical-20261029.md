# 552 P1-4 扩展：金属罐/陶盘/繁殖材料 JEI 信息页技术分析

> 日期：2026-10-29
> 状态：**静态实现；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 背景

P1-4 已为 10 类设备加入 JEI 信息页，但以下新增物品仍没有说明：

- 19 个金属罐；
- 18 个陶盘/木盘变体；
- 21 个无性繁殖材料。

## 2. 新增 JEI 信息页

`addDeviceInfo` 新增三个循环：

```java
for (can : AgricultureItems.METAL_CANS.values()) addInfo("metal_can");
for (plate : AgriculturePlates.ITEMS_BY_VARIANT.values()) addInfo("serving_plate");
for (stock : AgricultureItems.PROPAGATION_STOCKS.values()) addInfo("propagation_stock");
```

内容：

- `metal_can`：500 mB、铁砧/锻铁板来源、流体标签、图标显示液体；
- `serving_plate`：打制/烧制/烧前染色、放置装菜、保存菜品数据；
- `propagation_stock`：耕地/浅水放置、age 0、1 产品→2 材料。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
lang 1129 / 1129
final_static_audit problems 0
custom recipe isSpecial 4/4
```

## 4. 未完成

- 仍未新增 B 独立 JEI recipe category；
- 烹饪锅仍是动态组合；
- 未实机确认信息页；
- 未处理视觉。
