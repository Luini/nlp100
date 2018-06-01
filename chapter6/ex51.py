from ex50 import separateSentences

def separateWords(fileName):
    sentences = separateSentences(fileName)
    # 空白で分割
    sentences = [sentence.split() for sentence in sentences]
    return sentences


if __name__ == "__main__":
    sentences = separateWords("nlp.txt")
    print("\n\n".join(["\n".join(sentence) for sentence in sentences]))
