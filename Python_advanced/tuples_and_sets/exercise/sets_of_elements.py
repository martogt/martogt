numbs = input().split()

n = set()
m = set()

for _ in range(int(numbs[0])):
    num = int(input())
    n.add(num)

for _ in range(int(numbs[1])):
    num = int(input())
    m.add(num)

result = set.intersection(n, m)

for el in result:
    print(el)
