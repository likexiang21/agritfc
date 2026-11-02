# 404 树木冠层持久化 P0-BF 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：B 坚果/香料树冠层 persistent；未实机。

## 1. 完成内容

- `NutTreeSaplingBlock` 冠层 persistent；
- `SpiceTreeSaplingBlock` 冠层 persistent；
- 编译通过。

## 2. 验证

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- persistent 树叶不自然消失；
- 可能造成树冠过密；
- TFC 原木标签行为未核对；
- 只处理树苗生成的冠层。
