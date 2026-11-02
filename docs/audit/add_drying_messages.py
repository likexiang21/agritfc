import json, pathlib
root=pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus/lang")
keys={
 "message.tfcagricultureplus.drying_rack.empty":("The rack is empty.","晾架是空的。"),
 "message.tfcagricultureplus.drying_rack.not_ready":("Drying is not finished yet.","尚未干燥完成。"),
 "message.tfcagricultureplus.drying_rack.rotten":("The food is rotten.","食物已腐烂。"),
 "message.tfcagricultureplus.drying_rack.no_recipe":("No drying recipe for this item.","该物品没有干燥配方。"),
 "message.tfcagricultureplus.drying_rack.full":("The rack is full.","晾架已满。"),
}
for name,idx in (("en_us.json",0),("zh_cn.json",1)):
 p=root/name; d=json.loads(p.read_text(encoding="utf-8"))
 for k,v in keys.items(): d[k]=v[idx]
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(name,len(d))
