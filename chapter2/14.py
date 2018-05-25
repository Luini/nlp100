# diff <(python3 14.py 5) <(head -n 5 hightemp.txt)
import sys

N = int(sys.argv[1])

input = open("hightemp.txt", "r")

line = input.readline()
for i in range(N):
    if line:
        print(line, end='')
        line = input.readline()
    else:
        break

input.close()
