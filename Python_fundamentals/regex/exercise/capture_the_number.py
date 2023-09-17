import re

result = []
while True:
    line_input = input()
    if not line_input:
        break

    matches = re.findall(r"(\d+)", line_input)
    result.extend(matches)

print(*result, sep=" ")
