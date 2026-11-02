# 644 代码筛查：香料作物形状子类未重写 codec

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`SpiceCropBlocks` 的 6 个形状类：

```text
Herb / Shrub / Tree / Vine / Root / Corm
```

都只重写 `getShape`（Vine 还重写 `canSurvive`），构造函数是 `(Properties)`，但没有重写 `codec()`。

继承的是 vanilla `CropBlock`：

```java
public MapCodec<? extends CropBlock> codec() {
    return simpleCodec(CropBlock::new);
}
```

一旦 codec 被使用，会构造普通 `CropBlock`，丢失 B 的香料形状和 Vine 的棚架 `canSurvive` 逻辑。

## 2. 修复

6 个类分别增加：

```java
@Override
public MapCodec<? extends CropBlock> codec() {
    return simpleCodec(Herb::new); // 各子类自己的构造器
}
```

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,090 bytes
SHA-256 6E2AAD104A29DCB70874F800474E75D0DFA3B9D891BCD01B843172AEBD67E606
```

## 4. 未完成

- 未实机；
- 未验证其它自定义 CropBlock 子类。
