import wiki
import re

text = wiki.getBody("イギリス")
pattern = re.compile("(?P<level>={2,})\s*(?P<section>.*?)\s*(?P=level)")
results = pattern.findall(text)
for result in results:
    print(str(len(result[0])-1) + " " + result[1])
#    print(result[1] + " [Lev." + str(len(result[0])-1) + "]")
