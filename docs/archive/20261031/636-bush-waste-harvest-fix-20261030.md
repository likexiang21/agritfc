# 636 代码筛查：TFC 灌木采收不产废枝

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`BushHarvestHandler` 与 `BushRightClickHarvestHandler` 在成功采收 10 种 TFC 浆果灌木时：

- 只掉浆果；
- 把灌木切回 `stateAfterPicking`；
- **没有掉 `bush_waste`**。

`BushWasteHandler` 只在普通破坏事件里追加废枝，且上一轮加入 `event.isCanceled()` 后，被采收处理器取消的事件不会再走它。

结果：

- 正常采收路径拿不到灌木废枝；
- 只有非采收破坏才可能拿到，来源不一致。

## 2. 修复

两个采收处理器成功后都追加：

```java
final var waste = AgricultureShrubs.BUSH_WASTE.get(species.id());
if (waste != null) {
    Block.popResource(level, pos, new ItemStack(waste.get(), 1));
}
```

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,923,052 bytes
SHA-256 D33A87538B2575B55026709090501E8CB13F80F825C944C3A80C58E195CC9A98
```

## 4. 未完成

- 未实机；
- 未处理废枝掉落概率/产量平衡。
