# 329 香料形态类 P0-T 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：6 个 CropBlock 子类形状；完整树/藤/球茎机制未实现。

## 1. 完成内容

- `SpiceCropBlocks`：
  - Herb / Shrub / Tree / Vine / Root / Corm；
- `AgricultureSpices` 按 form 选择子类；
- 6 个 getShape 实现；
- 编译通过。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有：

```text
PASS: 283 crop P0 checks
```

## 3. 边界

- 未实机；
- 只区分形状，不是树/藤/球茎机制；
- 模型仍是 cross；
- 子类 codec 未单独验证；
- 不能宣称香料形态完成。

## 4. 下一批

1. 树/藤/球茎真实机制；
2. 专属模型；
3. 实机；
4. TFC 29 剩余。
