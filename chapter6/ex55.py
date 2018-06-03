import nlp

if __name__ == "__main__":
    coreNLP = nlp.CoreNLP("nlp.txt.xml")

    persons = [
        token.word
        for sentence in coreNLP.sentences for token in sentence
        if token.ner == "PERSON"
    ]

    print("\n".join(persons))
