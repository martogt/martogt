import re

coolest = {}

text = input()

matches = re.findall(r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*", text)
cool_threshold = re.findall(r"[0-9]", text)

cool = 0
threshold = 1

for el in cool_threshold:
    threshold *= int(el)

for match in matches:
    word = match[2:-2]
    for el in range(len(word)):
        cool += int(ord(word[el]))
        coolest[match] = cool
    cool = 0

print(f"Cool threshold: {threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for key in coolest:
    if coolest[key] > threshold:
        print(key)
