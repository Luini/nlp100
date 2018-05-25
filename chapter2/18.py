# sort -k 3,3 -t "\t" hightemp.txt
input = open("hightemp.txt", "r")
lines = input.readlines()
input.close()

lines = list(map(lambda x: x.split("\t"), lines))
lines.sort(key=lambda x: -float(x[2]))

for line in lines:
    print("\t".join(line), end="")
