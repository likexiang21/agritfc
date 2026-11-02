# 411 实机加载验证 P0-BI 工作报告

> 日期：2026-10-29
> 状态：**实机加载成功；未推送、未提交远程**
> 范围：真实客户端加载 + 进入 tfctest；未做逐玩法测试。

## 1. 完成内容

- 使用真实 `.minecraft` 运行时启动；
- 修复 5 类运行时问题：
  1. AFC 依赖范围 2.1.3 → 2.1.2；
  2. placed_feature count codec；
  3. `would_survive` state；
  4. 16 个谷物捆 recipe result；
  5. serving_plate blockstate variant；
  6. wild_mushroom_biomes 缺失 swamp tag（附）。
- 最终成功进入世界。

## 2. 证据

```text
Starting integrated minecraft server version 1.21.1
Total time to load game and open world was 64.18618 seconds
```

- 无 Registry loading errors；
- 无 B recipe parse error；
- B JEI 插件注册日志出现；
- 日志：`mod_rebuild/docs/audit/runtime-validation-20261029.log`。

## 3. 环境恢复

测试后：

- 恢复原 B jar；
- 恢复 `options.txt`；
- 停止测试客户端。

## 4. 边界

- **不是玩法验收**；
- 没有逐作物种植/收获；
- 没有树苗/菌包操作；
- 没有旧存档兼容测试；
- 仍有 KubeJS 既有 recipe warning（与 B 无关）；
- 不能宣称目标完成。

## 5. 下一批

1. 实机逐作物；
2. 树苗/菌包/育苗盘；
3. 旧存档兼容；
4. 全量验收。
