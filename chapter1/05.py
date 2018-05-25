def ngram(text, n):
    result = []
    for i in range(len(text) - n + 1):
        result.append(text[i:i+n])
    return result

text = "I am an NLPer"

print(ngram(text.split(" "), 3))
print(ngram(text, 3))
