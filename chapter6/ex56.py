import nlp
import re

# Stanford Core NLPの解析結果の記号やスペースをいい感じに整形する関数
def coreNlpTextFormatter(nlpText):
    nlpText = nlpText.replace("-LRB- ", "(")
    nlpText = nlpText.replace(" -RRB-", ")")
    nlpText = nlpText.replace(" - ", "-")
    nlpText = nlpText.replace("`", "\'")
    nlpText = re.sub("\' (.*?) \'", lambda x: "\'{}\'".format(x.group(1)), nlpText)
    nlpText = re.sub("(``)|(\'\')", "\"", nlpText)
    nlpText = re.sub("\" (.*?) \"", lambda x: "\"{}\"".format(x.group(1)), nlpText)
    nlpText = re.sub(" ([,.;:?!])", lambda x: x.group(1), nlpText)
    return nlpText


if __name__ == "__main__":
    coreNLP = nlp.CoreNLP("nlp.txt.xml")
    sentences = coreNLP.getSentences()
    for coreference in coreNLP.getCoreferences():
        for mention in coreference.mentions:
            index = mention.sentenceId-1
            start = mention.start-1
            end = mention.end-2
            sentences[index][start].word = "[{} ({}".format(coreference.representative.text, sentences[index][start].word)
            sentences[index][end].word += ")]"

    text = "\n".join([" ".join([token.word for token in sentence]) for sentence in sentences])
    text = coreNlpTextFormatter(text)
    print(text)
