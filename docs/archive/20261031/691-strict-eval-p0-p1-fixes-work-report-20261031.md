# 691 严格全量评估 P0/P1 修复工作报告

> 日期：2026-10-31
> 状态：**代码已修复；未实机**

## 1. 评估来源

独立子代理对 139 个 Java、6516 个 JSON、539 个 blockstate、943 个 item model 做了静态全量评估，并独立构建、校验。

结论：**未达到“无已知重大静态代码问题”**，存在 1 个 P0、5 个 P1。本轮修复如下。

## 2. 已修

### P0

- `UnifiedCropHarvestHandler` 调用 `Block.getDrops` 时把 BlockEntity 从 `null` 改为 `level.getBlockEntity(pos)`；
- 该参数决定 TFC `crop_yield_uniform` 是否读取 `CropBlockEntity`；否则返回 `min=0`，导致 95 个 A/TFC 非谷类物种主产物为 0。

### P1

- 移除 `CropPropagation` 对 `tfc:` 的前缀豁免；TFC 种子返回裸物种名并真正查表；
- 补 TFC 谷类/工业作物 11 项与 A 纤维/油料 10 项的显式分类；
- 4 个 TFC `*_bush_cane` 映射到对应灌木废枝；
- 草莓灌木非 FRUITING 期也给 `crop_waste/strawberry`；
- `tfc:wild_crop` / `tfcfarmingplus:wild_crop` 纳入废枝叶来源；
- 播种门取消时显示育苗提示（新增 en_us/zh_cn 键）；
- Firmalife 香草不再额外掉 B 产物，并将 B 废枝改为与 Firmalife 一致的刀具门槛。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 4. 未完成

- 未实机；P0 只验证参数链正确，不验证实际数量；
- Firmalife 其余 12+2 个植物方块已由 694/695 接入 B 废枝叶；
- TfcSeedReturnHandler/ACropSeedReturnHandler 仍注册但在成熟作物路径被统一收获器抢先取消；CropWasteHandler 仍负责 wild_crop 的 mature 分支，不再一概视为死代码；
- 旧文档 688/689 的 jar 指纹需继续按当前 jar 更新。
