import ex27
import re

def getResult():
    dec = ex27.getResult()
    # {{lang|*|*}}
    pattern = r"\{\{lang\|.*?\|(.*?)\}\}"
    dec = {key:re.sub(pattern, repl, value) for key, value in dec.items()}
    # <br/>
    pattern = r"\<br.*?\>"
    dec = {key:re.sub(pattern, "", value) for key, value in dec.items()}
    # *(**)
    pattern = r"\*+?"
    dec = {key:re.sub(pattern, "", value) for key, value in dec.items()}
    # 改行
    pattern = r":\n"
    dec = {key:re.sub(pattern, ":", value) for key, value in dec.items()}
    pattern = r"\n"
    dec = {key:re.sub(pattern, "，", value) for key, value in dec.items()}
    # ファイル
    pattern = r"\[\[ファイル:.*\|(.*?)\]\]"
    dec = {key:re.sub(pattern, repl, value) for key, value in dec.items()}
    # 外部参照
    pattern = r"\[http://.*?\s(.*?)\]"
    dec = {key:re.sub(pattern, repl, value) for key, value in dec.items()}
    # <ref>
    pattern = r"\<ref\s.*?/\>"
    dec = {key:re.sub(pattern, "", value) for key, value in dec.items()}
    pattern = r"\<ref.*?\>(.*?)\</ref\>"
    dec = {key:re.sub(pattern, refRepl, value) for key, value in dec.items()}
    return dec

def repl(matchobj):
    if matchobj.group(1):
        return matchobj.group(1)
    else:
        return ""

def refRepl(matchobj):
    if matchobj.group(1):
        return " [" + matchobj.group(1) + "]"
    else:
        return ""

if __name__ == "__main__":
    baseInfo = getResult()
#    print(baseInfo)
    for key, value in baseInfo.items():
        print(key + " : " + value)
