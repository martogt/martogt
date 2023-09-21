n = int(input())

unic_elements = set()

for _ in range(n):
    elements = input().split()

    for el in elements:
        unic_elements.add(el)

for el in unic_elements:
    print(el)
