# 345 A 87 全量种子解析 P0-AB 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：A 87 作物方块的全部种子解析；逐作物实机未做。

## 1. 完成内容

- `CropBItemResolver` 对 A 方块改用路径解析；
- `ACropSeedReturnHandler` 改用路径解析；
- 不再要求 `CropWasteCrops` 命中；
- 无废枝叶的 A 作物也能进入统一收获；
- 有废枝叶的继续追加 waste。

## 2. 验证

```text
PASS: 300 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- A 种子 ID 是否全部等于路径需逐项核对；
- 特殊 A 作物/双格未逐项验证；
- 没有 87 作物逐条收获回归；
- 不能宣称 A 87 完成验收。

## 4. 下一批

1. 逐作物核对 A 种子 ID；
2. 双格/特殊作物；
3. 全量实机测试。
