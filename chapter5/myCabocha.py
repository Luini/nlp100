class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "[surface]{} [base]{} [pos]{} [pos1]{}".format(self.surface, self.base, self.pos, self.pos1)

    @classmethod
    def createFromCabochaLine(cls, line):
        list = line.split("\t")
        values = list[1].split(",")
        return cls(list[0], values[6], values[0], values[1])



class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        str = "--- Chunk [dst]{} [srcs]{} ---".format(self.dst, self.srcs)
        for m in self.morphs:
            str += "\n{}".format(m)
        return str

    def addMorph(self, morph):
        self.morphs.append(morph)

    def addSrc(self, src):
        self.srcs.append(src)

    def getSurface(self):
        surface = ""
        for m in self.morphs:
            if m.pos != "記号":
                surface += m.surface
        return surface

    def isSymbol(self):
        flag = True
        for m in self.morphs:
            flag = flag and m.pos == "記号"
        return flag

    def isContain(self, pos):
        flag = False
        for m in self.morphs:
            flag = flag or m.pos == pos
        return flag

    def isContainNoun(self):
        return self.isContain("名詞")

    def isContainVerb(self):
        return self.isContain("動詞")

    def isContainPostposition(self):
        return self.isContain("助詞")

    def getFirstBase(self, pos):
        for m in self.morphs:
            if m.pos == pos:
                return m.base
        return None

    def getPredicate(self):
        return self.getFirstBase("動詞")

    def getPostposition(self):
        return self.getFirstBase("助詞")

    def getNoun(self):
        return self.getFirstBase("名詞")

    def isSahenWo(self):
        if len(self.morphs) == 2 and self.morphs[0].pos == "名詞" and self.morphs[0].pos1 == "サ変接続" and self.morphs[1].surface == "を":
            return True
        else:
            return False

    def replaceNoun(self, str):
        if self.isContainNoun():
            return self.getSurface().replace(self.getNoun(), str)
        else:
            return self.getSurface()

    @classmethod
    def createFromCabochaLine(cls, line):
        list = line.split()
        dst = list[2][:-1] # 最後の一文字を除く
        dst = int(dst)
        return cls([], dst, [])
