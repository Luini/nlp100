# cut -f 1 hightemp.txt
# cut -f 2 hightemp.txt
import sys

input = open(sys.argv[1], "r")
col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")

line = input.readline()
while line:
    cols = line.split("\t")
    col1.write(cols[0] + "\n")
    col2.write(cols[1] + "\n")
    line = input.readline()

input.close()
col1.close()
col2.close()
