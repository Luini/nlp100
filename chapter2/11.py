# expand -t 1 hightemp.txt
import sys

input = open(sys.argv[1],'r')
text = input.read()
input.close()

text = text.replace("\t", " ")

print(text, end='')
