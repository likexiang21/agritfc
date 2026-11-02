# 415 实机注册计数验证 P0-BK 工作报告

> 日期：2026-10-29
> 状态：**注册计数已确认；未推送、未提交远程**
> 范围：真实客户端注册计数日志；未做玩法测试。

## 1. 完成内容

- 注册后日志输出 registry 计数；
- 真实客户端加载；
- 记录：
  - spiceCrops=15；
  - spiceTrees=5；
  - cropWaste=82；
  - wildMushrooms=15；
- 停止客户端并恢复旧 jar/options。

## 2. 证据

```text
[TFC Agriculture Plus] registries:
  spiceCrops=15, spiceTrees=5, cropWaste=82, wildMushrooms=15
Starting integrated minecraft server version 1.21.1
```

日志：

`mod_rebuild/docs/audit/runtime-registry-counts-20261029.log`

## 3. 结论

- 香料/蘑菇/废枝叶注册表大小正确；
- 之前 setblock 未通过的 3 个 ID **不是注册缺失**；
- 仍需真实放置/支撑测试。

## 4. 边界

- 只验证注册表大小；
- 未验证 blockstate/model 全部正确；
- 未验证放置/生长/收获；
- 未验证树/菌包玩法；
- 不能宣称目标完成。

## 5. 下一批

1. 真实放置测试；
2. 育苗/种植/收获；
3. 树苗/菌包；
4. 全量验收。
