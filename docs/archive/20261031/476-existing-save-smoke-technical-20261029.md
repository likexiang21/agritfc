# 476 现有存档兼容 Smoke P0-CP 技术分析

> 日期：2026-10-29
> 目标：用最终 jar 加载已有 `tfctest` 存档，确认现有存档不会因新增注册/资源而失败。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

- 最终 jar（无 debug 命令）；
- QuickPlay `tfctest`（旧存档）；
- 检查注册计数、Registry/Recipe 错误。

## 2. 结果

```text
spiceCrops=15, spiceTrees=5, cropWaste=82, wildMushrooms=15
Starting integrated minecraft server version 1.21.1
Total time to load game and open world was 44.945442 seconds
```

- 无 Registry loading errors；
- 无 B recipe parse error；
- 无 debug 命令。

## 3. 结论

旧存档可在最终 jar 下加载并进入世界；这是**兼容 smoke**，不是完整存档内容回归测试。

## 4. 未确认

- 旧存档内已放置作物/树/菌包的逐项行为；
- 存档内旧 B 方块 ID 迁移；
- 长时间游玩稳定性。
