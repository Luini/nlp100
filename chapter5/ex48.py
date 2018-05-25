from myCabocha import Morph
from myCabocha import Chunk
from ex41 import formatter

def makePaths(sentence):
    paths = []
    for chunk in sentence:
        if chunk.isContainNoun():
            path = [chunk]
            while chunk.dst >= 0:
                chunk = sentence[chunk.dst]
                path.append(chunk)
            paths.append(path)
    return paths

if __name__ == "__main__":
    sentences = formatter("neko.txt.cabocha")
    paths = makePaths(sentences[7])
    for path in paths:
        print(" -> ".join([chunk.getSurface() for chunk in path]))
