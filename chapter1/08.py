def cipher(string):
    output = ""
    for s in string:
        if ord("a") <= ord(s) and ord(s) <= ord("z"):
            output += chr(219 - ord(s))
        else:
            output += s
    return output


text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

print(cipher(text))
print(cipher(cipher(text)))
