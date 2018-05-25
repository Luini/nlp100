# diff <(python3 15.py 3) <(tail -n 3 hightemp.txt)
import sys

N = int(sys.argv[1])

input = open("hightemp.txt", "r")
lines = input.readlines()
input.close()

lineCount = len(lines)

if N > lineCount:
    N = lineCount

for i in range(lineCount-N, lineCount):
    print(lines[i], end='')
