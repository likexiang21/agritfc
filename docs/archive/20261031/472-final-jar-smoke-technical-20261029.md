# 472 最终 jar 加载 Smoke P0-CN 技术分析

> 日期：2026-10-29
> 目标：用移除 debug 命令后的最终 jar 做一次客户端加载。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

- 复制最终 jar 到版本 mods；
- QuickPlay `tfctest`；
- 等待世界加载；
- 检查注册计数/注册错误/parsing/recipe/debug 命令日志。

## 2. 结果

```text
[TFC Agriculture Plus] registries:
  spiceCrops=15, spiceTrees=5, cropWaste=82, wildMushrooms=15

Starting integrated minecraft server version 1.21.1
Total time to load game and open world was 44.945442 seconds
```

- 无 Registry loading errors；
- 无 `Failed to parse tfcagricultureplus`；
- 无 `Parsing error loading recipe tfcagricultureplus`；
- 无 `tfcplusdebug` 日志/命令。

## 3. 结论

最终 jar 可加载并进入世界；debug 命令已移除。

## 4. 边界

- 只验证加载；
- 未重跑玩法链；
- 之前玩法日志来自功能相同的带 debug jar（仅多测试命令）。
