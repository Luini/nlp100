# diff <(sort col1.txt | uniq) <(python3 17.py | sort)
input = open("col1.txt", "r")
lines = input.readlines()
input.close()

lines = map(lambda x: x.replace("\n", ""), lines)
strs = set(lines)

for str in strs:
    print(str)
