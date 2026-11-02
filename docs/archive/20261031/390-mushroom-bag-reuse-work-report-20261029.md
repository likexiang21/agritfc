# 390 菌包复用 P0-AY 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：stage 3 菌包重新接种；未实机。

## 1. 完成内容

- `MushroomBagBlock.useItemOn` 允许 stage 0 或 3；
- stage 3 重新 inoculate；
- progress 重置；
- 消耗野生蘑菇方块；
- 回到 stage 1。

## 2. 验证

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 无次数/耐久限制；
- 自然专用仍拒绝；
- stage 3 视觉未验证；
- 可能与其他右键冲突；
- 不能宣称蘑菇链完成。

## 4. 下一批

1. 实机复用；
2. 次数/耐久；
3. GUI/提示；
4. 全量实机测试。
