# 366 草莓种子来源 P0-AM 技术分析

> 日期：2026-10-29
> 目标：给 B 草莓普通作物一个初始种子来源，闭合“TFC 草莓丛 → B 种子 → 育苗 → B 作物”链。
> 约束：不推送；不伪造；未实机。

## 1. 实现

`StrawberrySeedDropHandler`：

- 精确匹配 `tfc:plant/strawberry_bush`；
- 破坏时 20% 概率掉 1 个 `tfcagricultureplus:seeds/strawberry`；
- 不取消原 TFC 草莓掉落；
- 与 `StrawberryWasteHandler` 并存。

## 2. 链路

```text
TFC strawberry_bush
  -> B strawberry seed (20%)
  -> 种子处理 / 育苗盘
  -> B crop/strawberry
  -> 统一收获：TFC strawberry + B seed + crop_waste/strawberry
```

## 3. 测试

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 363 crop P0 checks
```

## 4. 风险

- 未实机；
- 20% 未平衡；
- 草莓丛与 B 草莓作物并存，可能重复；
- 不是正式野生生成；
- 不能宣称草莓链最终完成。
