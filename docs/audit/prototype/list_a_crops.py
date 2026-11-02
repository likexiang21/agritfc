import zipfile, pathlib
p = pathlib.Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\TFCFarmingPlus-NeoForge-1.21.1-0.1.0.jar")
with zipfile.ZipFile(p) as z:
    names=[n for n in z.namelist() if 'blockstates' in n and 'crop' in n]
    print(len(names)); print(*names[:10],sep='\n')
