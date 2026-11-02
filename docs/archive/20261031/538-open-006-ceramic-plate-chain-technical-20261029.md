# 538 OPEN-006 陶瓷盘链路复核技术分析

> 日期：2026-10-29
> 状态：**链路静态闭环；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 原问题

用户指出：

- 陶盘 knapping 配方和 TFC 陶碗**完全相同**；
- 陶盘/碗流程没有参考 TFC 陶罐；
- B 还重复引入木碗/陶碗。

## 2. 已有修复

- `unfired_plate` 已改成唯一 `tfc:clay` pattern：
  ```text
  " ### "
  "#####"
  " ### "
  "     "
  "     "
  ```
- 该 pattern 与 TFC 陶碗 pattern 不同；
- TFC 陶碗 pattern 为：
  ```text
  "#   #"
  " ### "
  "     "
  "#   #"
  " ### "
  ```
- B 重复木碗/陶碗物品与配方已删除。

## 3. 链路复核

脚本：`check_ceramic_plate_chain.py`

验证：

1. 陶盘 knapping pattern ≠ TFC 陶碗 pattern；
2. `ceramic/unfired_plate` → `plate/ceramic`（加热）；
3. `unfired_plate + white_dye` → `ceramic/white_unfired_plate`；
4. `white_unfired_plate` → `plate/ceramic_white`（加热）；
5. 15 种染料盘均以 `plate/ceramic_white` 为基底；
6. 旧的 `bowl_wood` / `bowl_ceramic` 配方不存在。

结果：

```text
ceramic plate chain problems 0
```

## 4. 与 TFC 陶罐流程的关系

B 陶盘保留：

- clay knapping；
- heating 烧制（1399 °C）；
- 烧前染色；
- 烧后颜色盘。

与 TFC 陶罐的“打制→烧制”主流程一致；没有再用碗转换或简易 crafting 替代。

## 5. 未完成

- 未实机验证 knapping/加热/染色流程；
- 未处理视觉；
- `plate/ceramic` 与 `plate/ceramic_white` 的用途区分仍需要用户确认是否符合预期。
