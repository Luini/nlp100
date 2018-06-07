import nlp
from ex56 import coreNlpTextFormatter

class Node:
    def __init__(self, type, text, children):
        self.type = type
        self.text = text
        self.children = children

    def __str__(self):
        if len(self.children) > 0:
            return " ".join([str(child) for child in self.children])
        else:
            return self.text

    def getNPs(self):
        if self.type == "NP":
            NPs = [str(self)]
        else:
            NPs = []
        for child in self.children:
            NPs += child.getNPs()
        return NPs

    @classmethod
    def createTree(cls, parseString, startPosition):
        position = startPosition+1 # 先頭は '(' のはずなので除外
        type = ""
        while parseString[position] != ' ':
            type += parseString[position]
            position += 1
        # 子がいる場合
        if parseString[position+1] == '(':
            children = []
            while parseString[position] == ' ':
                (child, position) = cls.createTree(parseString, position+1)
                children.append(child)
            return (cls(type, "", children), position+1) # nodeと次の開始位置を返す
        # 子がいない場合
        else:
            position += 1 # スペース除外
            text = ""
            while parseString[position] != ')':
                text += parseString[position]
                position += 1
            return (cls(type, text, []), position+1) # nodeと次の開始位置を返す


if __name__ == "__main__":
    coreNLP = nlp.CoreNLP("nlp.txt.xml")
    parses = coreNLP.getParses()
    for parse in parses:
        (tree, end) = Node.createTree(parse, 0)
        NPs = tree.getNPs()
        print("\n".join([coreNlpTextFormatter(NP) for NP in NPs]), end='\n\n')
