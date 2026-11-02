# 535 OPEN-004 厨房家具配方重做工作报告

> 日期：2026-10-29
> 状态：**配方静态重做完成；未实机**
> 范围：OPEN-004 家具配方部分。

## 1. 完成

- 删除旧 204 条木板占位配方；
- 用 TFC/AFC lumber、rod、wrought iron sheet、glass 重做 204 条；
- 6 类配方图案全部区分；
- 本地 shaped 冲突 groups=347/347；
- `gradle build` 成功。

## 2. 校验

```text
json 6442 / bad 0
final_static_audit problems 0
shaped groups 347 / 347
```

## 3. 未做

- 未实机；
- 家具掉落表已复核存在（204 个），仍需实机验证；
- 家具功能仅 P1-2 部分分化；
- 未处理视觉。
