# 295 作物 P0-B 收获替换技术分析

> 日期：2026-10-28
> 性质：P0-B 代码实现技术分析 + 实测记录
> 目标：把 A 10 + TFC 6 长秆谷物的成熟收获替换为 `grain_bundle + 种子`，为后续脱粒/湿草链提供真实入口。
> 约束：不推送；不伪造指标；不以注释代替实现。

## 1. 需求到代码的映射

P0-B 只做一件事：

```text
成熟谷物方块被破坏
  -> 取消原掉落
  -> 掉落 1 个 grain_bundle/<crop>
  -> 掉落 1 个对应种子
```

后续流程：

```text
grain_bundle/<crop> + 刀
  -> 对应谷粒 + 1 wet_grass
wet_grass -> 干燥 -> tfc:straw
```

## 2. API 评估

### 2.1 为什么用 `BlockEvent.BreakEvent`

- B 不能改 A 的源码/资源；
- TFC 29 要求“替换/覆盖”而不是跳过原流程；
- NeoForge `BlockEvent.BreakEvent` 在方块真正被破坏前触发，可取消，并能在服务端执行受控掉落；
- 该事件在 server level 上处理，不依赖客户端逻辑。

限定条件：

- 只处理 `tfcfarmingplus:crop/<crop>` 与 `tfc:crop/<crop>` 的精确 ID；
- 只处理成熟年龄；
- 只处理单格或双格作物的下半格；
- 其它方块/野生作物/未成熟作物完全不碰。

### 2.2 成熟年龄

从实际 blockstate 读取：

| 来源 | 作物 | maxAge |
|---|---|---:|
| A | millet / foxtail_millet / spelt / emmer / pearl_millet / sorghum / jobs_tears | 5 |
| A | fonio / einkorn / finger_millet | 7 |
| TFC | barley / oat / rice / rye / wheat / maize | 7 |

`GrainCrop.isMature(age)` 用 `age >= maxAge`；不在枚举中的方块直接返回。

### 2.3 双格作物

A/TFC 部分谷物有 `part=bottom/top`：

- `part=top`：不取消、不处理，避免双倍掉落；
- `part=bottom`：取消原事件，移除上方 `part=top`，再移除底部；
- 无 `part` 属性：按单格作物处理。

### 2.4 掉落

- bundle：`AgricultureItems.GRAIN_BUNDLES.get(crop.id())`；
- 种子：`crop.seedItemId()` 通过 `BuiltInRegistries.ITEM` 查找；
- 不使用 A 的 Java 类（B 不编译依赖 A）；
- 取消事件后不会生成原 TFC/A 的直掉谷粒/秸秆，符合“替换而非旁路”。

## 3. 代码结构

| 文件 | 作用 |
|---|---|
| `common/crop/GrainCrop.java` | 16 条记录的 block ID、seed ID、maxAge、bundle ID、谷粒 ID、反查 |
| `common/crop/GrainHarvestHandler.java` | `BlockEvent.BreakEvent` 服务端处理；成熟/双格/掉落 |
| `TFCAgriculturePlus.java` | `NeoForge.EVENT_BUS.addListener(GrainHarvestHandler::onBlockBreak)` |

不新增方块/实体；不修改 A 的类；TFC/A 只通过注册表 ID 访问。

## 4. 原型测试

纯 Java 原型 `CropYieldProto` 扩展了：

- 16 个谷物的 `seedItemId` 非空；
- `cropBlockId` 后缀正确；
- maxAge-1 未成熟、maxAge 成熟；
- `fromCropBlockId` 正查/反查；
- 野生作物/非谷物返回 null。

实测：

```text
PASS: 123 crop P0 checks
```

## 5. 编译/资源检查

```text
gradle compileJava --console=plain
BUILD SUCCESSFUL
```

说明：Gradle 构建成功；PowerShell 仍会因既有 deprecation 警告输出非零退出码，报告不把该警告当作成功指标。

资源校验保持：

```text
PASS: 17 models, 2 lang files, 17 recipes, all output item models exist
```

## 6. 风险与未验证项

| 风险 | 现状 |
|---|---|
| 事件顺序/取消语义 | 编译通过，**未实机**验证 |
| TFC 双格作物顶部破坏 | 按 `part=top` 跳过，**未实机**验证 |
| 取消后方块移除的掉落/音效 | 手动 `removeBlock` + `Block.popResource`，**未实机**验证 |
| 创造模式/工具耐久 | 未特殊处理，按普通破坏处理 |
| 旧存档已种作物 | 通过统一 block ID 处理，不需要迁移数据 |
| 其它作物 | 未处理，保持原行为 |

## 7. 下一批

1. 实机验证 P0-B（需完整运行环境）；
2. 把 bundle 入口扩展到 A 的 10 个谷物后再补 TFC 6 的其它行为；
3. `crop_waste` 101 条；
4. TFC 29 的 blockstate/model 完整覆盖与种子处理；
5. 蘑菇 worldgen；
6. 坚果 `nut_state`。
