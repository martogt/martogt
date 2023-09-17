import re

webs = []

while True:
    text = input()
    if not text:
        break

    matches = re.findall(r"(\bwww\.[a-zA-Z\d\-]+(\.[a-z]+)+)", text)
    webs.extend([m[0] for m in matches])

for web in webs:
    print("".join(web))
