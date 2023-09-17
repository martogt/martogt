phonebook = {}

n = 0
while True:
    line = input()
    parts = line.split("-")
    if len(parts) == 1:
        n = int(line)
        break

    name = parts[0]
    number = parts[1]

    phonebook[name] = number

for _ in range(n):
    search_name = input()
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
