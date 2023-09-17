in_stock = [el for el in input().split()]
stock = {}

for idx in range(0, len(in_stock), 2):
    key = in_stock[idx]
    value = in_stock[idx + 1]
    stock[key] = int(value)

are_in_stock = input().split()

for product in are_in_stock:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
