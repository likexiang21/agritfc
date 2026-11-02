# 546 P1-2 扩展：水槽玩家交互技术分析

> 日期：2026-10-29
> 状态：**静态实现；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 背景

上一轮给 sink_cabinet 增加了 4000 mB 水罐和 capability，但玩家只能通过管道交互。

本轮补充玩家手持交互：

```java
if (kind == SINK_CABINET
    && be.sinkTank() != null
    && FluidUtil.interactWithFluidHandler(player, hand, be.sinkTank())) {
    return ItemInteractionResult.sidedSuccess(level.isClientSide());
}
```

## 2. 行为

- 手持装水容器右键 sink：
  - 水倒入 4000 mB 水罐；
  - 容器留下空容器/按 TFC 逻辑处理；
- 手持空容器右键已装水 sink：
  - 从水罐装水；
- 非 sink 家具不触发此分支；
- 水罐仍只接受 `minecraft:water`。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 4. 未完成

- 没有水槽 GUI；
- 没有清洗/浸泡/洗碗逻辑；
- 未实机验证桶/罐/金属罐交互；
- 未处理视觉。
