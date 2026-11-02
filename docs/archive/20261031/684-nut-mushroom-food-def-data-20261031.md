# 684 全盘检查：坚果/坚果粉/野生蘑菇没有食物定义

> 日期：2026-10-31
> 状态：**数据已修复；静态构建通过；未实机**

## 1. 发现

TFC 的食物系统由 `FoodCapability` + `data/<ns>/tfc/food/*.json` 驱动；`FoodDefinition` 才把 `TFCComponents.FOOD` 挂到物品 stack 上。

检查 `data/tfcagricultureplus/tfc/food/` 后发现：

- 8 个坚果 `tfcagricultureplus:<nut>` **没有食物定义**；
- 8 个 `ground_nut/<nut>` **没有食物定义**；
- 15 个 `wild_mushroom/<species>` **没有食物定义**；
- 因此虽然文档 291 §9.2/§9.3 把它们写成可食用/可加工，实际 `FoodCapability.has(stack)` 为 false，不能食用，也不会进入 TFC 食物腐烂/营养链。

## 2. 修复

新增 31 个 `tfc/food/*.json`：

- 8 个坚果：hunger 4、saturation 0.5、protein 1.5、decay 1.2；
- 8 个坚果粉：hunger 2、saturation 0.5、protein 1.0、decay 1.0；
- 15 个野生蘑菇方块物品：hunger 2、saturation 0.5、protein 1.0、decay 1.0。

野生蘑菇的 `ingredient.item` 使用其 BlockItem ID：

```json
"ingredient": { "item": "tfcagricultureplus:wild_mushroom/oyster" }
```

因此菌包采出的蘑菇方块物品现在也带 TFC food 组件，可食用。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,937,449 bytes
SHA-256 FB7B183E9ABACB2009E59A17A92D20690490DA588D50AC19E1FD37907C6873BA
```

## 4. 未完成

- 未实机验证食物腐烂/营养；
- 蘑菇尚未增加干燥/烹饪加工配方；
- 香料产品的食物属性仍按“调料/加工原料”处理，未全部设为可食用。
