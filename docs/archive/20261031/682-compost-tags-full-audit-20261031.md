# 682 全盘检查：废枝叶/湿草未接入 TFC 堆肥标签

> 日期：2026-10-31
> 状态：**数据已修复；静态构建通过；未实机**

## 1. 发现

文档 291 §4.1.1/§4.1.2 明确要求：

- `wet_grass` → 绿色堆肥；
- 82 种 `crop_waste/<crop>` 按 high/medium/low 进入 `tfc:compost_greens/*`；
- 灌木废枝、坚果壳也应有副产物出口。

实际数据中：

```text
crop_waste/*  → 只被 NutShellFuelHandler 当 100 tick 燃料
bush_waste/*  → 只由灌木采收掉落，无任何配方/标签引用
wet_grass     → 只参与 grain_bundle 与干燥配方，未进堆肥标签
nut_shell/*   → 只由树叶掉落，无堆肥/燃料以外的用途
```

TFC 的堆肥桶只识别：

```java
TFCTags.Items.COMPOST_GREENS_HIGH/MEDIUM/LOW
TFCTags.Items.COMPOST_BROWNS_HIGH/MEDIUM/LOW
```

因此这些新副产物虽然能掉落，却**不能按预期进入堆肥链**。

## 2. 修复

基于 TFC 原始标签文件追加 B 条目（保留原 values，不覆盖）：

- `compost_greens/high`：36 个高氮废枝叶 + `wet_grass`；
- `compost_greens/medium`：43 个中氮废枝叶 + 10 个 `bush_waste`；
- `compost_greens/low`：3 个低氮废枝叶；
- `compost_browns/high`：8 个 `nut_shell/*`。

结果数量：

```text
greens/high 41 values
greens/medium 54 values
greens/low 153 values
browns/high 13 values
```

分类来自文档 291 §4.1.2 的逐作物 high/medium/low 表，不是猜测。

## 3. 校验

```text
B tag missing refs 0
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,928,335 bytes
SHA-256 31BDD86A58F94499A25DBBBC9F59DD1064A4C0901C659459A025C2BDF19F7EED
```

## 4. 未完成

- 未实机验证堆肥桶实际接受；
- 未添加饲料/青贮等其它副产物出口。
