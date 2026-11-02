# 410 实机加载验证 P0-BI 技术分析

> 日期：2026-10-29
> 目标：在真实客户端中加载 B，验证注册表/资源/世界生成是否真的能进入世界。
> 约束：不推送；不伪造；测试后恢复游戏原 jar/options。

## 1. 启动方式

使用已有 `.minecraft` 运行时：

- Java：`C:\Users\Lenovo\AppData\Roaming\.minecraft\runtime\java-runtime-delta`
- libraries：`D:\111\最强服务器\.minecraft\libraries`
- 版本：`Essential TerraFirmaCraft (TFC)`
- 存档：`tfctest`
- 启动脚本：`mod_rebuild/tools/launch-runtime.ps1`

## 2. 运行时发现并修复的问题

### 2.1 AFC 依赖版本

B 模板要求 `afc >= 2.1.3`，但实际 jar 文件名是 2.1.3、内部 metadata 是 **2.1.2-1.21**，导致：

```text
Mod tfcagricultureplus requires afc 2.1.3 or above
Currently, afc is 2.1.2-1.21
```

修复：`neoforge.mods.toml` 依赖改为 `[2.1.2,)`。

### 2.2 placed_feature count codec

```json
"count": {"type":"minecraft:uniform","min":1,"max":2}
```

1.21.1 需要：

```json
"count": {"type":"minecraft:uniform","min_inclusive":1,"max_inclusive":2}
```

修复 23 个 placed feature（15 蘑菇 + 3 坚果 + 5 香料树）。

### 2.3 would_survive predicate

`minecraft:would_survive` 必须带 `state`：

```json
{"type":"minecraft:would_survive","state":{"Name":"...sapling...","Properties":{"stage":"0"}}}
```

修复 23 个 placed feature；`star_anise` 的 state 还修正为 `spice_sapling/star_anise`。

### 2.4 16 个谷物捆配方 result

`result` 误写为：

```json
{"stack":{"count":1,"id":"..."}}
```

实际需要：

```json
{"id":"...","count":1}
```

修复 16 个 `grain_bundle_*`。

### 2.5 serving_plate blockstate

原 variant keys 写成 `wood`、`ceramic_*`，实际属性为 `variant`；修复为 `variant=wood` 等。

### 2.6 wild_mushroom_biomes 缺失 tag

移除不存在的 `#minecraft:is_swamp`，保留 forest/taiga。

## 3. 最终结果

最终启动日志：

```text
Starting integrated minecraft server version 1.21.1
Total time to load game and open world was 64.18618 seconds
```

- 无 Registry loading errors；
- 无 B 的 recipe parse error；
- 进入世界成功；
- B 的 JEI 插件注册日志出现。

剩余 warning 来自 KubeJS 的既有 `plant_fiber_rope` recipe，与 B 无关。

日志证据：

```text
mod_rebuild/docs/audit/runtime-validation-20261029.log
```

## 4. 边界

- 只验证了**加载/进入世界**；
- 没有逐作物实机种植/收获；
- 没有树苗/菌包/菌包 UI 实机操作；
- 测试后已恢复游戏原 B jar 与 options；
- 不能宣称玩法验收完成。
