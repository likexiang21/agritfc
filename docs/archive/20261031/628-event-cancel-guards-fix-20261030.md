# 628 代码筛查：事件处理器缺少取消状态检查

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

多个 `BlockEvent.BreakEvent` 处理器在事件已被取消时仍会执行：

```text
BushHarvestHandler
BushWasteHandler
GrainHarvestHandler
MacadamiaDropHandler
SpiceSeedDropHandler
StrawberrySeedDropHandler
StrawberryWasteHandler
WildNutDropHandler
```

这些处理器只检查了：

- 是否创造模式；
- 是否 ServerLevel；
- 方块 ID/年龄。

但未检查：

```java
event.isCanceled()
```

## 2. 后果

如果其它处理器/保护逻辑先取消了破坏事件，这些处理器仍可能：

- 额外掉落作物/种子/废枝叶；
- 取消事件后手动移除方块；
- 在保护区域内产生掉落物。

这是本模组事件顺序与边界处理的问题。

## 3. 修复

在上述 8 个处理器开头统一加入：

```java
if (event.isCanceled()) {
    return;
}
```

已有检查的处理器保持不变：

- `ACropSeedReturnHandler`
- `TfcSeedReturnHandler`
- `CropWasteHandler`
- `UnifiedCropHarvestHandler`

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,825 bytes
SHA-256 1093B0206CF7CC7BF73586FEB7D09B7407810D8C21F866DD3EDF436361A05041
```

## 5. 未完成

- 未实机；
- 未验证所有事件优先级组合。
