import re

text = input()
matches = re.findall(r"\b_([A-Za-z]+)\b", text)

print(*matches, sep=",")
