# 347 球茎香料繁殖 P0-AC 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：corm 香料收获固定 2 种子；完整球茎机制未完成。

## 1. 完成内容

- `SpiceSpecies.seedYield()`；
- `CropBItemResolver.seedCountForCropBlock`；
- 统一收获按 seeds 差额补足；
- 20 条纯 Java seedYield 校验。

## 2. 验证

```text
PASS: 320 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- corm 不是独立球茎物品；
- 没有无性繁殖/分级；
- 原 loot 种子计数假设未实机验证；
- 不能宣称球茎机制完成。

## 4. 下一批

1. 实机 saffron；
2. 独立球茎物品/模型；
3. 球茎分级；
4. 全量实机测试。
