# 529 P2-1 逐物种繁殖方式分类与播种门工作报告

> 日期：2026-10-29
> 状态：**部分静态修复；未实机**
> 范围：P2-1。

## 1. 完成

- 新增 `CropPropagation`，8 种繁殖方式；
- 82 个作物废枝叶物种全部显式分类；
- 播种门按物种放行/拦截；
- 提示改为具体繁殖方式；
- 育苗盘仍作为非直播物种的移栽路径；
- Patchouli 育苗页同步改为“直播 vs 育苗”。

## 2. 校验

```text
CropPropagationProto PASS
all crop-waste species explicit
gradle build BUILD SUCCESSFUL
json 6442 / bad 0
lang 1105 / 1105
final_static_audit problems 0
```

## 3. 明确未做

- 块茎/球茎/根茎/匍匐茎/冠芽/扦插物品链；
- 母株性状组件；
- 温湿度/缓苗；
- 农艺管理（间苗/培土/搭架/打顶/除草/施肥）；
- 实机。
