from ex51 import separateWords
from stemming.porter2 import stem

if __name__ == "__main__":
    sentences = separateWords("nlp.txt")
    sentences = [[word + "\t" + stem(word.strip(".;:?!,()'\"")) for word in sentence] for sentence in sentences]
    print("\n\n".join(["\n".join(sentence) for sentence in sentences]))
