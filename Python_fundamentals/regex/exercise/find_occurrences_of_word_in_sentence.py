import re

text = input().lower()
word = input().lower()

matches = re.findall(rf"\b{word}\b", text)

print(len(matches))
