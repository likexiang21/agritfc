# 515 P0-2 删除重复木碗/陶碗工作报告

> 日期：2026-10-29
> 状态：**静态修复完成；未实机**
> 范围：P0-2。

## 1. 完成

- 删除 B 重复木碗/陶碗物品、配方、模型、语言键；
- 移除创造页入口；
- 移除盘装菜→B 碗分装代码；
- `gradle clean build` 成功；
- 静态校验通过。

## 2. 证据

```text
BUILD SUCCESSFUL
validate_crop_p0a.py PASS
final_static_audit.py problems 0
json 6250 / bad 0
lang 1061 / 1061
models 3668
item_models 922
```

## 3. 行为影响

- 盘装菜不能分装到碗；
- 仍可直接从盘子食用；
- 以后应用 TFC `BowlBlock` 正确实现分装。

## 4. 未完成

- 实机（不执行）；
- TFC BowlBlock 分装；
- OPEN-004。
