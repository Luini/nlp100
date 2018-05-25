import sys

def formatter(mecabFile):
    with open(mecabFile, 'r') as file:
        mecabList = []
        line = file.readline()
        while line:
            list = line.split("\t")
            if len(list) == 2:
                values = list[1].split(",")
                if values[6] == "*\n":
                    dic = {"surface":list[0], "base":list[0], "pos":values[0], "pos1":values[1]}
                else:
                    dic = {"surface":list[0], "base":values[6], "pos":values[0], "pos1":values[1]}
                mecabList.append(dic)
            line = file.readline()
    return mecabList

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python3 mecab.py [mecabFileName]")
    else:
        list = formatter(sys.argv[1])
        list = list[:20]
        for l in list:
            print(l)
