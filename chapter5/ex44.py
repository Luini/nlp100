from myCabocha import Morph
from myCabocha import Chunk
from ex41 import formatter
import pydot_ng as pydot
import sys

def makeGraph(sentence, outputFileName):
    g = pydot.Dot(graph_type='digraph')
#    g.add_node(pydot.Node())
    chunkPairs = [(chunk.getSurface(), sentence[chunk.dst].getSurface()) for chunk in sentence if chunk.dst >= 0 and not chunk.isSymbol()]
    for chunkPair in chunkPairs:
        g.add_edge(pydot.Edge(chunkPair[0], chunkPair[1]))
    g.write_png(outputFileName)

if __name__ == "__main__":
    sentences = formatter("neko.txt.cabocha")
#    makeGraph(sentences[7], "output_ex44.png")


    line = int(sys.argv[1]) - 1

    print("===== Sentence =====")
    for chunk in sentences[line]:
        print(chunk)
    '''
    print([chunk.getSurface() for chunk in sentences[line]])
    '''

    makeGraph(sentences[line], sys.argv[2])
