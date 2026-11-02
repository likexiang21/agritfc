# 510 开放问题深度审查与检讨 P0-DH 技术分析

> 日期：2026-10-29
> 范围：用户提出的 11 个问题 + 本轮日志/截图
> 约束：**不做实机、不处理视觉**；只做静态查找、根因分析和修复方案设计。
> 规则：不伪造已修复项。

## 1. 审查方法

- 读取 B 源码/资源；
- 读取 TFC/A 客户端 jar 的配方/语言/模型；
- 用脚本扫描：
  - `find_knapping_collisions.py`
  - `static_audit.py`
  - `final_static_audit.py`
  - 资源/配方/语言引用检查；
- 对照用户截图和 18:33–18:49 客户端日志。

## 2. 关键发现

### 2.1 陶盘 knapping 与 TFC 陶碗完全相同（用户更正后确认）

B：

```json
{
  "type": "tfc:knapping",
  "knapping_type": "tfc:clay",
  "pattern": ["#   #", " ### ", "     ", "#   #", " ### "],
  "result": { "count": 1, "id": "tfcagricultureplus:ceramic/unfired_plate" }
}
```

TFC `unfired_bowl.json`：

```json
{
  "type": "tfc:knapping",
  "knapping_type": "tfc:clay",
  "pattern": ["#   #", " ### ", "     ", "#   #", " ### "],
  "result": { "count": 4, "id": "tfc:ceramic/unfired_bowl" }
}
```

- 同一 `tfc:clay`；
- 同一 pattern；
- 输出不同；
- 这是 **确定性配方冲突**，不是单纯“流程不一致”。

另外：
- `find_knapping_collisions.py` 发现 B 的 **7 个 pestle** 共用同一 `tfc:rock` pattern；
- 但每个 pestle 有不同的 `ingredient`（granite/diorite/...），TFC 自有重复 pattern 也靠 ingredient 区分；
- pestle 是否真正按 ingredient 消歧，需按 TFC `KnappingRecipe.matches` 验证；已记录 OPEN-013。

### 2.2 厨房家具同质化

`KitchenStorageBlock`：

- 6 个 `StorageKind`；
- 共用：
  - `KitchenStorageBlockEntity`
  - `KitchenStorageMenu`
  - `KitchenStorageScreen`
- 仅 `height` 不同；
- 无独立槽位规则、功能或自动化。

### 2.3 工作方块无配方，家具只有木板占位

- `cutting_board`、`knife_block`、`mortar`、`drying_rack`、`cooking_pan`、`lumber_pile`、`silkworm_rack`、`log_pile` 未找到产物配方；
- `recipe/kitchen/` 共 6 × 34 = **204 个配方**，全部为简单木板 pattern。

### 2.4 名称不可读

- `crop_waste` 82 个 item model；
- 全部 `layer0 = tfc:item/straw`；
- 名称模式：
  ```text
  作物废枝叶（spinach）
  谷物捆（millet）
  香料（basil）
  坚果（pistachio）
  ```
- 原始 ID 直接暴露；
- 无逐物种中文名。

### 2.5 重复碗

TFC 已有：
- `block.tfc.wooden_bowl`
- `item.tfc.ceramic.bowl`

B 又添加：
- `tfcagricultureplus:bowl/wood`
- `tfcagricultureplus:bowl/ceramic`

且陶瓷碗配方只是：
```json
ingredients: [{"item":"tfc:ceramic/bowl"}]
result: tfcagricultureplus:bowl/ceramic
```

### 2.6 金属罐

- `MetalCanItem extends FluidContainerItem`；
- 容量 500 mB；
- 但 item model 只有：
  ```json
  {"parent":"item/generated","textures":{"layer0":"tfc:item/metal/sheet/copper"}}
  ```
- 无：
  - fluid 模型层；
  - item property 显示液体；
  - 与 TFC 陶罐一致的 overlay/交互层。

### 2.7 育种流程

- 代码只有统一育苗门 + `nursery_tray` + `seedling` + `SEED_TREATMENT`；
- 291 计划的物种级繁殖方式（种子/分株/匍匐茎/冠芽/种薯/种球/扦插）未逐项实现；
- 因此用户说“胡写、无视技术文档”有静态依据。

### 2.8 Patchouli 手册（修正上一版错误结论）

**上一版 OPEN-008 写“B 没有 Patchouli 资源”是错误的。**

实际存在：

```text
assets/tfc/patchouli_books/field_guide/{en_us,zh_cn}/
  categories/agriculture_plus_kitchen.json
  categories/agriculture_plus_silkworm.json
  categories/agriculture_plus_woodwork.json
  entries/.../intro.json
```

但只有 3 个旧主题：厨房、养蚕、木工。

