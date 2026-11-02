# 621 二次崩溃彻查与修复工作报告

> 日期：2026-10-30
> 状态：**代码/数据已修复；未实机**

## 1. 完成

- 15 条 `firmalife:oven` → `tfc:heating`；
- 删除 `recipe/oven/`；
- JEI `firmalife:oven` 分类缺失类保护（隐藏分类）；
- 修复 `log_pile` → `lumber_pile` 标签；
- `plant_fiber_rope` 改 shapeless；
- Patchouli `crop/strawberry` → `seeds/strawberry`；
- 修正 Patchouli icon 验证脚本只认 item model；
- `gradle build` 成功；
- 新 jar 已迁移到 `mods/`，`mods` 中只有当前版本 jar。

## 2. 校验

```text
B tag missing refs 0
firmalife:oven refs 0
heating recipes 16
bad Patchouli icons 0
json 6484 / bad 0
final_static_audit problems 0
```

当前 jar：

```text
2,921,490 bytes
SHA-256 FB2B2201A9751700D37F1CEA723FA81DF8CE16FC12FB67F8786192C9A0484837
```

## 3. 未做

- 未实机；
- 需用户启动确认崩溃消失。

## 4. 说明

上一轮曾尝试启动客户端，收到“不要自行尝试启动”后已停止；
本轮所有结论来自日志和静态验证，没有把问题归给用户或其它模组。
