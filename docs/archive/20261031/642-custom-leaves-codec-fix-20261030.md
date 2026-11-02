# 642 代码筛查：自定义树叶方块未重写 codec

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`SpiceTreeLeavesBlock` 和 `NutLeavesBlock` 的构造函数都是：

```java
public SpiceTreeLeavesBlock(SpiceTreeSpecies species, Properties properties)
public NutLeavesBlock(NutTreeSpecies species, Properties properties)
```

但它们没有重写 `codec()`，继承了 vanilla `LeavesBlock` 的：

```java
public MapCodec<? extends LeavesBlock> codec() {
    return simpleCodec(LeavesBlock::new);
}
```

一旦 BlockState/Block codec 被使用，会尝试构造普通 `LeavesBlock`，丢失 B 的 species 类型，甚至造成类型不匹配。

## 2. 修复

两个类都重写：

```java
@Override
public MapCodec<? extends LeavesBlock> codec() {
    return simpleCodec(properties -> new SpiceTreeLeavesBlock(species, properties));
}
```

`NutLeavesBlock` 同理。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,924,120 bytes
SHA-256 A9B1D14063DB73868E02B0B5406593BFC4A14A266C7437C1E8430EDD11D83AF8
```

## 4. 未完成

- 未实机；
- 未逐项验证所有自定义 `Block` 子类的 codec。
