# 502 最终构建与环境冻结 P0-DC 技术分析

> 日期：2026-10-29
> 目标：冻结最终交付物并记录环境恢复状态。
> 约束：不推送；不伪造。

## 1. 最终 jar

```text
TFCAgriculturePlus-NeoForge-1.21.1-0.1.0.jar
2,745,942 bytes
SHA-256 E64953BA2F7C4075DAA101A6426C99B137D6060DD9C6B4866AA2F6CC606F7E37
debug_bytes = False
```

## 2. 最终校验

- `validate_crop_p0a.py` 全 PASS；
- `CropYieldProto` 393 PASS；
- 最终 jar 加载 smoke 通过（P0-CX）。

## 3. 环境

- `tfctest2` 不存在；
- `options.txt` 已恢复（SHA-256 `90C19365...`）；
- 游戏 mods 中为旧版 B jar；
- 无测试客户端运行；
- 未推送。

## 4. 未完成

- A 87 / TFC 29 / TFC 10 全量实机；
- 自然世界生成；
- 树叶衰减方块状态；
- 全量 159 行验收；
- 视觉/平衡；
- 长时间稳定性。

## 5. 目标状态

active，不能 mark complete。
