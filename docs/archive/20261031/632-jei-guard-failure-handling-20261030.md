# 632 代码筛查：JEI 兼容保护自身失败处理

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 发现

`AgricultureJeiPlugin.onRuntimeAvailable` 中的烤箱分类保护只处理了：

```java
catch (ClassNotFoundException missing) {
    runtime.getRecipeManager().hideRecipeCategory(FLJEIPlugin.OVEN);
}
```

如果 `hideRecipeCategory` 自身抛出异常（分类未注册、JEI 内部状态变化），本模组会让客户端在 JEI runtime 初始化时崩溃。

## 2. 修复

给隐藏操作增加第二层保护：

```java
try {
    runtime.getRecipeManager().hideRecipeCategory(FLJEIPlugin.OVEN);
    ...
} catch (RuntimeException | LinkageError hideFailure) {
    LOGGER.warn("[JEI] could not hide firmalife:oven category", hideFailure);
}
```

这样即使隐藏失败，也只记录警告，不再由本模组触发新的崩溃。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,922,025 bytes
SHA-256 3809EF4E55819812E982DDBB39231CC1CFEEEC31F746C2F79812F61F795403B1
```

## 4. 未完成

- 未实机；
- 未验证 JEI 分类状态。
