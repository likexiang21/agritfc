# 686 全盘检查：20 种香料废枝叶未接入堆肥

> 日期：2026-10-31
> 状态：**数据已修复；静态构建通过；未实机**

## 1. 发现

`AgricultureSpices.WASTES` 为 20 个香料物种注册了：

```text
tfcagricultureplus:spice_waste/<spice>
```

但 `data/tfcagricultureplus` 中没有任何配方、标签或堆肥引用；这些废枝叶只能掉落，**不能进入 TFC 堆肥链**。

## 2. 修复

按形态分类追加到 TFC 原始标签：

- `herb`（9 种：basil/cilantro/cumin/oregano/thyme/sage/dill/fennel/mustard）→ `tfc:compost_greens/high`；
- 其余 11 种（shrub/root/tree/vine/corm）→ `tfc:compost_greens/medium`。

结果：

```text
compost_greens/high 50 values
compost_greens/medium 65 values
```

仍然保留 TFC 原始 values。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,937,590 bytes
SHA-256 77D4BDA06C3C54BB4ED33EC6BDBE9F12D8A2CEB183D25C64A6D94B956422E623
```

## 4. 未完成

- 未实机验证堆肥桶；
- 香料其它加工/饲料出口仍不完整。
