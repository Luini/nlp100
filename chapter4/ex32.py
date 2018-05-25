import mecab

vList = [morpheme["base"] for morpheme in mecab.formatter("neko.txt.mecab") if morpheme["pos"] == "動詞"]
vList = vList[:20]
for v in vList:
    print(v)
