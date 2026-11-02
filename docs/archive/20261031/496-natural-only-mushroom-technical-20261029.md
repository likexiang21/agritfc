# 496 自然专用蘑菇拒绝实机验证 P0-CZ 技术分析

> 日期：2026-10-29
> 目标：实机验证 4 种 naturalOnly 蘑菇不能装菌包。
> 约束：不推送；不伪造；调试命令为临时测试入口。

## 1. 测试

干净存档：

- 两个空 `mushroom_bag[stage=0]`；
- use_with porcini 到 ~2；
- use_with oyster 到 ~4；
- 检查 stage。

## 2. 实机结果

```text
NATURAL_PORCINI_REJECTED
OYSTER_INOCULATED
```

- porcini 菌包保持 stage0；
- oyster 菌包进入 stage1。

## 3. 结论

自然专用 4 种蘑菇的菌包拒绝规则实机生效；可栽培种正常接种。

## 4. 未确认

- 其余 3 种 naturalOnly 逐一；
- 温度错误提示；
- 自然世界生成。
