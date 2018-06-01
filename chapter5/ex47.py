'''
コーパス中で頻出する述語（サ変接続名詞+を+動詞）
$ cut -f 1 output_ex47.txt | sort | uniq -c | sort -r | less
コーパス中で頻出する述語と助詞パターン
$ cut -f 1,2 output_ex47.txt | sort | uniq -c | sort -r | less
'''
from myCabocha import Morph
from myCabocha import Chunk
from ex41 import formatter

if __name__ == "__main__":
    sentences = formatter("neko.txt.cabocha")
    pairs = [
        [sentence, vChunk, [sentence[src] for src in vChunk.srcs if sentence[src].isSahenWo()]]
        for sentence in sentences for vChunk in sentence
        if vChunk.srcs and vChunk.isContainVerb()
    ]
    pairs = [pair[:2] + [sahenWo] for pair in pairs if pair[2] for sahenWo in pair[2]]
    pairs = [
        [sahenWo.getSurface() + vChunk.getPredicate(), [[sentence[src].getPostposition(), sentence[src].getSurface()] for src in sahenWo.srcs if sentence[src].isContainPostposition()]]
        for [sentence, vChunk, sahenWo] in pairs
        if sahenWo.srcs
    ]
    pairs = [[pair[0], sorted(pair[1])] for pair in pairs if pair[1]]
    pairs = [[pair[0], [p[0] for p in pair[1]], [p[1] for p in pair[1]]] for pair in pairs]
    for pair in pairs:
        print("\t".join([pair[0], " ".join(pair[1]), " ".join(pair[2])]))
