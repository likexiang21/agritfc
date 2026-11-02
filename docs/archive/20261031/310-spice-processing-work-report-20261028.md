# 310 香料初加工 P0-K 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：20 种香料的产物 → 香料粉研磨链；形态与实机验证未完成。

## 1. 完成内容

### 1.1 物品

新增 20 个：

```text
tfcagricultureplus:ground_spice/<spice>
```

### 1.2 配方

20 条石臼配方：

```text
spice/<spice> -> ground_spice/<spice>
grind_time = 4
```

### 1.3 资源

- 20 个 item model；
- en_us/zh_cn 各 20 个 ground_spice key；
- 创造页加入全部 20 个；
- 临时贴图 `tfc:item/straw`。

## 2. 验证

### 纯 Java

```text
PASS: 265 crop P0 checks
```

新增 20 个 `groundPath` 校验。

### 编译

```text
gradle compileJava
BUILD SUCCESSFUL
```

### 资源

```text
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, 20 ground spices, tags valid
```

`processResources`：

```text
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机验证**石臼配方加载和研磨；
- 香料粉暂无食物/烹饪效果；
- 香料树/藤/球茎形态未实现；
- 没有完整采种/育苗/移栽链；
- 贴图仍为 TFC 临时资源；
- 不能宣称 B 香料完成。

## 4. 下一批

1. 香料形态；
2. 香料粉烹饪；
3. TFC 29 剩余覆盖；
4. 全量实机测试。
