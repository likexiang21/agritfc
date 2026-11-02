# 589 厨房家具“去 UI 化”快速存取技术分析

> 日期：2026-10-30
> 状态：**静态实现；未实机**
> 用户要求：交互尽可能去 UI 化。

## 1. 背景

厨房家具有容器菜单/屏幕。玩家只是放/取一个物品时，打开整页 GUI 过重。

## 2. 实现

### 快速存入

条件：

- 非 sink；
- 玩家潜行；
- 手持物品；
- 右击家具。

流程：

- `KitchenStorageBlockEntity.quickInsert(stack)`：
  - 先合并同物品且有空位的合法槽；
  - 再找第一个空且合法的槽；
  - 遵守 `isItemValid` 与 `getSlotStackLimit`；
- 成功后播放 `ITEM_FRAME_ADD_ITEM`。

### 快速取出

条件：

- 非 sink；
- 玩家潜行；
- 空手；
- 右击家具。

流程：

- `quickExtract()` 从最后一个非空槽取 1 个；
- 进背包，失败则掉落；
- 播放 `ITEM_PICKUP`。

### 保留

- 普通右击仍打开容器菜单；
- sink 仍只做装水/倒水，不提供快速存取。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 4. 未完成

- 未实机验证潜行右击是否与方块放置冲突；
- 未做批量存取；
- 未实机确认音效/背包满时掉落。
