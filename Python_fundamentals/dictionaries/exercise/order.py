products = {}
products_info = {}

while True:
    line_input = input()
    if line_input == "buy":
        break

    name, price, quantity = line_input.split()

    if name not in products_info:
        products_info[name] = int(quantity)
    else:
        products_info[name] += int(quantity)

    if name not in products:
        products[name] = float(price) * int(quantity)
    else:
        total_quantity = products_info[name]
        products[name] = total_quantity * float(price)

for product in products:
    print(f"{product} -> {products[product]:.2f}")
