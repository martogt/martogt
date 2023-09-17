resources = {}

while True:
    line_input = input()
    if line_input == "stop":
        break

    quantity = int(input())
    if line_input in resources:
        resources[line_input] += quantity
    else:
        resources[line_input] = quantity

for name in resources:
    print(f"{name} -> {resources[name]}")
