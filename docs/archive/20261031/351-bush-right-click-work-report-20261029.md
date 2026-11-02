# 351 TFC 灌木右键采收 P0-AE 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：10 种 TFC 灌木空手右键采收替换；未实机。

## 1. 完成内容

- `BushRightClickHarvestHandler`；
- 10 种 TFC bush 精确匹配；
- FRUITING 才可采；
- 掉 1–2 产物；
- `stateAfterPicking` 进入已采；
- 主入口注册。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 320 crop P0 checks
```

## 3. 边界

- **未实机**；
- 只空手；
- 与 TFC 原 useItemOn 顺序未验证；
- 可能影响其他右键监听；
- 没有 10 种逐项实机验证。

## 4. 下一批

1. 实机 10 种灌木右键；
2. 事件顺序；
3. 全量实机测试。
