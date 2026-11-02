import zipfile, pathlib
p = pathlib.Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\TFCFarmingPlus-NeoForge-1.21.1-0.1.0.jar")
with zipfile.ZipFile(p) as z:
    hits=[]
    for n in z.namelist():
        if n.endswith(".json") and "blockstates" in n:
            s=z.read(n).decode("utf-8", errors="ignore")
            if '"part"' in s: hits.append(n)
    print(len(hits)); print(*hits[:10],sep="\n")