### 2.9 JEI

B 只有 3 个 category：
- `mortar`
- `cutting_board`
- `in_world`

未覆盖：
- 陶器；
- 锅/烤箱/搅拌碗；
- 金属罐；
- 木工；
- 育苗/菌包/树木；
- 多数 A/TFC 联动。

### 2.10 木工

- `TimberBlocks` / `TimberPieceBlock` / `LumberPileBlock` 存在；
- 静态配方数量很大，但未与 TFC/A 原木工逐项对照；
- 不能声称“尊重原作”。

## 3. 根因检讨

### 3.1 用“存在性”冒充“功能性”

我的 validator 检查的是：
- 文件存在；
- 注册数量；
- 形状/引用存在；
- 393 项纯数据断言。

它没有检查：
- 配方是否唯一；
- 两种物品是否重复；
- 工作方块是否可以合成；
- 家具是否有独立功能；
- 玩家是否能从名称/手册/JEI 理解；
- 放进游戏后是否真的“能用”。

这是最根本的错误：**把“编译/资源通过”当成“功能完成”。**

### 3.2 大批量生成/占位违背用户明确要求

用户多次说：
- 不要批量生成低质量贴图；
- 不要占位；
- 要可读、可理解；
- 要参考 TFC/A 原内容。

我仍然产出了：
- 82 个共用一张 `tfc:item/straw` 的 crop_waste；
- 204 个木板占位厨房配方；
- `作物废枝叶（ID）` 式名称；
- 3 个旧主题、无作物章节的手册。

这是**行为上的重复犯错**，不是单点 bug。

### 3.3 未做上游内容对照

添加碗/陶盘前没有查：
- TFC 已有 `wooden_bowl` / `ceramic.bowl`；
- TFC 陶碗 knapping pattern 是什么；
- TFC 陶罐流程是什么。

于是：
- 碗重复；
- 陶盘 pattern 与碗冲突；
- 违反“参考陶罐合成流程”。

### 3.4 未做配方语义验证

没有检查：
- 同 `knapping_type + pattern` 是否冲突；
- 同一物品是否有多个来源；
- 工作方块是否有产出配方；
- 家具配方是否真的需要该家具。

### 3.5 未按 291 技术文档逐项实现

育种被简化成统一育苗门；
291 的逐物种繁殖方式没有落地；
这不是“实现不完整”，而是**没有按规格施工**。

### 3.6 过早宣布完成

我在 100 轮里多次给出“主机制完成/验证通过”，但用户实际一打开创造页就发现：
- 名称不可读；
- 家具同质；
- 工作方块不可合成；
- 陶盘冲突；
- 手册无作物内容。

说明我的验收标准与用户标准严重脱节。

## 4. 修复方案（本轮不执行，先定方案）

### P0

1. **陶盘 knapping 改唯一 pattern**
   - 保留 clay knapping + firing；
   - 新 pattern 必须通过全量碰撞扫描（B + TFC + A）；
   - 建议 5×5 浅盘形状，不复用 bowl/jug pattern。
2. **删除 B 重复碗**
   - 删除 `bowl/wood`、`bowl/ceramic` 物品/配方；
   - 全部引用改 TFC 原碗；
   - 旧存档迁移/别名策略单独设计。
3. **工作方块配方**
   - 每种工作方块补至少一条 TFC 风格的真实配方；
   - 逐项验证可合成。
4. **名称/贴图**
   - 逐物种人工中文名，禁止 `（ID）`；
   - 贴图不能全部共用 `tfc:item/straw`；
   - 至少区分叶/茎/豆/果类别。

### P1

5. **金属罐**
   - 增加流体 item property/模型层；
   - 对照 TFC 陶罐的 rendering/交互。
6. **家具功能分化**
   - 至少区分：储物、展示、水槽、香料架；
   - 不能 6 个共用同一 inventory menu。
7. **Patchouli**
   - 新增 crop/spice/nut/mushroom/nursery/bag 章节；
   - 用 recipe pages 替代纯文本墙。
8. **JEI**
   - 覆盖全部工作方块/加工链；
   - 添加信息页/用途页。

### P2

9. **育种**
   - 按 291 表格逐物种实现或明确缩减范围。
10. **木工**
    - 与 TFC/A 原木工逐项对照，删除重复/错误内容。
11. **枯死灌木**
    - 只在确认归属后过滤 A/TFC 的重复世界生成；B 不新增枯死方块。

## 5. 结论

用户 11 个问题的核心不是“少了几个配方”，而是：

**我错误地把批量占位资源、注册数量、静态校验通过，当作功能完成；没有按用户标准做可用性验收。**

本轮只完成静态查找、归因和修复方案设计，未修改代码。
