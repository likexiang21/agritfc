# 324 坚果初加工 P0-R 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：8 种坚果的坚果粉与石臼配方；完整坚果链未完成。

## 1. 完成内容

- `AgricultureItems.GROUND_NUTS` 8 个；
- 8 条 `tfcagricultureplus:mortar` 配方；
- 8 个 item model；
- en/zh 语言；
- 创造页加入。

## 2. 验证

```text
PASS: 282 crop P0 checks
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, 20 ground spices, 8 ground nuts, tags valid
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
- 坚果粉暂无营养/烹饪用途；
- 8 个坚果中只有一部分有树/掉落来源；
- 没有坚果壳/油/烤制；
- 贴图仍为 TFC 临时资源。

## 4. 下一批

1. 新树/坚果来源；
2. 坚果营养/烹饪；
3. TFC 29 剩余；
4. 全量实机测试。
