from xml.etree import ElementTree
import re

def getTokens(xmlFileName):
    tree = ElementTree.parse(xmlFileName)
    root = tree.getroot()
    sentences = root.findall("document/sentences/sentence")
    sentences = [sentence.findall("tokens/token") for sentence in sentences]
    tokens = [token for sentence in sentences for token in sentence]
    return tokens

if __name__ == "__main__":
    tokens = getTokens("nlp.txt.xml")
    # 記号を除外する
    wordPosPattern = re.compile("[A-Z][A-Z][A-Z]?")
    words = [
        token.find("word").text
        for token in tokens
        if wordPosPattern.match(token.find("POS").text) and token.find("POS").text != "POS"
    ]

    print("\n".join(words))
