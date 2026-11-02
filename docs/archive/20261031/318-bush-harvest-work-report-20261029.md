# 318 TFC 灌木采收替换 P0-O 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：10 种 TFC 灌木的破坏采收替换；B 灌木方块/育苗仍未完成。

## 1. 完成内容

- `BushHarvestHandler`；
- 精确匹配 10 种 TFC bush；
- `Lifecycle.FRUITING` 时：
  - 取消原破坏；
  - 掉 1–2 个 `getProductItem` 浆果；
  - 用 `stateAfterPicking` 保留灌木；
- 非结果状态走 TFC 原行为；
- 与已有 `BushWasteHandler` 并存。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有纯 Java：

```text
PASS: 274 crop P0 checks
```

## 3. 边界

- **未实机验证**；
- 只处理破坏，不替换原右键采摘；
- 与废枝 handler 的顺序未实测；
- 没有 B 灌木方块/育苗/扦插；
- 不能宣称 TFC 10 灌木完整重做完成。

## 4. 下一批

1. 实机验证灌木；
2. 右键采摘；
3. B 灌木方块；
4. TFC 29 剩余覆盖；
5. 全量实机测试。
