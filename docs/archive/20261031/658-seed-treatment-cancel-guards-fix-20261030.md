# 658 代码筛查：种子处理右键入口未检查已取消事件

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

以下两个右键处理器没有检查 `event.isCanceled()`：

- `SeedTreatmentHandler.onRightClickItem`
- `SeedTreatmentGrowthHandler.onRightClickBlock`

它们只判断了客户端和种子组件。

## 2. 后果

- 其它模组/保护逻辑取消右键后，本模组仍可能消耗副手堆肥/木灰/石灰，给种子写入处理阶段；
- 仍可能调度一次作物生长 boost；
- 多个交互叠加时产生不应有的副作用。

## 3. 修复

两个入口开头统一：

```java
if (event.isCanceled()) {
    return;
}
```

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,999 bytes
SHA-256 24C0D90922192E4DB75619D250DAB0DECD2035DF3727A44E7FD15B73B1B56A50
```

## 5. 未完成

- 未实机；
- 未验证其它 SeedTreatment 相关入口。
