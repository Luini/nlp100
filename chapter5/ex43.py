from myCabocha import Morph
from myCabocha import Chunk
from ex41 import formatter

if __name__ == "__main__":
    sentences = formatter("neko.txt.cabocha")

    chunkPairs = [[chunk.getSurface(), sentence[chunk.dst].getSurface()] for sentence in sentences for chunk in sentence if chunk.dst >= 0 and not chunk.isSymbol() and chunk.isContainNoun() and sentence[chunk.dst].isContainVerb()]

    for chunkPair in chunkPairs:
        print("\t".join(chunkPair))
