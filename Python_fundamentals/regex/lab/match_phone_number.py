import re

pattern = r"\+359 2 \d{3,} \d{4}\b|\+359-2-\d{3,}-\d{4}\b"
number = input()
result = re.findall(pattern, number)

print(", ".join(result))
