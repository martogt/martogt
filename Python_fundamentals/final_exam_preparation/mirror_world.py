import re

matches_list = []
final_list = []

text = input()
matches = re.findall(r"@([A-Za-z]{3,})@@([A-Za-z]{3,})@|#([A-Za-z]{3,})##([A-Za-z]{3,})#", text)

for word in matches:
    for el in word:
        if el != "":
            matches_list.append(el)

for word in matches_list:
    inverted_word = word[-1::-1]
    if inverted_word in matches_list:
        final_list.append(word + " " + "<=>" + " " + inverted_word)
        matches_list.remove(word)
        matches_list.remove(inverted_word)

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if not final_list:
    print("No mirror words!")
else:
    print(f"The mirror words are:\n{', '.join(final_list)}")
