str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

list = str.split(" ")
list = map(lambda x: x.replace(",", "").replace(".", ""), list)
list = map(lambda x: len(x), list)

print(list)
