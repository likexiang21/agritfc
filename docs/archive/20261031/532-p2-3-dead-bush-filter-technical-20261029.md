# 532 P2-3 枯死灌木重复过滤技术分析

> 日期：2026-10-29
> 状态：**静态过滤实现；未实机；有世界生成风险**
> 约束：不实机、不处理视觉、不推送。

## 1. 来源确认

TFC：

```text
configured_feature: tfc:plant/dead_bush
configured_feature: tfc:plant/dead_bush_patch
placed_feature:     tfc:plant/dead_bush
placed_feature:     tfc:plant/dead_bush_patch
```

- `dead_bush` 是 `simple_block`；
- `dead_bush_patch` 是 `random_patch`，引用 `tfc:plant/dead_bush`；
- TFC biome 通过 `#tfc:feature/land_plants` 引用。

A：

```text
block: tfcfarmingplus:plant/dead_cane
```

A 的 `dead_cane` 没有对应 placed feature，主要是作物死亡/环境结果，不是可直接删除的世界生成。

## 2. 实现

新增：

```text
data/tfcagricultureplus/neoforge/biome_modifier/remove_duplicate_dead_bush.json
```

类型：

```json
"type": "neoforge:remove_features"
```

删除：

```text
tfc:plant/dead_bush
tfc:plant/dead_bush_patch
```

目标 biome：

- `#minecraft:is_overworld`
- 125 个 `tfc:*` biome（从 TFC jar 抽取）

## 3. 边界

- 这会把 TFC 自然生成的枯死灌木**全局移除**（主世界）；
- **A 的 dead_cane 仍然存在**，因为它没有可过滤的 placed feature；
- 因此结果从“TFC 枯死灌木 + A 枯死藤蔓”降为“只剩 A 枯死藤蔓”，不是两边都消除；
- 如果用户希望保留 TFC 枯死灌木、只删除 A 的，本方案方向相反，需要回退；
- 未实机验证数据包 schema 和实际 biome 注入。

## 4. 校验

```text
json 6442 / bad 0
final_static_audit problems 0
gradle build BUILD SUCCESSFUL
```

## 5. 未完成

- 实机验证；
- 未验证 `neoforge:remove_features` 对 TFC biome 的 tag 引用是否按预期生效；
- 未处理 A dead_cane；
- 未处理 TFC `dead_berry_bush`（没有对应 placed feature）。
