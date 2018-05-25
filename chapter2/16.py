import sys

N = int(sys.argv[1])

input = open(sys.argv[2], "r")
lines = input.readlines()
input.close()

lineCount = len(lines)
surplus = lineCount % N
ofset = 0

for i in range(N):
    fileName = "16_output_" + str(i) + ".txt"
    output = open(fileName, "w")

    nextOfset = ofset + int(lineCount/N)
    if i < surplus:
        nextOfset += 1
    outputLines = lines[ofset : nextOfset]
    ofset = nextOfset

    for line in outputLines:
        output.write(line)
    output.close()
