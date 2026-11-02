# 550 P2-1 扩展：水生繁殖材料放置技术分析

> 日期：2026-10-29
> 状态：**静态实现；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 背景

21 个 `propagation_stock/<species>` 上轮只支持耕地放置。
水生/湿地作物（taro、water_chestnut、water_caltrop、lotus 等）需要水。

## 2. 实现

`PropagationStockItem.useOn` 现在有两条路径：

### 2.1 耕地

- 点击耕地；
- 目标上方必须为空；
- 作物 state 的 `age` 设 0；
- `canSurvive` 后放置。

### 2.2 水源

- 点击的水方块必须是 **source**；
- 直接用作物方块调用 `getStateForPlacement(new BlockPlaceContext(context))`；
- 让 `FloodedCropBlock` 自己设置 `fluid` 属性；
- 再将 `age` 设 0；
- `canSurvive` 后替换水方块放置。

## 3. 边界

- 只有真正实现 `FloodedCropBlock` 的作物才会在水源上成功；
- 普通作物若 `canSurvive` 在水的目标位置不成立，仍会 PASS；
- 没有实现“先排水再种”或“浅水高度”；
- 未实机验证。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 5. 未完成

- 实机；
- 水稻田水深/灌溉；
- 母株性状；
- 育苗/缓苗。
