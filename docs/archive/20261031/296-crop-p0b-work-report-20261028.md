# 296 作物 P0-B 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 说明：P0-B 仍不是完整 TFC 覆盖；只完成了成熟谷物收获替换和 bundle 入口。

## 1. 完成内容

### 1.1 收获替换

新增 `GrainHarvestHandler`：

- 监听 `BlockEvent.BreakEvent`；
- 只匹配 A/TFC 的 16 个长秆谷物方块；
- 只处理成熟年龄：
  - A：5 或 7，按实际 blockstate；
  - TFC：7；
- 成熟时：
  - 取消原掉落；
  - 掉 1 个 `grain_bundle/<crop>`；
  - 掉 1 个对应种子；
- 双格作物只在 `part=bottom` 处理，避免双掉；
- 不处理野生作物、未成熟作物、非谷物。

### 1.2 映射补齐

`GrainCrop` 增加：

- `cropBlockId`：A `tfcfarmingplus:crop/*`；TFC `tfc:crop/*`；
- `seedItemId`：A `tfcfarmingplus:seeds/*`；TFC `tfc:seeds/*`；
- `maxAge`；
- `isMature(age)`；
- `fromCropBlockId` 反查。

### 1.3 事件注册

`TFCAgriculturePlus`：

```java
NeoForge.EVENT_BUS.addListener(GrainHarvestHandler::onBlockBreak);
```

不使用资源覆盖绕过；取消原事件后再做受控掉落。

## 2. 验证结果

### 2.1 纯 Java 原型

```text
PASS: 123 crop P0 checks
```

新增检查包括：

- 16 个谷物 seed item 非空；
- crop block ID 正确；
- maxAge-1 未成熟、maxAge 成熟；
- A/TFC 反查；
- 野生作物/非谷物返回 null。

### 2.2 编译

```text
gradle compileJava --console=plain
BUILD SUCCESSFUL
```

### 2.3 资源

```text
PASS: 17 models, 2 lang files, 17 recipes, all output item models exist
```

## 3. 还没有做什么

- 没有实机验证；
- 没有处理 TFC 29 的完整 blockstate/model 覆盖；
- 没有实现 102 个 crop_waste；
- 没有实现蘑菇 worldgen/刷新；
- 没有实现坚果 `nut_state`；
- 没有把 A/TFC 的其它非谷物流程接入六环节。

## 4. 诚实结论

本轮代码已经建立了真实的 `成熟谷物 → bundle + 种子` 入口，而不是只注册物品或写注释。

但：

- 该入口只在代码/编译/纯 Java 策略层验证；
- 未进入游戏验证事件顺序、双格表现、区块移除和物品掉落；
- 不能宣称“TFC 种植/收获已完成”。

## 5. 文件清单

- `mod_rebuild/tfcagricultureplus/src/main/java/.../common/crop/GrainCrop.java`
- `mod_rebuild/tfcagricultureplus/src/main/java/.../common/crop/GrainHarvestHandler.java`
- `mod_rebuild/tfcagricultureplus/src/main/java/.../TFCAgriculturePlus.java`
- `mod_rebuild/docs/295-crop-harvest-p0b-technical-20261028.md`

## 6. 下一批

1. 实机验证 P0-B；
2. `crop_waste` 101 条；
3. TFC 29 的完整种植/收获/掉落覆盖；
4. 蘑菇 worldgen + 自然刷新；
5. 坚果叶状态与随机掉落；
6. 全部通过后再做 159 条逐作物验收。
