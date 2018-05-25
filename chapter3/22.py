import wiki
import re

text = wiki.getBody("イギリス")
pattern = re.compile(".*Category:(.+?)(?:\|.*?)?\]\].*")
results = pattern.findall(text)
for result in results:
    print(result)
