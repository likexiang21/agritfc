# 500 作物系统最终交接 P0-DB 技术分析

> 日期：2026-10-29
> 状态：**代码/资源/构建完成；实机样本覆盖主机制；目标未全部完成**
> 约束：不推送；不伪造。

## 1. 最终构建

```text
TFCAgriculturePlus-NeoForge-1.21.1-0.1.0.jar
2,745,942 bytes
debug_bytes = False
validate_crop_p0a.py PASS
CropYieldProto PASS: 393 checks
```

## 2. 已验证的实机主机制

- 客户端加载 / worldgen codec；
- 注册计数 15/5/82/15；
- 方块/物品放置；
- basil / bag / nursery 生长；
- 3 坚果 + 5 香料树；
- 玩家破坏收获 + 掉落物 ID；
- 未成熟作物不掉落；
- 菌包采集 / naturalOnly 拒绝；
- 育苗盘产出 / 移栽 / 生长 / 收获；
- 3 个蘑菇 feature `/place`；
- TFC 直接播种 vs A/B 育苗门；
- 旧存档/最终 jar 加载 smoke。

## 3. 未完成

- A 87 / TFC 29 / TFC 10 全量实机；
- 自然世界生成（非 `/place`）；
- 树叶衰减方块状态；
- 全量 159 行验收；
- 视觉/平衡；
- 长时间稳定性。

## 4. 环境

- 游戏 jar 已恢复旧版；
- `options.txt` 已恢复；
- `tfctest2` 已删除；
- 无测试客户端运行；
- 未推送。

## 5. 目标状态

**active**，不能 mark complete。
