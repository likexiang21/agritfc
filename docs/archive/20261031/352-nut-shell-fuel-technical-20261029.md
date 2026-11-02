# 352 坚果壳/废枝叶燃料 P0-AF 技术分析

> 日期：2026-10-29
> 目标：让 B 的坚果壳与 crop_waste 有实际炉用出口，而不只是堆肥占位。
> 约束：不推送；不伪造；未实机。

## 1. 实现

`NutShellFuelHandler` 监听 `FurnaceFuelBurnTimeEvent`：

- `nut_shell/*` → 200 tick；
- `crop_waste/*` → 100 tick；
- 其他物品不处理。

## 2. 为什么用事件

- 不改变物品注册；
- 不新增燃料物品；
- 兼容其他燃料事件；
- 所有 8 种壳、82 种 crop_waste 自动覆盖。

## 3. 测试

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 320 crop P0 checks
```

## 4. 风险

- 未实机；
- 100/200 tick 未平衡；
- TFC 炉/其他炉是否都走该事件需实机确认；
- 与 TFC 原有燃料值可能冲突；
- 不影响堆肥标签。
