from xml.etree import ElementTree
import re
import pydot_ng as pydot

NO_SYMBOL_POS_PATTERN = re.compile("[A-Z][A-Z][A-Z]?")

class CoreNLP:
    def __init__(self, xmlFileName):
        tree = ElementTree.parse(xmlFileName)
        self.document = tree.getroot().find("document")

    def getSentences(self):
        sentenceElements = self.document.findall("sentences/sentence")
        sentences = [
            Token.createTokens(sentenceElement.findall("tokens/token"))
            for sentenceElement in sentenceElements
        ]
        return sentences

    def getCoreferences(self):
        coreferenceElements = self.document.findall("coreference/coreference")
        return Coreference.createCoreferences(coreferenceElements)

    def getDependencies(self):
        depsElemets = self.document.findall("sentences/sentence/dependencies[@type='collapsed-dependencies']")
        dependencies = [
            Dep.createDeps(depsElemet.findall("dep"))
            for depsElemet in depsElemets
        ]
        return dependencies

    def getParses(self):
        parseElements = self.document.findall("sentences/sentence/parse")
        return [parseElement.text for parseElement in parseElements]

    def createDigraph(self, sentenceId, outputFileName):
        graph = pydot.Dot(graph_type="digraph")
        # ノード追加
        graph.add_node(pydot.Node(0, label="root")) # rootノード
        for id, token in enumerate(self.getSentences()[sentenceId]):
            graph.add_node(pydot.Node(id+1, label=token.word.replace(",", "comma")))
        # 辺追加
        deps = self.getDependencies()[sentenceId]
        for dep in deps:
            graph.add_edge(pydot.Edge(dep.governor, dep.dependent))
        # 出力
        graph.write_png(outputFileName)


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


class Dep:
    def __init__(self, depElement):
        self.type = depElement.get("type")
        self.governor = int(depElement.find("governor").get("idx"))
        self.dependent = int(depElement.find("dependent").get("idx"))
        self.governorText = depElement.find("governor").text
        self.dependentText = depElement.find("dependent").text

    def __str__(self):
        return "[type]{} [governor:{}]{} [dependent:{}]{}".format(self.type, self.governor, self.governorText, self.dependent, self.dependentText)

    @classmethod
    def createDeps(cls, depElements):
        return [cls(depElement) for depElement in depElements]
