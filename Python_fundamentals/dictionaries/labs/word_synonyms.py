n_inputs = int(input())

synonyms = {}

for el in range(n_inputs):
    key = input()
    value = input()

    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(value)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
