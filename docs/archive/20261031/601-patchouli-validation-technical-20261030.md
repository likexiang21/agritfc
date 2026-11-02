# 601 手册条目静态验证脚本技术分析

> 日期：2026-10-30
> 状态：**静态验证 PASS；未实机**
> 约束：不实机、不推送。

## 1. 目的

为 Patchouli 内容建立可重复验证，避免只靠人工翻页。

## 2. 检查项

`validate_patchouli_entries.py`：

- 每语言 **10 个 entry、4 个 category**；
- entry 的 `category` 必须存在；
- 每个 entry 至少 1 页；
- spotlight 的 B 物品必须在 item model 或 blockstate 中存在；
- crafting 页的 B recipe ID 必须存在；
- 中英 entry 路径与页数一致。

## 3. 结果

```text
entries 10
categories 4
problems 0
PASS: patchouli entries
```

> 备注：此前“20 entries / 8 categories”是**中英合计**，不是单语言数量；脚本已按单语言 10/4 校正。

## 4. 边界

- 只验证资源/引用；
- 不验证游戏内排版、翻页、图片渲染；
- 未实机。
