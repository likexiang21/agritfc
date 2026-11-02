# 579 OPEN-012 扩展：in-world 配方 JEI 催化剂技术分析

> 日期：2026-10-30
> 状态：**静态实现；未实机**
> 约束：不实机、不推送。

## 1. 问题

`AgricultureJeiPlugin.IN_WORLD` 分类注册了 409 条 B 的 in-world 配方
（205 条 axe、204 条 saw），但 `registerRecipeCatalysts` 没有给该分类添加任何催化剂。

结果：

- 玩家点配方能看到输入方块，但分类本身没有“用斧/锯”的入口；
- JEI 分类侧栏可能不显示该类别。

## 2. 修复

在 `registerRecipeCatalysts` 中：

```java
for (Holder<Item> axe : BuiltInRegistries.ITEM.getTagOrEmpty(ItemTags.AXES)) {
    registration.addRecipeCatalyst(new ItemStack(axe.value()), IN_WORLD);
}
TagKey<Item> sawTag = TagKey.create(Registries.ITEM, ResourceLocation.parse("c:tools/saw"));
for (Holder<Item> saw : BuiltInRegistries.ITEM.getTagOrEmpty(sawTag)) {
    registration.addRecipeCatalyst(new ItemStack(saw.value()), IN_WORLD);
}
```

效果：

- `#c:tools/axe` 与 `#c:tools/saw` 中所有物品都可以作为 in-world 分类催化剂；
- 207+ 条 in-world 配方可被对应工具入口检索到。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 4. 未完成

- 未实机确认 JEI 侧栏/催化剂量；
- 未添加 `hammer`/`pickaxe` 类 in-world 工具（当前数据里没有）；
- 未新增独立 category。
