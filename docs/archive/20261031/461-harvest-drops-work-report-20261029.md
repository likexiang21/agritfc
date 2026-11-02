# 461 收获掉落物 ID 实机验证 P0-CH 工作报告

> 日期：2026-10-29
> 状态：**basil/strawberry 掉落物 ID 已确认**
> 范围：临时 debug 命令 + 干净存档实机。

## 1. 完成内容

- 添加 `tfcplusdebug_drops` 临时命令；
- 真实玩家破坏成熟作物；
- 读取 ItemEntity ID/数量；
- 记录：
  - seeds/strawberry；
  - spice/basil；
  - spice_seed/basil；
  - tfc:food/strawberry；
  - crop_waste/strawberry；
- 恢复环境。

## 2. 结论

玩家破坏路径的掉落种子/产品/废枝叶 top-up 实际生效。

## 3. 未完成

- 全部物种；
- 概率/数量；
- 未成熟保护；
- creative；
- basil 是否有对应 waste。

## 4. 风险

- debug 命令必须发布前移除/加开关；
- 不能宣称全部收获链完成。
