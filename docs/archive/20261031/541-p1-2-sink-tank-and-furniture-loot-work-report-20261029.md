# 541 P1-2 水槽罐与家具掉落表复核工作报告

> 日期：2026-10-29
> 状态：**静态实现；未实机**
> 范围：OPEN-003 水槽功能扩展、OPEN-004 掉落表更正。

## 1. 完成

- sink_cabinet 增加 4000 mB 水罐；
- 注册 KITCHEN_STORAGE 的 ItemHandler/FluidHandler block capability；
- 水罐 NBT 持久化；
- 复核 204 个家具 loot table 均已存在；
- 修正 P0-3 / OPEN-004 中“家具掉落表仍缺”的错误描述。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
json 6442 / bad 0
final_static_audit problems 0
furniture loot tables 204
```

## 3. 未做

- 未实机；
- 无 GUI 水槽/水桶交互/清洗；
- 未验证家具掉落；
- 视觉未处理。
