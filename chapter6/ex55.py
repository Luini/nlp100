from ex53 import getTokens

if __name__ == "__main__":
    tokens = getTokens("nlp.txt.xml")

    NNPs = [
        token.find("word").text
        for token in tokens
        if token.find("POS").text == "NNP"
    ]

    print("\n".join(NNPs))
