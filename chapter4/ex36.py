import mecab

def count(morphemes):
#    morphemes = [morpheme for morpheme in morphemes if morpheme["pos"] != "記号"]
    morphemesCount = {}
    for m in morphemes:
        if m["base"] in morphemesCount.keys():
            morphemesCount[m["base"]] += 1
        else:
            morphemesCount[m["base"]] = 1
    return morphemesCount

if __name__ == "__main__":
    morphemesCount = count(mecab.formatter("neko.txt.mecab"))
    morphemesCount = sorted(morphemesCount.items(), key=lambda x: -x[1])
#    morphemesCount = morphemesCount[:20]
    for key, value in morphemesCount:
        print(str(value) + " " + key)
