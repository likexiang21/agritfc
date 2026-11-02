# 593 移除锅状态死方法技术分析

> 日期：2026-10-30
> 状态：**静态清理；未实机**
> 用户要求：减少弹出式提示文本。

## 1. 问题

`CookingPanBlockEntity.status()` 仍返回 4 个已删除的 `message.tfcagricultureplus.pan.*` 翻译键：

```java
public Component status() {
    if (!hasHeat()) return Component.translatable("...no_heat");
    if (!hasOil()) return Component.translatable("...no_oil");
    if (entries.isEmpty()) return Component.translatable("...empty");
    return Component.translatable("...contents", ...);
}
```

但 587/588 之后没有调用方，属于死代码。

## 2. 清理

- 删除 `status()`；
- 删除 `net.minecraft.network.chat.Component` import；
- 保留 `hasHeat()` / `hasOil()` / `entries` 等实际字段。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 4. 未完成

- 未实机；
- 其它交互类的 `MESSAGE` 常量仍存在但已无输出，未清理。
