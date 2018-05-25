import mecab

list = [morpheme["base"] for morpheme in mecab.formatter("neko.txt.mecab") if morpheme["pos"] == "名詞" and morpheme["pos1"] == "サ変接続"]
list = list[:20]
for l in list:
    print(l)
