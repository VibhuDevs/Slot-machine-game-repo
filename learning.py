def strip(l, word):
    for item in l:
        n = []
        for item in l:
            if not(item==word):
                n.append(item.strip(word))
    return n
l = ["me", "word", "vibhu", "hu"]
print(strip(l, "hu"))
