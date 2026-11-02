# 623 模组代码问题筛查工作报告（第二轮）

> 日期：2026-10-30
> 状态：**静态筛查完成；未实机、未启动客户端**

## 1. 完成

- 复核二次崩溃日志；
- 修复烤箱配方/JEI 分类路径；
- 修复 `log_pile` 标签；
- 修复 `plant_fiber_rope` 配方；
- 修复 Patchouli icon；
- 补中英方块名称；
- 扫描全部方块默认状态构造与静态注册 `get()`；
- 运行完整静态验证集。

## 2. 结果

```text
final_static_audit problems 0
lang 1092 / 1092 / missing 0
B tag missing refs 0
recipe reference problems 0
bad Patchouli icons 0
firmalife:oven refs 0
```

## 3. 未做

- 未实机；
- 未启动客户端；
- 未通知玩家测试；
- 仍有运行时路径无法静态证明。

## 4. 当前 jar

```text
2,922,025 bytes
SHA-256 3809EF4E55819812E982DDBB39231CC1CFEEEC31F746C2F79812F61F795403B1
```
