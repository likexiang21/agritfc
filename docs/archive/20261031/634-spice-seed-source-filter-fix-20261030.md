# 634 代码筛查：野草香料种子源选中无种子树种

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`SpiceSeedDropHandler` 在短草/高草掉落香料种子时，从全部 `SpiceSpecies.values()` 随机：

```java
final SpiceSpecies[] spices = SpiceSpecies.values();
final SpiceSpecies spice = spices[level.random.nextInt(spices.length)];
final var seed = AgricultureSpices.SEEDS.get(spice.id());
```

但 5 个 `tree` 形态物种（pimento/cinnamon/clove/nutmeg/star_anise）在 `AgricultureSpices.SEEDS` 中没有条目，`seed` 为 null，掉落被静默跳过。

结果：

- 5/20 的随机结果不会产生任何种子；
- 树形香料的繁殖入口仍只有树苗，但野草种子源没有意义地空转。

## 2. 修复

只从 `AgricultureSpices.SEEDS` 中实际存在的物种选择：

```java
final SpiceSpecies[] spices = Arrays.stream(SpiceSpecies.values())
    .filter(spice -> AgricultureSpices.SEEDS.containsKey(spice.id()))
    .toArray(SpiceSpecies[]::new);
if (spices.length == 0) return;
```

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,922,504 bytes
SHA-256 D214794275030D777106CE6155EA17DD76416862E9837BB642F3708416F1388D
```

## 4. 未完成

- 未实机；
- 未处理树形香料的独立种子/树苗来源设计。
