text = input().replace(" ", "")

chars = {}

for el in range(len(text)):
    char = text[el]
    if char not in chars:
        chars[char] = 1
    else:
        chars[char] += 1

for idx in chars:
    print(f"{idx} -> {chars[idx]}")
