# 294 作物 P0-A 代码工作报告

> 日期：2026-10-28
> 范围：`291` 作物计划的 P0-A 地基层
> 状态：**初步完成，未推送、未提交远程**
> 后续：P0-B 已接续完成成熟谷物 → bundle + 种子的收获替换，见 [296](296-crop-p0b-work-report-20261028.md)。
> 注意：P0-A 不是完整作物系统；TFC 种植/收获覆盖、102 个 crop_waste、蘑菇 worldgen、坚果叶状态尚未实现。

## 1. 本次完成了什么

### 1.1 数据/代码基础

| 文件 | 内容 |
|---|---|
| `common/crop/CropYieldLedger.java` | 纯 Java 产量账本；约束 seedBack/processed/byproduct/raw |
| `common/crop/GrainCrop.java` | A 10 + TFC 6 = 16 个长秆谷物枚举；bundle ID/谷粒 ID |
| `AgricultureItems.java` | 新增 `WET_GRASS`；新增 `GRAIN_BUNDLES`（16 个物品） |
| `AgricultureDataComponents.java` | 新增 `CROP_ID` String 数据组件 |
| `AgricultureCreativeTab.java` | 创造页加入 `wet_grass` + 16 个 bundle |
| `en_us.json` / `zh_cn.json` | 各新增 17 个语言 key |

### 1.2 资源

- 17 个 item model：
  - `wet_grass` 1 个；
  - `grain_bundle/<crop>` 16 个；
- 临时贴图按要求指向 TFC：
  - `wet_grass` → `tfc:item/straw`；
  - bundle → `tfc:item/stick_bundle`；
- 干燥配方：
  - `data/tfcagricultureplus/recipe/drying/wet_grass.json`；
  - `firmalife:drying`：`wet_grass` → `tfc:straw` 1:1；
- 脱粒配方 16 条：
  - `data/tfcagricultureplus/recipe/crafting/grain_bundle_<crop>.json`；
  - `tfc:advanced_shapeless_crafting` + `tfc:extra_products`；
  - 输入 bundle + `c:tools/knife`；
  - 输出 A/TFC 真实谷粒 + `wet_grass`；
- 堆肥标签：
  - `data/tfc/tags/item/compost_greens/medium.json` 追加 `wet_grass`，`replace=false`。

### 1.3 更新隔离

- 修改前备份到：
  - `mod_rebuild/backups/crop-p0a-20261028/`
- 只追加新代码/新资源；
- 未删除已有物品/方块/注册；
- 未改 A 的源码/资源；
- 未执行 `git push`。

## 2. 验证结果

### 2.1 纯 Java 原型

命令：

```powershell
javac -encoding UTF-8 ... CropYieldLedger.java GrainCrop.java CropYieldProto.java
java ... CropYieldProto
```

实际输出：

```text
PASS: 55 crop P0 checks
```

覆盖：

- 合法账本；
- seedBack=0 拒绝；
- processed>raw 拒绝；
- byproduct=0 拒绝；
- 16 个谷物数量；
- A/TFC 来源拆分；
- bundle path/id；
- 谷粒 ID 非空。

### 2.2 Java 编译

```text
gradle compileJava --console=plain
BUILD SUCCESSFUL
```

### 2.3 资源校验

脚本逐项读取实际文件与 TFC/A jar：

```text
PASS: 17 models, 2 lang files, 17 recipes, all output item models exist
```

校验内容：

- 17 个 model JSON 存在且 `layer0` 与计划一致；
- `tfc:item/straw`、`tfc:item/stick_bundle` 在 TFC jar 里真实存在；
- en_us/zh_cn 的 17 个 key 存在；
- 17 个配方 JSON 可解析；
- 16 个脱粒输出谷粒在 A/TFC jar 的 item model 中真实存在。

### 2.4 资源处理

```text
gradle processResources
BUILD SUCCESSFUL
```

## 3. 必须诚实说明的边界

本轮**没有**完成：

- 任何作物的收获掉落改动；
- TFC 29 的种植/收获/掉落覆盖；
- `crop_waste` 101 条；
- 蘑菇 worldgen / 自然刷新；
- 坚果 `nut_state` 叶状态；
- 实机验证（当前运行环境不完整，未加载客户端测试）。

因此：

- bundle 物品目前只能通过创造页/命令获得，不能从作物收获；
- 17 条配方尚未在游戏中跑过，只通过 JSON/资源/代码编译验证；
- 不能宣称“作物系统已完成”。

## 4. 下一批建议

按 `291`/`292` 顺序：

1. **P0-B**：把 16 个谷物的收获接入 bundle（A 10 + TFC 6）；先做 A 侧，TFC 侧同时准备覆盖；
2. 加入 102 个 `crop_waste` 及实际堆肥标签；
3. 实现 TFC 29 的种植/收获覆盖与存档迁移；
4. 蘑菇 wild block + worldgen + 随机刷新；
5. 已有乔木 `nut_state` 叶状态与坚果随机掉落；
6. 实机验证：物品图标、创造页、干燥配方、脱粒配方。

## 5. 回退方式

- 代码/资源：从 `backups/crop-p0a-20261028/` 恢复修改过的 5 个文件；
- 新增文件：按本报告清单删除；
- 未推送，无需远程回退。
