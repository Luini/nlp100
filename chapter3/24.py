import wiki
import re

text = wiki.getBody("イギリス")
pattern = re.compile(r"((?:File|ファイル):(.*?)\|)|(\[\[(?:File|ファイル):([^|]*?)\]\])")
results = pattern.findall(text)
for result in results:
    if result[1]!="":
        print(result[1])
    if result[3]!="":
        print(result[3])
