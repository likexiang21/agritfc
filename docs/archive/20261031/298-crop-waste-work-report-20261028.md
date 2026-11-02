# 298 作物废枝叶 P0-C 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：82 条 A/TFC 实际 crop_waste；B 香料 20 条暂未注册。

## 1. 完成内容

### 1.1 物品

新增 `AgricultureItems.CROP_WASTE`：

```text
tfcagricultureplus:crop_waste/<crop>
```

共 82 条，来自 `291 §4.1.2` 实际有废枝叶的 A/TFC 作物。

不包含：

- 谷物 → bundle/wet_grass；
- 油料 → cake/stalk；
- 纤维 → shives；
- 坚果 → shell；
- 蘑菇 → spent substrate。

### 1.2 收获行为

新增 `CropWasteHandler`：

- 监听 `BlockEvent.BreakEvent`；
- 只处理 82 个精确作物方块；
- 只在真实最大 `age` 时产出；
- 双格作物只在 bottom 产一次；
- **不取消原方块破坏**；原 main/byproduct 掉落保留，waste 为新增副产。

### 1.3 堆肥

82 条全部写入 TFC `compost_greens/{high,medium,low}`：

- `replace:false`；
- 不覆盖 TFC 原值；
- 校验每条只出现在对应档。

### 1.4 资源

- 82 个 waste item model；
- `layer0: tfc:item/straw` 临时贴图；
- en_us/zh_cn 各 82 个 key；
- 创造页加入全部 82 个。

## 2. 验证

### 纯 Java 原型

```text
PASS: 129 crop P0 checks
```

新增检查：

- 82 条 waste；
- `spinach` 有、`wheat` 无；
- A/TFC 反查；
- 野生/非作物拒绝。

### 编译

```text
gradle compileJava
BUILD SUCCESSFUL
```

### 资源

```text
PASS: 99 models, 2 lang files, 17 recipes, 82 crop_waste, tags valid
```

## 3. 边界

- **未实机验证**：事件顺序、真实最大 age、双格表现、物品掉落；
- B 香料 20 条 waste 未注册，因此当前是 **82/102**；
- 没有取消原掉落，因此这是“新增真实副产”，不是替换主产物；
- TFC 29 完整 blockstate/model 覆盖、蘑菇 worldgen、坚果叶状态仍未完成。

## 4. 下一批

1. 实机验证 82 条 waste；
2. B 香料 20 条 waste，补齐 102；
3. TFC 29 完整种植/收获/掉落覆盖；
4. 蘑菇 worldgen + 自然刷新；
5. 坚果 `nut_state`；
6. 逐作物验收。
