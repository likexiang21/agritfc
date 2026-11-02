# 403 树木冠层持久化 P0-BF 技术分析

> 日期：2026-10-29
> 目标：修复 B 树苗生成的树叶可能因 TFC 原木不在 vanilla logs 距离计算中而快速衰减的问题。
> 约束：不推送；不伪造；未实机。

## 1. 修改

`NutTreeSaplingBlock` / `SpiceTreeSaplingBlock` 放置冠层时：

```java
leaves.defaultBlockState()
    .setValue(LeavesBlock.PERSISTENT, true)
```

- 树干仍为 TFC oak log；
- 冠层 B leaves 设为 persistent；
- 不再依赖 logs 距离 decay 判定。

## 2. 为什么

- B leaves 是 vanilla `LeavesBlock` 子类；
- TFC oak log 不一定在 `minecraft:logs` 标签中；
- 若不在，distance 计算会认为没有树干，树叶可能快速消失。

## 3. 测试

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- persistent 树叶不会自然消失，需要玩家破坏；
- 树苗生成后树冠过密/不衰减；
- 真实 TFC log 标签行为未核对。
