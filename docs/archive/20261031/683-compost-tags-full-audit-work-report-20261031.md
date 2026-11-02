# 683 废枝叶/湿草/坚果壳堆肥标签修复工作报告

> 日期：2026-10-31
> 状态：**数据已修复；未实机**

## 1. 完成

- 解析文档 291 §4.1.2 的 82 个 `crop_waste` 高/中/低分类；
- 生成 5 个 TFC 堆肥标签文件：
  - `tfc:compost_greens/high`
  - `tfc:compost_greens/medium`
  - `tfc:compost_greens/low`
  - `tfc:compost_browns/high`
- 新增覆盖：
  - 82 `crop_waste`；
  - 10 `bush_waste`；
  - `wet_grass`；
  - 8 `nut_shell`；
- TFC 原始 values 全部保留，只追加 B 条目；
- `check_tag_refs.py`：B tag missing refs 0；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
B tag missing refs 0
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,928,335 bytes
SHA-256 31BDD86A58F94499A25DBBBC9F59DD1064A4C0901C659459A025C2BDF19F7EED
```

## 3. 未做

- 未实机验证堆肥桶；
- 未添加饲料/青贮等其它出口。
