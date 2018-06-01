import re

def separateSentences(fileName):
    with open(fileName, 'r') as file:
        sentences = []
        # 文の区切りパターン (. or ; or : or ? or !) → 空白文字 → 英大文字
        SeparationPattern = re.compile("(?<=[.;:?!])\s(?=[A-Z])")
        for line in file:
            line = line.rstrip()
            if line: # 空行除外
                sentences += SeparationPattern.split(line)
    return sentences


if __name__ == "__main__":
    sentences = separateSentences("nlp.txt")
    print("\n".join(sentences))
