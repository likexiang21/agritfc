# 409 失效树形作物资源清理 P0-BH 工作报告

> 日期：2026-10-29
> 状态：**已完成清理，未推送、未提交远程**
> 范围：20 个 dead 资源 + 语言键；clean build 通过。

## 1. 完成内容

- 删除 5 个 tree form 的旧 blockstate/model/item model/loot；
- 删除对应语言键；
- 保留树形态 leaves/sapling/product/waste/ground；
- `clean build` 通过。

## 2. 验证

```text
gradle clean build
BUILD SUCCESSFUL

PASS: 99 item models ... 15 spice crops, 5 spice trees ...
BAD_REFS 0
```

## 3. 边界

- 未实机；
- 旧存档方块 ID 缺失风险；
- 没有回收站恢复；
- 不能宣称最终验收。

## 4. 下一批

1. 实机旧存档兼容；
2. 全量实机测试。
