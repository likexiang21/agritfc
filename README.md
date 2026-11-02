# mod_rebuild — TFC Agriculture Plus 开发树

> 记录日期：2026-10-31
> 状态：**代码持续修复中；静态构建通过；未实机验证**。
> 本目录是与 `moddev/` 并行的新版开发树；旧树保持原样，未移动、未删除。

## 1. 项目

- Minecraft 1.21.1 / NeoForge 21.1.233
- TFC 4.2.12 / Firmalife 3.0.15 / AFC 2.1.3 / JEI 19.57.0.449
- 模组 ID：`tfcagricultureplus`
- Java 包根：`io.github.likexiang21.tfcplus.agriculture`

## 2. 模块

- `tfcfarmingplus/`：A 内容（前置依赖）
- `tfcagricultureplus/`：B 内容（本模组）

## 3. 构建

```powershell
cd mod_rebuild/tfcagricultureplus
.\gradlew.bat build --console=plain
```

产物：

```text
mod_rebuild/tfcagricultureplus/build/libs/TFCAgriculturePlus-NeoForge-1.21.1-0.1.0.jar
```

当前交付 jar 位于 `mods/`：

```text
2,973,658 bytes
SHA-256 4AF65C57A47C7D43550E3165D0D80B159D9CD2FA71A3D929EFF5C42B643FFAA0
```

## 4. 文档

当前只保留三份：

- [最终审计与修复报告](docs/最终审计与修复报告-20261031.md)
- [验证记录](docs/验证记录-20261031.md)
- [未清问题账本](docs/audit/OPEN-ISSUES.md)

历史 442 份逐项过程文档已归档到 `docs/archive/20261031/`，不再作为当前依据。

## 5. 约束

- 不启动客户端/游戏，不做实机验证；
- 不推送，不通知玩家测试；
- 所有结论来自静态审查、构建、数据/资源校验；
- 静态通过不等于运行期正确，未验证项在最终报告中列出。

## 6. 历史

旧树 `moddev/` 保持原样；完整历史文档见 `docs/archive/20261031/`。
