# 328 香料形态类 P0-T 技术分析

> 日期：2026-10-29
> 目标：把 20 种香料的 form 数据从纯字符串落成不同的 CropBlock 子类，至少区分形状/碰撞箱。
> 约束：不推送；不伪造；未实机。

## 1. 实现

`SpiceCropBlocks` 提供：

- `Herb`
- `Shrub`
- `Tree`
- `Vine`
- `Root`
- `Corm`

均 extends `CropBlock`，当前只覆盖 `getShape`：

| 形态 | 形状 |
|---|---|
| herb | 2..14 × 10 |
| shrub | 1..15 × 12 |
| tree | 3..13 × 16 |
| vine | 5..11 × 16 |
| root | 3..13 × 8 |
| corm | 4..12 × 8 |

`AgricultureSpices.newSpiceCrop` 按 `SpiceSpecies.form()` 选择子类。

## 2. 仍然不是完整形态

- tree 没有树干/树叶/树苗；
- vine 没有攀爬/支架；
- corm 没有球茎繁殖；
- shrub 没有灌木生命周期；
- 所有作物仍是 8 龄 CropBlock；
- 没有专属模型/贴图。

本轮只完成了“不同 form 至少不再是同一个空类”的代码层第一步。

## 3. 测试

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有纯 Java：

```text
PASS: 283 crop P0 checks
```

## 4. 风险

- 未实机验证；
- CropBlock 子类沿用父 codec，尚未验证数据包序列化；
- 形状与模型不匹配（模型仍为 cross）；
- 不能宣称香料形态完成。
