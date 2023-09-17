import re

total_price = 0
furnitures = []

while True:
    line_input = input()
    if line_input == "Purchase":
        break

    matches = re.findall(r"^>>(?P<Furniture>[a-zA-Z]+)<<(?P<Price>\d+\.?\d+)!(?P<Quantity>\d+)$", line_input)

    if not matches:
        continue

    group = matches[0]

    furniture = furnitures.append(group[0])
    price = float(group[1])
    quantity = int(group[2])

    total_price += quantity * price

print("Bought furniture:")
for item in furnitures:
    print(item)
print(f"Total money spend: {total_price:.2f}")
