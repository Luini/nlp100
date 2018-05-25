import random

def typoglycemia(text):
    textlist = text.split(" ")
    for i, li in enumerate(textlist):
        if len(li) > 4:
            textlist[i] = li[0] + "".join(random.sample(list(li[1:len(li)-1]), len(li)-2)) + li[len(li)-1]
    return " ".join(textlist)


text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(typoglycemia(text))
