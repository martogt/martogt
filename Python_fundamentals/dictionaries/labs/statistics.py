command = input()
stock = {}

while command != "statistics":
    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])

    if product not in stock:
        stock[product] = 0
    stock[product] += quantity

    command = input()

print("Products in stock:")

for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
