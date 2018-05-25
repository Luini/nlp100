from myCabocha import Morph

def formatter(cabochaFile):
    with open(cabochaFile, 'r') as file:
        sentences = []
        line = file.readline().rstrip()
        while line:
            sentence = []
            while line != "EOS":
                if line[0] != "*":
                    sentence.append(Morph.createFromCabochaLine(line))
                line = file.readline().rstrip()
            if sentence:
                sentences.append(sentence)
            line = file.readline().rstrip()
    return sentences

if __name__ == "__main__":
    sentences = formatter("neko.txt.cabocha")
    '''
    for sentence in sentences:
        print("===== Sentence =====")
        for m in sentence:
            print(m)
    '''
    for m in sentences[2]:
        print(m)
