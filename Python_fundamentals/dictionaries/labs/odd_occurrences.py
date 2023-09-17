languages = input().lower().split()
dictionary = dict.fromkeys(languages, 0)
output = []

for word in languages:
    if word in dictionary:
        dictionary[word] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        output.append(key)

print(" ".join(output))
