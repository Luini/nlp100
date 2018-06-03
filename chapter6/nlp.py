from xml.etree import ElementTree
import re

NO_SYMBOL_POS_PATTERN = re.compile("[A-Z][A-Z][A-Z]?")

class CoreNLP:
    def __init__(self, xmlFileName):
        tree = ElementTree.parse(xmlFileName)
        root = tree.getroot()
        sentences = root.findall("document/sentences/sentence")
        self.sentences = [
            Token.createTokens(sentence.findall("tokens/token"))
            for sentence in sentences
        ]
        coreferenceElements = root.findall("document/coreference/coreference")
        self.coreferences = Coreference.createCoreferences(coreferenceElements)


class Token:
    def __init__(self, tokenElement):
        self.word = tokenElement.find("word").text
        self.lemma = tokenElement.find("lemma").text
        self.pos = tokenElement.find("POS").text
        self.ner = tokenElement.find("NER").text

    def __str__(self):
        return "[word]{} [lemma]{} [POS]{} [NER]{}".format(self.word, self.lemma, self.pos, self.ner)

    @classmethod
    def createTokens(cls, tokenElements):
        return [cls(tokenElement) for tokenElement in tokenElements]

    @classmethod
    def getNoSymbolTokens(cls, tokens):
        # 記号を除外する
        noSymbolTokens = [
            token
            for token in tokens
            if NO_SYMBOL_POS_PATTERN.match(token.pos) and token.pos != "POS"
        ]
        return noSymbolTokens


class Coreference:
    def __init__(self, coreferenceElement):
        representativeElement = coreferenceElement.find("mention[@representative='true']")
        self.representative = Mention(representativeElement)
        self.mentions = [
            Mention(mentionElement)
            for mentionElement in coreferenceElement.findall("mention")
            if mentionElement != representativeElement
        ]

    def __str__(self):
        returnStr = "- representative -\n" + str(self.representative) + "\n- mentions -"
        for mention in self.mentions:
            returnStr += "\n" + str(mention)
        return returnStr

    @classmethod
    def createCoreferences(cls, coreferenceElements):
        return [cls(coreferenceElement) for coreferenceElement in coreferenceElements]


class Mention:
    def __init__(self, mentionElement):
        self.sentenceId = int(mentionElement.find("sentence").text)
        self.start = int(mentionElement.find("start").text)
        self.end = int(mentionElement.find("end").text)
        self.text = mentionElement.find("text").text

    def __str__(self):
        return "[sentenceId]{} [start]{} [end]{} [text]{}".format(self.sentenceId, self.start, self.end, self.text)
