import ex25
import re

def getResult():
    dec = ex25.getResult()
    pattern = r"((?<!')'{2,}(?!'))(?P<str>.+)\1"
    dec = {key:re.sub(pattern, repl, value) for key, value in dec.items()}
    return dec

def repl(matchobj):
    if matchobj.group("str"):
        return matchobj.group("str")
    else:
        return ""

if __name__ == "__main__":
    baseInfo = getResult()
#    print(baseInfo)
    for key, value in baseInfo.items():
        print(key + " : " + value)
