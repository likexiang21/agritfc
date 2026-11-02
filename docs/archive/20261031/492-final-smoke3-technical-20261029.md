# 492 最终 jar 三次 Smoke（P0-CV 后）P0-CX 技术分析

> 日期：2026-10-29
> 目标：确认 TFC 直接播种修复后的最终 jar 仍可加载。
> 约束：不推送；不伪造。

## 1. 结果

```text
spiceCrops=15, spiceTrees=5, cropWaste=82, wildMushrooms=15
Starting integrated minecraft server version 1.21.1
Total time to load game and open world was 42.923435 seconds
```

无 Registry/Recipe/B parse 错误；无 debug 命令。

## 2. 结论

P0-CV 修改未破坏加载；最终 jar 可进入世界。

## 3. 边界

- 仅加载 smoke；
- 未重跑全部玩法；
- 自然生成/全量验收/视觉/平衡仍未完成。
