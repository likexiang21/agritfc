# 423 树木生长失败定位 P0-BO 工作报告

> 日期：2026-10-29
> 状态：**修复一个树生成 bug；树生长仍未验证**
> 范围：NutTreeSaplingBlock / SpiceTreeSaplingBlock 底部原木修复。

## 1. 完成内容

- 代码审查发现并修复：
  - `growTree` 末尾 `removeBlock(pos)` 会删掉底部树干；
  - 两个树苗类都删除该行；
- 重新构建；
- 服务器/客户端日志保存。

## 2. 结果

绝对坐标测试仍然没有树干/树冠标记；树苗 stage 检查因 `forceload remove` 在检查前而无效。

## 3. 边界

- 树生成未实机验证；
- 测试设计有缺陷；
- 没有确认树苗是否仍在；
- 没有验证树冠/树叶衰减；
- 测试后已恢复环境。

## 4. 证据

`mod_rebuild/docs/audit/runtime-tree-absolute-20261029.log`

## 5. 下一批

1. 固定玩家平台；
2. 玩家区块 random tick；
3. stage 检查；
4. 树干/树冠检查。
