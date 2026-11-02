# 313 育苗盘与移栽 P0-M 技术分析

> 日期：2026-10-28
> 目标：加入单格育苗盘、通用幼苗物品和右键移栽，作为六环节中“育苗/移栽”的第一版代码。
> 约束：不推送；不伪造；贴图暂时指向 TFC。

## 1. 范围

本轮实现：

- `nursery_tray` 方块 + BE；
- 3 个 blockstate：0 空 / 1 生长 / 2 可移栽；
- 单个种子槽；
- 1200 tick 生长；
- `seedling` 通用幼苗物品；
- 幼苗用 `CROP_ID` 组件保存原种子物品 ID；
- 右键幼苗在目标位置尝试放置对应 BlockItem 的默认方块；
- 育苗盘右键放种子、右键取出幼苗。

不实现：

- 真正的温湿度/季节；
- 移栽缓苗；
- 无性繁殖苗；
- 非 BlockItem 种子的移栽；
- 实机验证。

## 2. 设计

### 2.1 NurseryTrayBlockEntity

- `seed` 单槽；
- `progress`；
- 只接受 `SeedTreatments.isSeedItemId` 的种子；
- 1200 tick 后 ready；
- `takeSeedling` 生成 `SeedlingItem.forSeed(seedItemId)`。

### 2.2 SeedlingItem

- 读 CROP_ID 组件；
- 解析原种子物品；
- 只有 `BlockItem` 才能解析目标方块；
- 目标位置 `canSurvive` 才放置；
- 成功消耗幼苗；
- 非 BlockItem 明确返回 FAIL，不假装成功。

### 2.3 交互

- `useItemOn`：
  - stage 0 + 种子 → 放入；
  - stage 2 → 取幼苗；
- `useWithoutItem`：stage 2 空手取；
- `onRemove`：掉出未处理的种子。

## 3. 测试

纯 Java：

```text
PASS: 271 crop P0 checks
```

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

资源：

```text
PASS: nursery tray + seedling resources
```

## 4. 风险

- 未实机；
- `SeedlingItem` 只支持 BlockItem 种子；
- 没有缓苗/生长加成；
- 没有育苗盘温度/湿度；
- 没有 GUI/槽位 capability；
- 当前 seeds 可能不是 BlockItem，移栽会明确失败。
