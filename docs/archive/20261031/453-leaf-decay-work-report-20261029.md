# 453 树叶衰减测试 P0-CD 工作报告

> 日期：2026-10-29
> 状态：**persistent 保留确认；非 persistent 衰减未确认**
> 范围：干净存档落叶测试；无代码修改。

## 1. 完成内容

- 干净存档放 4 种树叶状态；
- randomTickSpeed=1000；
- 检查；
- 记录；
- 恢复环境。

## 2. 结果

```text
LEAF_NUT_PERSISTENT_STILL
LEAF_SPICE_PERSISTENT_STILL
```

非 persistent 树叶没有 `DECAYED`/`STILL` 标记。

## 3. 结论

- persistent=true 正常；
- 非 persistent 衰减未确认；
- 不能宣称树叶衰减完成。

## 4. 下一批

- 用 `data get block`/绝对坐标复查；
- 掉落物检查；
- 树苗掉落。
