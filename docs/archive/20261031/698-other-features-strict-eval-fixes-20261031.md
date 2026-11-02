# 698 其他功能严格符合性评估 P0/P1 修复

> 日期：2026-10-31
> 状态：**代码/数据已修复；静态构建通过；未实机**
> 来源：strict-feature-auditor（其他模组功能严格评估）

## 1. P0：世界生成 biome 过滤与 TFC 世界不匹配

评估证据：3 个 `neoforge:add_features` 的 biome tag 只含
`#minecraft:is_forest` / `is_taiga` / `is_jungle`；TFC 4.2.12 没有向
`data/minecraft/tags/worldgen/biome/*` 注入，TFC 世界的 biome 是 `tfc:*`，因此
15 蘑菇、3 坚果树、5 香料树在 TFC 世界中不会生成。

修复：

- 读取 TFC jar 的 `data/tfc/worldgen/biome/*`；
- 过滤掉 ocean/lake/river/ice_sheet/subglacial，得到 85 个陆生 TFC biome；
- 将 `tfc:<biome>` 显式加入：
  - `wild_mushroom_biomes`
  - `nut_tree_biomes`
  - `spice_tree_biomes`
- 同时保留原 vanilla 标签，兼容非 TFC 世界。

## 2. P1-1：厨房食物展示/水果盘拒绝 TFC/B 食物

原判定：

```java
stack.has(DataComponents.FOOD)
```

TFC 食物不使用 vanilla `DataComponents.FOOD`，改用 TFC 的 `FoodComponent`。
修复为：

```java
FoodCapability.has(stack)
```

`FOOD_DISPLAY` 与 `FRUIT_BOWL` 现在同时接受 TFC、Firmalife、B 食物。

## 3. P1-2：锅铲勺油参数顺序

`FluidUtil.tryFluidTransfer(destination, source, amount, simulate)` 的参数写反：

- 旧：`(handler, pan.oilTank(), ...)` → destination=副手容器、source=空锅；
- 新：`(pan.oilTank(), handler, ...)` → destination=锅、source=副手容器。

## 4. P1-4：语言键斜杠

MC 的翻译键由 `ResourceLocation.toLanguageKey()` 生成，路径分隔符是 `.`，不是 `/`。
B 原 lang 文件有 37 个 block + 9 个 item 的斜杠键。

修复：把 en_us/zh_cn 中所有键的 `/` 替换为 `.`（值不变，1107/1107 键对齐）。

## 5. P1-3：菌包/育苗盘阶段模型

原 blockstate 的 stage 0..3 / 0..2 全部指向同一模型，状态变化客户端不可见。

新增：

- `block/mushroom_bag_stage_1/2/3.json`：在基础袋模型上增加不同大小的菌盖/菌柄；
- `block/nursery_tray_stage_1/2.json`：在托盘土面上增加幼苗几何；
- blockstate 按 stage 指向对应模型。

## 6. 校验

```text
gradle build BUILD SUCCESSFUL
json 6535 / models 3709 / blockstates 539 / item_models 957
lang 1107 / 1107 / missing 0 / extra 0
final_static_audit problems 0
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 7. 仍未完成

- 未实机；
- 香料树/树苗贴图、坚果叶挂果 overlay、14 个 Firmalife 废枝叶图标/中文名仍是 P2；
- 其他 P2：菌包破坏丢进度、锅自动化食材不进入 entries、流体不掉落、部分设备无 BER 等。
