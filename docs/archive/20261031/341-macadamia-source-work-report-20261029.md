# 341 澳洲坚果来源 P0-Z 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：澳洲坚果从 A 树叶的临时来源；新树未完成。

## 1. 完成内容

- `MacadamiaDropHandler`；
- 精确匹配 A `macadamia_leaves`；
- 5% 掉 B `macadamia` + `nut_shell/macadamia`；
- 不取消原掉落；
- 主入口注册。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有：

```text
PASS: 283 crop P0 checks
```

## 3. 边界

- **未实机**；
- 临时 5% 来源，不是正式树；
- pistachio/cashew 仍无来源；
- 未验证 A 树叶 ID/掉落；
- 不能宣称坚果链完成。

## 4. 下一批

1. 实机核对 A 树叶；
2. pistachio/cashew 树；
3. 坚果加工；
4. 全量实机测试。
