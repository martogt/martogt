n = int(input())
names_list = set()

for name in range(n):
    names = input()
    names_list.add(names)

for names in names_list:
    print(names)
