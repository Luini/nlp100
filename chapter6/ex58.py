import nlp

if __name__ == "__main__":
    coreNLP = nlp.CoreNLP("nlp.txt.xml")
    dependencies = coreNLP.getDependencies()
    results = []
    for deps in dependencies:
        nsubjs = [dep for dep in deps if dep.type == "nsubj"]
        dobjs = [dep for dep in deps if dep.type == "dobj"]
        for nsubj in nsubjs:
            results += [
                (nsubj.dependentText, nsubj.governorText, dobj.dependentText)
                for dobj in dobjs
                if nsubj.governorText == dobj.governorText
            ]

    print("\n".join(["\t".join(result) for result in results]))
