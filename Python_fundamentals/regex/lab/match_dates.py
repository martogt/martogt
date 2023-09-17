import re

pattern = r"\b(?P<Day>\d{2})([\./\-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
text = input()

date = re.findall(pattern, text)

print(f"{}")
