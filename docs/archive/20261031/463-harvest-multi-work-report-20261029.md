# 463 多作物收获实机验证 P0-CI 工作报告

> 日期：2026-10-29
> 状态：**TFC/A/B 三类作物均有掉落；strawberry 异常待查**
> 范围：多作物玩家破坏收获；无代码修改。

## 1. 完成内容

- 干净存档；
- TFC 小麦 / A napa / B basil / B strawberry；
- 真实玩家破坏；
- 掉落物日志；
- 恢复环境。

## 2. 结果

确认：

```text
tfc:seeds/wheat
tfcagricultureplus:grain_bundle/wheat
tfcfarmingplus:seeds/napa_cabbage
tfcagricultureplus:crop_waste/napa_cabbage
tfcagricultureplus:spice_seed/basil
tfcagricultureplus:spice/basil
```

## 3. 异常

- strawberry 本轮无掉落日志；
- B immature basil 被移除但无掉落日志。

## 4. 未完成

- 未成熟保护；
- 数量/概率；
- 全部物种；
- creative。

## 5. 风险

- debug 命令需移除/加开关；
- 不能宣称全部收获链完成。
