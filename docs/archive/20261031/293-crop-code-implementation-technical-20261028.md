# 293 作物代码实现技术分析与 P0 原型

> 日期：2026-10-28
> 性质：**代码实现前技术文档**。先评估现有 API、实现方案、测试原型和更新隔离；本文件完成并验证后才开始改动代码。
> 依据：`291`、`292`、`287–290`、`AGENTS.md`。
> 本轮约束：**不推送**；不伪造指标；贴图路径暂时指向 TFC。

## 1. 本轮代码范围（P0-A）

先做可独立验证的地基，不一次性铺 159 条作物：

1. `tfcagricultureplus:wet_grass` —— B 新物品，不是 TFC 物品；
2. 16 个 `grain_bundle/<crop>` 物品（A 10 + TFC 6）；
3. 作物产量账本 `CropYieldLedger`（纯 Java，可单测）；
4. 谷物枚举 `GrainCrop`（16 条，含 A/TFC 来源、谷粒 ID、bundle ID）；
5. 临时贴图路径：bundle → `tfc:item/stick_bundle`，wet grass → `tfc:item/straw`；
6. 干燥配方原型：`wet_grass` → `tfc:straw`（Firmalife `drying`）；
7. 脱粒配方：16 条 `grain_bundle/<crop>` + 刀 → 对应谷粒 + `wet_grass`；
8. 纯 Java 原型测试：验证 `seedBack >= 1`、`processed <= raw`、`processed/byproduct >= 1`；
9. 编译与资源检查。

**不在本轮**：TFC 29 的完整种植/收获覆盖、102 个 `crop_waste`、蘑菇 worldgen、坚果叶状态。这些在 P0-B/P1 继续，不能声称已完成。

## 2. 现有代码/注册顺序评估

`TFCAgriculturePlus` 当前注册顺序：

```text
Blocks -> Items -> Plates -> Bowls -> Spatulas -> Sounds -> FoodTraits
-> DataComponents -> BlockEntities -> Menus -> CreativeTab
-> RecipeSerializers -> RecipeTypes
```

新增物品必须加在 `AgricultureItems`，不能单独建 register；创造页在 `AgricultureCreativeTab.MAIN` 中显式加入；语言在 `en_us.json`（B 的资源）。

### 2.1 物品注册方式

现有 `AgricultureItems` 使用：

```java
public static final DeferredRegister.Items ITEMS =
    DeferredRegister.createItems(TFCAgriculturePlus.MOD_ID);

public static final DeferredHolder<Item, Item> X =
    ITEMS.registerSimpleItem("path", materialProps());
```

结论：沿用 `registerSimpleItem` + `Map<String, DeferredHolder<Item, Item>>`；不要另造注册器。

### 2.2 DataComponent

现有 `AgricultureDataComponentsDISH` 使用：

```java
DataComponentType.<CompoundTag>builder()
    .persistent(CompoundTag.CODEC)
    .networkSynchronized(ByteBufCodecs.COMPOUND_TAG)
    .build();
```

本轮新增 `CROP_ID` 用 `Codec.STRING` + `ByteBufCodecs.STRING_UTF8`；它服务于后续 `crop_waste`、种子处理、bundle 来源，避免 43/102 个重复组件类型。

### 2.3 配方

- 干燥：Firmalife `firmalife:drying`，现有 `DryingRackBlockEntity` 直接查 `DryingRecipe`；已实测配方格式：
  ```json
  {"type":"firmalife:drying","ingredient":{"item":"..."},
   "result":{"count":1,"id":"..."}}
  ```
- 脱粒：TFC `tfc:advanced_shapeless_crafting` + `tfc:extra_products` 是 TFC 原生机制；P0-A 已落 16 条，输出分别指向 A/TFC 的真实谷粒物品；

### 2.4 临时贴图

已实测 TFC jar 内有：

- `assets/tfc/textures/item/stick_bundle.png`
- `assets/tfc/textures/item/straw.png`

本轮模型 `layer0` 指向：

```text
grain_bundle/* -> tfc:item/stick_bundle
wet_grass       -> tfc:item/straw
```

后续补图时只改 `layer0`，不改注册/ID。

## 3. 作物产量账本（评估函数）

纯 Java，不依赖 Minecraft，便于原型测试：

```java
public record CropYieldLedger(String crop, int raw, int seedBack, int processed, int byproduct) {
    public boolean isValid() {
        return seedBack >= 1
            && processed >= 1
            && byproduct >= 1
            && processed <= raw
            && raw > 0;
    }

    public int netEdible() { return processed; }
    public int totalUseful() { return processed + byproduct; }
}
```

**为什么先做这个**：产量平衡是后续所有配方/掉落/世界生成调参的基准；如果先堆物品，后面无法统一验收。

`GrainCrop` 映射：

