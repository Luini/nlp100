'''
コーパス中で頻出する述語と格パターンの組み合わせ
$ sort output_ex45.txt | uniq -c | sort -r | less
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
$ grep "^する\t" output_ex45.txt | sort | uniq -c | sort -r | less
$ grep "^見る\t" output_ex45.txt | sort | uniq -c | sort -r | less
$ grep "^与える\t" output_ex45.txt | sort | uniq -c | sort -r | less
'''
from myCabocha import Morph
from myCabocha import Chunk
from ex41 import formatter

if __name__ == "__main__":
    sentences = formatter("neko.txt.cabocha")
    pairs = [[chunk.getPredicate(), [sentence[src].getPostposition() for src in chunk.srcs if sentence[src].isContainPostposition()]] for sentence in sentences for chunk in sentence if chunk.srcs and chunk.isContainVerb()]
    pairs = [[pair[0], sorted(pair[1])] for pair in pairs if pair[1]]
    for pair in pairs:
        print("\t".join([pair[0], " ".join(pair[1])]))
