# from collections import deque
#
# client = input()
# shop_queue = deque()
# shop_queue.append(client)
#
# while client != "End":
#     client = input()
#
#     if client != "Paid":
#         if client != "End":
#             shop_queue.append(client)
#     else:
#         for _ in range(len(shop_queue)):
#             print(shop_queue.popleft())
#
# print(f"{len(shop_queue)} people remaining.")

from collections import deque

shop_queue = deque()

while True:
    client = input()

    if client == "End":
        break

    if client == "Paid":
        while shop_queue:
            print(shop_queue.popleft())
    else:
        shop_queue.append(client)

print(f"{len(shop_queue)} people remaining.")