| 字段 | 示例 | 用途 |
|---|---|---|
| `id` | `millet` | 物品路径/配方 |
| `source` | `A` / `TFC` | 掉落表/来源 |
| `grainItem` | `tfcfarmingplus:food/millet` | 脱粒输出 |
| `bundleId` | `tfcagricultureplus:grain_bundle/millet` | 收获中间物 |

## 4. 原型测试

### 4.1 纯 Java 测试

`docs/audit/prototype/io/github/likexiang21/tfcplus/agriculture/common/crop/CropYieldProto.java`：
- 合法账本通过；
- `seedBack=0` 拒绝；
- `processed>raw` 拒绝；
- `byproduct=0` 拒绝；
- 16 个 `GrainCrop` 均有 bundle/grain 映射。

运行：

```powershell
javac -encoding UTF-8 docs/audit/prototype/CropYieldProto.java
java -cp docs/audit/prototype CropYieldProto
```

预期输出明确的 `PASS` 行；失败返回非 0，不能只看日志有无报错。

### 4.2 编译测试

```powershell
cd mod_rebuild/tfcagricultureplus
gradle compileJava --console=plain
```

同时检查：

- 所有新模型 JSON 可解析；
- `layer0` 指向的 TFC 贴图在 jar 内存在；
- lang key 与物品 ID 一一对应；
- 不改已有物品注册顺序。

## 5. 更新隔离

在改动前记录：

- `git status --short` 当前未提交文件清单；
- 对将修改的 `AgricultureItems.java`、`AgricultureCreativeTab.java`、`AgricultureDataComponents.java`、`en_us.json` 做文件级备份到 `mod_rebuild/backups/crop-p0a-20261028/`；
- 新增文件只放 `src/main/java/.../common/crop/` 和对应资源，不删除已有代码；
- 不使用 `gradle clean`（避免误删生成物），除非明确需要；本轮只 `compileJava`；
- 不修改 A 的源码/资源；B 只引用 A/TFC 的 ID。

## 6. 风险与回退

| 风险 | 处理 |
|---|---|
| `Item.Properties` / DataComponent API 版本差异 | 以现有 `AgricultureDataComponents` 编译通过版本为准；先小改再编译 |
| 模型指向 TFC 贴图不存在 | 已实测 2 个路径存在；编译后检查资源引用 |
| 配方格式错误 | 只先加 1 条原型，JSON 解析通过后再批量 |
| 注册顺序导致 creative tab 失败 | 新物品只在 `AgricultureItems` 静态初始化；creative tab 只 accept 已有 holder |
| 破坏既有物品 | 先备份；只追加，不删/不改已有字段 |
| 误报成功 | 原型测试 + `compileJava` 输出 + 逐项资源核对，不以注释/日志代替 |

## 8. P0-A 实施结果（2026-10-28）

### 8.1 实际落地

| 项 | 文件/结果 |
|---|---|
| 产量账本 | `common/crop/CropYieldLedger.java` |
| 16 谷物映射 | `common/crop/GrainCrop.java` |
| 物品注册 | `AgricultureItems` 增加 `WET_GRASS` + `GRAIN_BUNDLES`（16） |
| 数据组件 | `AgricultureDataComponents.CROP_ID`（String） |
| 创造页 | `AgricultureCreativeTab` 加入 1 + 16 个物品 |
| 资源 | 17 个 item model；en_us/zh_cn 各 17 个 key |
| 配方 | `drying/wet_grass.json` + 16 条 `crafting/grain_bundle_<crop>.json` |
| 标签 | `data/tfc/tags/item/compost_greens/medium.json` 追加 `wet_grass` |
| 备份 | `mod_rebuild/backups/crop-p0a-20261028/` |

### 8.2 实测结果

```text
纯 Java 原型：PASS: 55 crop P0 checks
gradle compileJava：BUILD SUCCESSFUL
资源校验：PASS: 17 models, 2 lang files, 17 recipes, all output item models exist
gradle processResources：BUILD SUCCESSFUL
```

### 8.3 诚实边界

- `wet_grass`、bundle 物品已注册，但**还没有接作物收获掉落**；
- 16 条脱粒配方是**数据原型**，尚未实机验证（当前无可用 `.tooling` 运行环境）；
- TFC 29 的种植/收获覆盖、102 个 crop_waste、蘑菇 worldgen、坚果叶状态**未开始**；
- 模型贴图全部指向 TFC 临时路径，补图时只改 `layer0`；
- 没有推送、没有提交远程。

## 9. 下一步（P0-B，不在本轮完成）

1. 16 条 bundle 脱粒配方全部落地；
2. `crop_waste` 101 条（逐作物物品 + 堆肥标签）；
3. TFC 29 种植/收获覆盖；
4. 蘑菇 worldgen/刷新；
5. 坚果 `nut_state` 叶状态与随机掉落；
6. 实机验证（当前 `.tooling` 缺失时明确标注未实机）。
