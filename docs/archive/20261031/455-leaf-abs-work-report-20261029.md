# 455 绝对坐标树叶衰减测试 P0-CE 工作报告

> 日期：2026-10-29
> 状态：**persistent 确认；nut 有掉落线索；spice 未确认**
> 范围：绝对坐标树叶测试；无代码修改。

## 1. 完成内容

- 干净存档；
- 绝对坐标放 4 种树叶状态；
- 300t 检查；
- 记录；
- 恢复环境。

## 2. 结果

```text
ABSLEAF_NUT_PERSISTENT_STILL
ABSLEAF_SPICE_PERSISTENT_STILL
ABSLEAF_NUT_DROP
```

## 3. 未完成

- 非 persistent 叶的 `air`/`still` 未命中；
- 掉落物 ID 未读取；
- spice 普通叶未确认衰减；
- 树苗掉落未验证。

## 4. 下一批

1. `data get block` 查方块；
2. `data get entity` 查掉落物 ID；
3. 再判断衰减逻辑。
