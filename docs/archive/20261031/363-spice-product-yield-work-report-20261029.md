# 363 香料形态产物产量 P0-AK 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：tree/root 香料产物 +1；真实形态机制未完成。

## 1. 完成内容

- `productYield` 20 条规则；
- `CropBItemResolver` 产物解析/数量；
- 统一收获按原 loot 产物差额补足；
- 20 条纯 Java 校验。

## 2. 验证

```text
PASS: 363 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- tree/root 仍是形状/产量差异，不是真实树/根；
- 原 loot 产物计数未逐项验证；
- 数值未平衡；
- 不能宣称香料形态完成。

## 4. 下一批

1. 真实树/根机制；
2. 实机收获；
3. 全量实机测试。
