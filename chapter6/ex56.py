import nlp
import re

if __name__ == "__main__":
    coreNLP = nlp.CoreNLP("nlp.txt.xml")
    sentences = coreNLP.sentences
    for coreference in coreNLP.coreferences:
        for mention in coreference.mentions:
            index = mention.sentenceId-1
            start = mention.start-1
            end = mention.end-2
            sentences[index][start].word = "[{} ({}".format(coreference.representative.text, sentences[index][start].word)
            sentences[index][end].word += ")]"

    text = "\n".join([" ".join([token.word for token in sentence]) for sentence in sentences])
    # 整形
    text = text.replace("-LRB- ", "(")
    text = text.replace(" -RRB-", ")")
    text = text.replace(" - ", "-")
    text = text.replace("`", "\'")
    text = re.sub("\' (.*?) \'", lambda x: "\'{}\'".format(x.group(1)), text)
    text = re.sub("(``)|(\'\')", "\"", text)
    text = re.sub("\" (.*?) \"", lambda x: "\"{}\"".format(x.group(1)), text)
    text = re.sub(" ([,.;:?!])", lambda x: x.group(1), text)

    print(text)
