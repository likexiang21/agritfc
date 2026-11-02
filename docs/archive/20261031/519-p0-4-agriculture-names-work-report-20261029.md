# 519 P0-4 逐物种人工名称工作报告

> 日期：2026-10-29
> 状态：**静态修复完成；未实机；不改贴图**
> 范围：P0-4。

## 1. 完成

- 农业物品名称 246 键/语言；
- 木材/家具/木工名称 510 键/语言；
- 中英双语同步；
- 中文 item/block 名称中的 ASCII 原始 ID 清零；
- `gradle build` 成功。

## 2. 关键结果

```text
lang en_us 1061 / zh_cn 1061
missing 0 / extra 0
中文 item/block 名称含 ASCII: 0
json 6425 / bad 0
final_static_audit problems 0
```

## 3. 未做

- 未改贴图（视觉问题，用户明确暂不处理）；
- 未实机逐项看 tooltip；
- 未处理 JEI/手册可读性（P1）；
- 未处理家具功能（P1）。

## 4. 产物

- 518 技术分析；
- `lang/en_us.json`、`lang/zh_cn.json`。
