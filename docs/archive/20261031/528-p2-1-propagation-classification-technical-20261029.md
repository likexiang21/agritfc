# 528 P2-1 逐物种繁殖方式分类与播种门技术分析

> 日期：2026-10-29
> 状态：**部分静态修复；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

用户报告：

- 育种流程“胡写”，没有按 291 技术文档；
- 此前 A/B 种子统一被育苗门拦截，没有逐物种区别。

## 2. 本次实现

新增：

```text
common/crop/CropPropagation.java
```

定义 8 种繁殖方式：

```text
SEED_DIRECT / NURSERY / RUNNER / TUBER
RHIZOME / CORM / CROWN / DIVISION
```

分类统计：

| 方式 | 条数 |
|---|---:|
| SEED_DIRECT | 46 |
| NURSERY | 27 |
| RUNNER | 1 |
| TUBER | 4 |
| RHIZOME | 4 |
| CORM | 7 |
| CROWN | 4 |
| DIVISION | 2 |

其中 `CropWasteCrops.ALL` 的 **82 个作物全部显式分类**，原型验证：

```text
PASS: all crop-waste species have explicit propagation
```

`DirectSeedPlantingGate` 改为：

- TFC 种子：保持原版直播，不拦截；
- A/B 种子：`SEED_DIRECT` 放行，走原版种植；
- 其它方式：取消直接播种，并显示对应繁殖方式提示；
- 育苗盘仍可接收所有种子，作为非直播物种的当前移栽路径。

## 3. 当前仍不是完整“无性繁殖”

- 没有新增块茎/球茎/根茎/匍匐茎/冠芽/扦插物品；
- 非直播物种暂时仍用“种子→育苗盘→幼苗→移栽”占位；
- 这解决了“所有种子一律拦截”的错误，但还不是 291 要求的完整无性繁殖链；
- 因此只能标为 partially-fixed-static。

## 4. 校验

```text
CropPropagationProto:
  species=82 classified=95 missing=0
  PASS

gradle build BUILD SUCCESSFUL
json 6442 / bad 0
lang 1105 / 1105
final_static_audit problems 0
```

## 5. 未完成

- 无性繁殖物品/配方；
- 母株性状 DataComponent；
- 温湿度对育苗成活影响；
- 间苗/培土/搭架/打顶/除草/施肥；
- 实机。
