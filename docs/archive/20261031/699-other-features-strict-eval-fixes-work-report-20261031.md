# 699 其他功能严格符合性评估修复工作报告

> 日期：2026-10-31
> 状态：**代码/数据已修复；未实机**

## 1. 完成

- 世界生成 biome 标签加入 85 个 TFC 陆生 biome，修复蘑菇/坚果/香料树在 TFC 世界不生成；
- 厨房食物展示/水果盘改用 `FoodCapability.has`，接受 TFC/B 食物；
- 锅铲勺油 `tryFluidTransfer` 参数顺序修正；
- en_us/zh_cn 所有 lang 键斜杠改为点号（1107/1107）；
- 菌包/育苗盘按 stage 增加不同模型。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
json 6535 / models 3709 / blockstates 539 / item_models 957
lang 1107 / 1107 / missing 0 / extra 0
final_static_audit problems 0
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 3. 未完成

- 未实机；
- 香料树/树苗贴图、坚果叶挂果 overlay、14 个 Firmalife 废枝叶图标/中文名；
- 菌包破坏丢进度、锅自动化食材不进入 entries、流体不掉落、部分设备无 BER；
- 世界生成是否实际触发仍需实机。
