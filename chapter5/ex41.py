from myCabocha import Morph
from myCabocha import Chunk

def formatter(cabochaFile):
    with open(cabochaFile, 'r') as file:
        sentences = []
        line = file.readline().rstrip()
        while line:
            sentence = []
            while line != "EOS":
                chunk = Chunk.createFromCabochaLine(line)
                line = file.readline().rstrip()
                while line[0] != "*" and line != "EOS":
                    chunk.addMorph(Morph.createFromCabochaLine(line))
                    line = file.readline().rstrip()
                sentence.append(chunk)
            if sentence:
                for index, chunk in enumerate(sentence):
                    if chunk.dst >= 0:
                        sentence[chunk.dst].addSrc(index)
                sentences.append(sentence)
            line = file.readline().rstrip()
    return sentences

if __name__ == "__main__":
    sentences = formatter("neko.txt.cabocha")
    '''
    for sentence in sentences:
        print("===== Sentence =====")
        for c in sentence:
            print(c)
    '''
    for c in sentences[7]:
        print(c)
