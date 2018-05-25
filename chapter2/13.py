# diff <(python3 13.py) <(paste col1.txt col2.txt)
input1 = open("col1.txt", "r")
input2 = open("col2.txt", "r")
col1 = input1.readline()
col2 = input2.readline()

output = open("13_output.txt", "w")
while col1:
    col1 = col1.replace("\n", "")
    output.write(col1 + "\t" +col2)
    col1 = input1.readline()
    col2 = input2.readline()

input1.close()
input2.close()
