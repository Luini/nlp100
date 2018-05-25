from myCabocha import Morph
from myCabocha import Chunk
from ex41 import formatter
from ex48 import makePaths

def getCommonPartIndex(l, l2):
    for i, value in enumerate(l2):
        if value in l:
            return [l.index(value), i]
    return None

if __name__ == "__main__":
    sentences = formatter("neko.txt.cabocha")
    sentence = sentences[7]

    paths = makePaths(sentence)
    pathPairs = [(path, path2) for i, path in enumerate(paths) for path2 in paths[i+1:]]
    for path, path2 in pathPairs:
        if path2[0] in path:
            path = path[:path.index(path2[0])+1]
            path = [chunk.getSurface() if index != 0 and index != len(path)-1 else chunk.replaceNoun("X") if index == 0 else chunk.replaceNoun("Y") for index, chunk in enumerate(path)]
            print(" -> ".join(path))
        else:
            commonPartIndex = getCommonPartIndex(path, path2)
            if commonPartIndex:
                result = [path[:commonPartIndex[0]], path2[:commonPartIndex[1]], path[commonPartIndex[0]:commonPartIndex[0]+1]]
                result[0] = [chunk.replaceNoun("X") if index == 0 else chunk.getSurface() for index, chunk in enumerate(result[0])]
                result[1] = [chunk.replaceNoun("Y") if index == 0 else chunk.getSurface() for index, chunk in enumerate(result[1])]
                result[2] = [chunk.getSurface() for chunk in result[2]]
                print(" | ".join([" -> ".join(chunkSurfaces) for chunkSurfaces in result]))
            else:
                print("None!")
