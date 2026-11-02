# 406 树形香料形态拆分 P0-BG 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：5 个 tree form 香料只保留树形态；未实机。

## 1. 完成内容

- `AgricultureSpices` 对 tree form 跳过 crop/seed 注册；
- 15 个 crop-form 香料仍注册；
- 5 个 tree-form 香料只保留 product/waste/ground + 树；
- 树树叶 loot 增加 `spice_waste` 5%；
- validator 改为 15 crops + 5 trees。

## 2. 验证

```text
PASS: 15 spice crops, 5 spice trees, 20 ground spices
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 旧 crop/seed 资源未删除；
- 树产物只从树链获得；
- 没有树苗到成树的完整实机验证；
- 不能宣称香料链最终验收。

## 4. 下一批

1. 实机 5 树；
2. 清理旧 crop/seed 资源（需确认不误删）；
3. 产物平衡；
4. 全量实机测试。
