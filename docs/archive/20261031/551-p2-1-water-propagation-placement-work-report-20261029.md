# 551 P2-1 扩展：水生繁殖材料放置工作报告

> 日期：2026-10-29
> 状态：**静态实现；未实机**
> 范围：OPEN-007 水生繁殖。

## 1. 完成

- `PropagationStockItem` 增加水源目标路径；
- 使用作物方块 `getStateForPlacement` 获取 `fluid` 属性；
- 之后设 age0、canSurvive、放置；
- 耕地路径保持。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 3. 未做

- 未实机；
- 水深/灌溉；
- 母株性状；
- 育苗/缓苗。
