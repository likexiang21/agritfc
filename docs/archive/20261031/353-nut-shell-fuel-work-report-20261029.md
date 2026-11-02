# 353 坚果壳/废枝叶燃料 P0-AF 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：nut_shell 200 tick、crop_waste 100 tick 燃料；未实机。

## 1. 完成内容

- `NutShellFuelHandler`；
- `FurnaceFuelBurnTimeEvent`；
- 8 种 nut_shell → 200 tick；
- 82 种 crop_waste → 100 tick；
- 主入口注册。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 320 crop P0 checks
```

## 3. 边界

- **未实机**；
- 数值未平衡；
- TFC 炉是否全部走该事件未验证；
- 可能与其他燃料冲突；
- 不改变堆肥用途；
- 不能宣称加工链完成。

## 4. 下一批

1. 实机燃料；
2. 数值平衡；
3. 壳炭/堆肥扩展；
4. 全量实机测试。
