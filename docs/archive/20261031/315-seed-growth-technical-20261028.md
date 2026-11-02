# 315 种子处理生长效果 P0-N 技术分析

> 日期：2026-10-28
> 目标：让已存在的 `seed_treatment` 组件在种植后产生一次受限的生长推进。
> 约束：不推送；不伪造；不替代 TFC 种植。

## 1. 实现

`SeedTreatmentGrowthHandler`：

- 监听 `PlayerInteractEvent.RightClickBlock`；
- 检查主手种子的 `SEED_TREATMENT`；
- soaked → 1 次、germinated → 2 次、dressed → 3 次；
- 在下一 server task 检查 `clickedPos.relative(face)`；
- 只有目标方块是 `BonemealableBlock` 且 `isValidBonemealTarget` 时才调用 `performBonemeal`；
- 不强制改 age，不绕过作物自身规则。

## 2. 为什么这样接

- TFC/A 作物不一定暴露“种子 → 作物”的内部数据；
- 不替换 TFC 种植；
- 通过标准 `BonemealableBlock` 接口让作物自己决定能否推进；
- 最多 3 次，避免 dressing 变成无限加速。

## 3. 测试

纯 Java：

```text
PASS: 274 crop P0 checks
```

新增：

- soaked/germinated/dressed → 1/2/3 次推进。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 4. 风险/未验证

- 未实机验证；
- 依赖作物实现 `BonemealableBlock`；TFC 作物可能不实现或不接受 bonemeal；
- 服务器 task 时序与方块放置顺序未验证；
- 没有处理失败提示；
- 不保证任意种子都能获得生长效果。
