usernames = input().split(", ")

for name in usernames:
    if 3 < len(name) < 16:
        if name.isalnum():
            print(name)
        if "_" in name or "-" in name:
            print(name)
