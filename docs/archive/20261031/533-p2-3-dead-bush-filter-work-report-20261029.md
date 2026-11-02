# 533 P2-3 枯死灌木重复过滤工作报告

> 日期：2026-10-29
> 状态：**静态过滤实现；未实机；有风险**
> 范围：P2-3。

## 1. 完成

- 新增 `neoforge:remove_features` biome modifier；
- 目标 `#minecraft:is_overworld` + 125 个 TFC biome；
- 移除 `tfc:plant/dead_bush` 与 `tfc:plant/dead_bush_patch`；
- `gradle build` 成功，JSON/引用校验通过。

## 2. 边界

- A `dead_cane` 仍存在（无 placed feature）；
- TFC 枯死灌木被全局移除，可能不是用户想要的保留方向；
- 未实机验证。

## 3. 未做

- 实机；
- A dead_cane 处理；
- 视觉。
