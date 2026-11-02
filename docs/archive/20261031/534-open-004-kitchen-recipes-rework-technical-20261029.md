# 534 P2-4/OPEN-004 厨房家具配方重做技术分析

> 日期：2026-10-29
> 状态：**配方静态重做完成；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

旧配方：

- 6 类 × 34 木材 = 204 条；
- 全部是 `"PPP","PPP","   "` 木板占位；
- `food_display` 与 `sink_cabinet` 配方结构完全相同，存在真实冲突。

## 2. 新配方

全部改为 TFC/AFC 的真实木材中间物：

| 家具 | 图案 | 材料 |
|---|---|---:|
| counter_cabinet | `LLL / L L / LLL` | 8 lumber |
| half_cabinet | `LLL / L L` | 5 lumber |
| sink_cabinet | `LLL / LML / LLL` | 8 lumber + 1 wrought iron sheet |
| spice_rack | `LLL / R R` | 3 lumber + 2 rods |
| food_display | `LLL / LGL / LLL` | 8 lumber + 1 glass |
| fruit_bowl | `L L / LLL` | 5 lumber |

其中：

- `L` = 对应木材的 `tfc:wood/lumber/<wood>` 或 `afc:wood/lumber/<wood>`；
- `R` = `#c:rods/wooden`；
- `M` = `tfc:metal/sheet/wrought_iron`；
- `G` = `minecraft:glass`。

## 3. 冲突检查

`check_shaped_collisions.py`：

```text
total shaped recipes 347
groups 347
```

即 B 本地所有 shaped 配方**没有重复的 pattern+key 组**；旧的 `food_display` / `sink_cabinet` 冲突已消失。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
json 6442 / bad 0
final_static_audit problems 0
shaped groups 347 / 347
```

## 5. 未完成

- 未实机验证配方；
- 家具方块掉落表已复核存在（204 个，见 docs/540/541），仍需实机验证；
- 家具功能仍是 P1-2 的“部分过滤/堆叠”状态；
- 未处理视觉效果。
