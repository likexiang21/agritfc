# 327 坚果壳副产 P0-S 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：8 种坚果壳物品、掉落与堆肥标签；完整坚果链未完成。

## 1. 完成内容

- 8 个 `nut_shell/<nut>` 物品；
- 8 个 item model；
- en/zh 语言；
- 8 条加入 `tfc:compost_browns/high`；
- 树叶秋熟掉落坚果时同时掉 1 个壳；
- 创造页加入 8 个壳。

## 2. 验证

```text
PASS: 283 crop P0 checks
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, 20 ground spices, 8 ground nuts, 8 nut shells, tags valid
```

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

`processResources`：

```text
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机验证**；
- 壳目前只有堆肥出口；
- 后 3 个坚果仍无树来源；
- 贴图仍为 TFC 临时资源；
- 不能宣称坚果内容完成。

## 4. 下一批

1. 新树；
2. 壳燃料/活性炭；
3. TFC 29 剩余；
4. 全量实机测试。
