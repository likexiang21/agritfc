# 508 全量静态审查与修复 P0-DG 技术分析

> 日期：2026-10-29
> 范围：**不做实机验证**；只做资源/代码/构建静态审查与修复。
> 约束：不推送；不伪造。

## 1. 审查范围

- 6254 个 JSON 解析；
- 3670 个 model；
- 539 个 blockstate；
- 924 个 item model；
- 2 个语言文件；
- 配方、战利品表、worldgen、tags、模型父子/贴图引用；
- 136 个 Java 源文件静态标记；
- jar 内容/调试字符串。

## 2. 发现并修复

### 2.1 16 个方块缺语言键

缺失：

- `serving_plate`；
- 15 个 `spice_crop/*`。

修复：en_us/zh_cn 各补 16 键，语言键数均 1047 → **1063**。

### 2.2 空语言值

`gui.tfcagricultureplus.silkworm_container` 原为空字符串。

修复：

- en: `Silkworm Container`
- zh: `养蚕容器`

### 2.3 创造页占位图标

`AgricultureCreativeTab` 原用原版面包作为图标，并有 TODO。

修复：

```java
.icon(() -> new ItemStack(AgricultureItems.WET_GRASS.get()))
```

TODO 已清除。

### 2.4 mod 元数据描述过期

`neoforge.mods.toml` 仍描述“cooking utensils/moulds…” 。

修复：改为作物/香料/坚果/蘑菇生产层，明确 102 crop-waste、10 bush-waste、15 蘑菇、20 香料、3 坚果、TFC/A/AFC 叶状态。

## 3. 审查结果

| 检查 | 结果 |
|---|---|
| JSON 解析 | 6254 / 0 错 |
| 重复 JSON key | 0 |
| lang 对齐 | 1063/1063，0 缺/0 多 |
| 方块/物品语言键 | 0 缺 |
| 模型 parent | 0 缺 |
| 模型贴图 B 引用 | 0 缺 |
| 配方引用 | 0 缺 |
| 战利品表 block/item | 0 缺 |
| worldgen configured/placed | 0 缺 |
| tags B 引用 | 0 缺 |
| TFC 叶覆盖 nut_state | 20/20 全 4 态 |
| AFC 叶覆盖 nut_state | 59/59 全 4 态 |
| crop loot age=7 条件 | 16/16 |
| Java TODO/FIXME/debug | 0 |
| 零字节资源 | 0 |

## 4. 构建

```text
gradle build BUILD SUCCESSFUL
validate_crop_p0a.py 全 PASS
CropYieldProto PASS: 393 checks
jar 2,746,323 bytes
SHA-256 730EC7C26625C35A7A99DA82E8C9AAB0FB2BD9EDC0481F5B89014F547BAB31AF
debug_bytes = False
```

## 5. 未覆盖

- 实机逐物种；
- 自然群系生成；
- 视觉/平衡；
- 长时间稳定性。
