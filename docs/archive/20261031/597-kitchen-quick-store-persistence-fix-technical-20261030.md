# 597 厨房快速存取持久化修复技术分析

> 日期：2026-10-30
> 状态：**静态修复；未实机**
> 约束：不实机、不推送。

## 1. 问题

`quickInsert` / `quickExtract` 直接修改 `inventory.getStackInSlot(slot)` 的返回栈：

```java
current.grow(moved);
current.shrink(1);
```

没有回写 `inventory.setStackInSlot(slot, current)`。

`ItemStackHandler.getStackInSlot` 返回的栈不保证是内部引用；若不回写，
快速存取可能只在当前调用内生效，后续读取/保存仍看到旧数量。

## 2. 修复

两处都补回写：

```java
current.grow(moved);
inventory.setStackInSlot(slot, current);

current.shrink(1);
inventory.setStackInSlot(slot, current);
```

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 4. 未完成

- 未实机验证快速存/取后的保存与重载；
- 未做批量存取。
