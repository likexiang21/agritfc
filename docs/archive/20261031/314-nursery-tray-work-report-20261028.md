# 314 育苗盘与移栽 P0-M 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：单格育苗盘 + 通用幼苗 + 右键移栽第一版；实机与完整六环节未完成。

## 1. 完成内容

### 1.1 育苗盘

- `tfcagricultureplus:nursery_tray`
- stage 0 空 / 1 生长 / 2 可移栽
- 单种子槽
- 1200 tick 生长
- 右键放入种子 / 右键取出幼苗
- 破坏掉出未处理种子

### 1.2 幼苗

- `tfcagricultureplus:seedling`
- CROP_ID 组件保存原种子 ID
- 右键目标位置：
  - 解析原种子为 BlockItem；
  - 放置目标方块默认状态；
  - 目标 `canSurvive` 才成功；
  - 非 BlockItem 明确失败。

### 1.3 资源

- blockstate 3 variants；
- block model + item model；
- seedling item model；
- loot table；
- 配方：`oak_planks + tfc:straw` → nursery tray；
- en/zh 语言。

## 2. 验证

```text
PASS: 271 crop P0 checks
PASS: nursery tray + seedling resources
```

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

`processResources`：

```text
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机验证**；
- 只支持 BlockItem 种子移栽；
- 没有缓苗/生长加成；
- 没有温湿度/季节；
- 没有 GUI 或 item capability；
- 没有无性繁殖苗；
- 不能宣称六环节完成。

## 4. 下一批

1. 缓苗/生长加成；
2. 温湿度；
3. 无性苗；
4. TFC 29 剩余覆盖；
5. 全部完成后再统一实机测试。
