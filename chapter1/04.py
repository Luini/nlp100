string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

list = string.split(" ")
list = map(lambda x: x.replace(",", "").replace(".", ""), list)

flag = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dic = {}
for i, s in enumerate(list):
    if i+1 in flag:
        n = 1
    else:
        n = 2

    dic[s[0:n]] = i+1


print(dic)
