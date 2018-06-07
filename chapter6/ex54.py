import nlp

if __name__ == "__main__":
    coreNLP = nlp.CoreNLP("nlp.txt.xml")
    sentences = [
        nlp.Token.getNoSymbolTokens(sentence) # 記号を除外する
        for sentence in coreNLP.getSentences()
    ]
    words = [
        (token.word, token.lemma, token.pos)
        for sentence in sentences for token in sentence
    ]

    print("\n".join(["\t".join(word) for word in words]))
