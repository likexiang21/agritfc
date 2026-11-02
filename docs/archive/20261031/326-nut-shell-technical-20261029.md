# 326 坚果壳副产 P0-S 技术分析

> 日期：2026-10-29
> 目标：为 8 种坚果增加坚果壳副产，补齐坚果收获的壳出口。
> 约束：不推送；不伪造；贴图暂用 TFC。

## 1. 范围

8 种：

```text
acorn · chestnut · pine_nut · hickory_nut ·
pistachio · cashew · macadamia · beechnut
```

新增：

- `nut_shell/<nut>` 8 个物品；
- item model；
- en/zh 语言；
- 全部加入 `tfc:compost_browns/high`，`replace:false`。

## 2. 收获

`TFCLeavesNutStateMixin` 在秋熟随机掉落时：

- 掉 1 个坚果；
- 再掉 1 个对应坚果壳；
- 仍只对 5 个坚果组的树叶生效。

## 3. 测试

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

资源：

```text
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, 20 ground spices, 8 ground nuts, 8 nut shells, tags valid
```

纯 Java：

```text
PASS: 283 crop P0 checks
```

## 4. 风险

- 未实机验证；
- shellItemId 由 nut item id 派生，需实机核对；
- 壳没有燃料/活性炭等更具体用途；
- 后 3 个坚果仍没有树来源。
