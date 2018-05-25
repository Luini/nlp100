# wc -l hightemp.txt
import sys

input = open(sys.argv[1],'r')
lines = input.readlines()
input.close()

print(len(lines))
