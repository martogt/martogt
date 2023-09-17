from collections import deque

food_quantity = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))

while orders and food_quantity >= orders[0]:
    food_quantity -= orders.popleft()
    if not orders:
        print("Orders complete")
if orders and food_quantity < orders[0]:
    print('Orders left: ', end="")

for order in orders:
    print(order, end=" ")
