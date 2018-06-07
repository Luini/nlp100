import nlp
import sys

if __name__ == "__main__":
    coreNLP = nlp.CoreNLP("nlp.txt.xml")
    coreNLP.createDigraph(int(sys.argv[1]), "output_ex57.png")
