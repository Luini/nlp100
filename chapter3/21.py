import wiki
import re

text = wiki.getBody("イギリス")
results = re.findall("(.*Category.*)", text)
for result in results:
    print(result)
