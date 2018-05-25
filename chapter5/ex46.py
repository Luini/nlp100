from myCabocha import Morph
from myCabocha import Chunk
from ex41 import formatter

if __name__ == "__main__":
    sentences = formatter("neko.txt.cabocha")
    pairs = [[chunk.getPredicate(), [[sentence[src].getPostposition(), sentence[src].getSurface()] for src in chunk.srcs if sentence[src].isContainPostposition()]] for sentence in sentences for chunk in sentence if chunk.srcs and chunk.isContainVerb()]
    pairs = [[pair[0], sorted(pair[1])] for pair in pairs if pair[1]]
    pairs = [[pair[0], [p[0] for p in pair[1]], [p[1] for p in pair[1]]] for pair in pairs]
    for pair in pairs:
        print("\t".join([pair[0], " ".join(pair[1]), " ".join(pair[2])]))
