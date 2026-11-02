# 482 最终 jar 二次 Smoke 与验收矩阵更新 P0-CS 技术分析

> 日期：2026-10-29
> 目标：用最新最终 jar 再加载一次，并把新证据并入验收矩阵。
> 约束：不推送；不伪造。

## 1. 最终 jar smoke

```text
spiceCrops=15, spiceTrees=5, cropWaste=82, wildMushrooms=15
Starting integrated minecraft server version 1.21.1
Total time to load game and open world was 42.55842 seconds
```

无 Registry/Recipe/B parse 错误，无 debug 命令。

## 2. 矩阵新增证据

- 玩家破坏收获；
- 收获掉落物 ID；
- 未成熟不掉落修复；
- 菌包采集；
- 育苗盘产出；
- seedling 移栽；
- 3 个蘑菇 feature 执行；
- 旧存档 smoke。

## 3. 仍未完成

- 自然世界生成（非 /place）；
- 移栽后完整生长→收获；
- 树叶衰减方块状态；
- 全量 159 行验收；
- 视觉/平衡；
- 长时间稳定性。
