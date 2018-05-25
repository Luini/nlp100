import wiki
import re

def getResult():
    text = wiki.getBody("イギリス")
    pattern = re.compile("^{\{基礎情報.*$.*?^\}\}$", re.M + re.S)
    template = pattern.search(text)
    template = template.group()
    pattern = re.compile("^\|(.+?)\s*=\s*(.+?)$(?=\n^[|}])", re.M + re.S)
    results = pattern.findall(template)
    return {name:value for name, value in results}

if __name__ == "__main__":
    baseInfo = getResult()
#    print(baseInfo)
    for key, value in baseInfo.items():
        print(key + " : " + value)
