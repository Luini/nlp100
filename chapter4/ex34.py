import mecab

morphemes = mecab.formatter("neko.txt.mecab")
threeMorphemesList = [morphemes[i:i+3] for i in range(len(morphemes)-2)]
results = [threeMorphemes[0]["surface"]+threeMorphemes[1]["surface"]+threeMorphemes[2]["surface"] for threeMorphemes in threeMorphemesList if threeMorphemes[0]["pos"] == "名詞" and threeMorphemes[1]["surface"] == "の" and threeMorphemes[2]["pos"] == "名詞"]
#results = results[:20]
for r in results:
    print(r)
