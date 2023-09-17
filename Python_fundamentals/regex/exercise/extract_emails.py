import re

emails = []

emails_list = input()
matches = re.findall(r"\b([a-zA-Z0-9_\-\.]+)(@)([a-zA-Z0-9_\-\.]+)\b", emails_list)
emails.extend(matches)

for email in emails:
    print("".join(email), end="\n")
