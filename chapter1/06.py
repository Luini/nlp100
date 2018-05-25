def ngram(text, n):
    result = []
    for i in range(len(text) - n + 1):
        result.append(text[i:i+n])
    return result

textX = "paraparaparadise"
textY = "paragraph"

X = set(ngram(textX, 2))
Y = set(ngram(textY, 2))

print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X)
print("se" in Y)
