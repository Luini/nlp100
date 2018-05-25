import sys
import gzip
import json

def getBody(title):
    with gzip.open("jawiki-country.json.gz", 'rt') as file:
        wikiJsonString = file.readline()
        while wikiJsonString:
            # パース（辞書型になる）
            wikiJson = json.loads(wikiJsonString)
            # titelがマッチしていたらその本文を返す
            if wikiJson["title"] == title:
                return wikiJson["text"]
            # 次の行を読み込む
            wikiJsonString = file.readline()
    # 全ての行が読み込み終わってもマッチするものがなければ No text を返す
    return "No text"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python3 wiki.py [title]")
    else:
        print(getBody(sys.argv[1]))
