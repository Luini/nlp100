# cut -f 1 hightemp.txt | sort | uniq -c | sort -r
input = open("col1.txt", "r")
lines = input.readlines()
input.close()

lines = map(lambda x: x.rstrip(), lines)

strs = {}
for s in lines:
    if s in strs.keys():
        strs[s] += 1
    else:
        strs[s] = 1

for s, n in sorted(strs.items(), key=lambda x: -x[1]):
    print(s + " " + str(n) + "回")
