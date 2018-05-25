import ex26
import re

def getResult():
    dec = ex26.getResult()
    pattern = r"(?:\[\[([^|]*?)\]\])|(?:\[\[[^|]*?\|([^|]*?)\]\])"
    dec = {key:re.sub(pattern, repl, value) for key, value in dec.items()}
    return dec

def repl(matchobj):
    if matchobj.group(1):
        return matchobj.group(1)
    elif matchobj.group(2):
        return matchobj.group(2)
    else:
        return ""

if __name__ == "__main__":
    baseInfo = getResult()
#    print(baseInfo)
    for key, value in baseInfo.items():
        print(key + " : " + value)
