import mecab

morphemes = mecab.formatter("neko.txt.mecab")
result = []
nFlag = False
for morpheme in morphemes:
    if morpheme["pos"] == "名詞":
        if nFlag:
            result[len(result)-1].append(morpheme["surface"])
        else:
            result.append([morpheme["surface"]])
            nFlag = True
    else:
        nFlag = False
#result = result[:20]
for n in result:
    if len(n) >= 2:
        print("".join(n))
