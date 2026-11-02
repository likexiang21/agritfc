# 394 自然专用蘑菇提示 P0-BA 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：4 种自然专用蘑菇的菌包提示；未实机。

## 1. 完成内容

- `useItemOn` naturalOnly 分支；
- actionbar 提示；
- 不消耗物品；
- en/zh 文案。

## 2. 验证

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 只 actionbar；
- 不区分物种；
- 可能被其他右键抢；
- 不能宣称蘑菇链完成。

## 4. 下一批

1. 实机提示；
2. 物种专属文案；
3. GUI；
4. 全量实机测试。
