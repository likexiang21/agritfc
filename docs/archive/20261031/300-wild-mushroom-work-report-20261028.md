# 300 野生蘑菇 P0-D 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：15 种野生蘑菇方块 + 世界生成 + 随机刻刷新；菌包尚未实现。

## 1. 完成内容

### 1.1 15 种蘑菇

- 可栽培候选 11 种；
- 自然专用 4 种：porcini · morel · chanterelle · black_truffle；
- 全部注册 `wild_mushroom/<species>` 方块与 BlockItem。

### 1.2 野生行为

`WildMushroomBlock`：

- `AGE` 0..2；
- 随机刻生长；
- 成熟后向附近 3×3 兼容土壤扩散；
- 支持 TFC `#tfc:dirt` / `#tfc:grass`；
- 不做菌包；自然专用 4 种未来也不允许菌包。

### 1.3 世界生成

- 15 个 configured feature；
- 15 个 placed feature；
- biome tag：森林/针叶林/沼泽；
- `neoforge:add_features` biome modifier。

### 1.4 资源

- 15 blockstate（age 0/1/2）；
- 15 block model + item model；
- 15 loot table；
- 15 语言 key（en/zh）；
- 临时贴图：`tfc:block/plant/red_oat_grass/red_oat_grass`。

## 2. 验证

### 纯 Java 原型

```text
PASS: 134 crop P0 checks
```

新增：

- 15 种；
- 4 种自然专用；
- 11 种可栽培候选；
- porcini 自然专用；
- oyster wild block path。

### 编译

```text
gradle compileJava
BUILD SUCCESSFUL
```

### 资源

```text
PASS: 99 item models, 2 lang files, 17 recipes, 82 crop_waste, 15 wild mushrooms, tags valid
```

`processResources`：

```text
BUILD SUCCESSFUL
```

构建输出确认：

- 15 个 wild mushroom blockstate；
- 15 个 placed feature。

## 3. 边界

- **未实机验证** worldgen / biome modifier / 随机刷新；
- 菌包未实现，所以“可栽培 11 种”目前也只是野生；
- 自然专用 4 种的“禁止菌包”目前体现为没有菌包系统；
- 所有蘑菇共用临时 TFC 贴图；
- 随机刷新只从已有成熟蘑菇扩散，不保证灭绝后重新出现；
- 没有生成密度/群系概率调参。

## 4. 下一批

1. 实机验证蘑菇 worldgen/刷新；
2. 菌包系统，显式排除自然专用 4 种；
3. TFC 29 完整种植/收获覆盖；
4. 坚果 `nut_state` 叶状态；
5. 全部逐作物验收。
