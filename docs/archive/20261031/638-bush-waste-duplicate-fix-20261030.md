# 638 代码筛查：TFC 灌木采收废枝可能重复掉两份

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

上一轮给 `BushHarvestHandler` 和 `BushRightClickHarvestHandler` 增加 `bush_waste` 后，出现事件顺序重叠：

`TFCAgriculturePlus` 注册顺序是：

```java
NeoForge.EVENT_BUS.addListener(BushWasteHandler::onBlockBreak);   // 先
...
NeoForge.EVENT_BUS.addListener(BushHarvestHandler::onBlockBreak); // 后
```

对一棵正在结果的 TFC 灌木，破坏时：

1. `BushWasteHandler` 先运行，事件尚未取消，掉一份 `bush_waste`；
2. `BushHarvestHandler` 随后取消事件、采收，并再掉一份 `bush_waste`。

结果正常破坏成熟灌木会得到 **两份废枝**。

## 2. 修复

`BushWasteHandler` 跳过 `LIFECYCLE == FRUITING`：

```java
if (state.hasProperty(SeasonalPlantBlock.LIFECYCLE)
    && state.getValue(SeasonalPlantBlock.LIFECYCLE) == Lifecycle.FRUITING) {
    return;
}
```

这样：

- `BushWasteHandler` 先跑：跳过，`BushHarvestHandler` 只掉一份；
- `BushHarvestHandler` 先跑：取消事件，`BushWasteHandler` 的取消检查直接返回；
- 非结果灌木仍由 `BushWasteHandler` 掉废枝。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,923,274 bytes
SHA-256 6B9801C5DCA4FC5512807011DFC31436F2A75375095732DA826CDA886094E073
```

## 4. 未完成

- 未实机；
- 未验证其它果实类 SeasonalPlantBlock 的掉落。
