from ex53 import getTokens
import re

if __name__ == "__main__":
    tokens = getTokens("nlp.txt.xml")
    # 記号を除外する
    wordPosPattern = re.compile("[A-Z][A-Z][A-Z]?")
    words = [
        (token.find("word").text ,token.find("lemma").text ,token.find("POS").text)
        for token in tokens
        if wordPosPattern.match(token.find("POS").text) and token.find("POS").text != "POS"
    ]

    print("\n".join(["\t".join(word) for word in words]))
