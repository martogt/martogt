import math

n = int(input())

names_set = set()
odd_set = set()
even_set = set()

for index in range(n):
    names = input()
    names_sum = (math.floor(sum([ord(el) for el in names]) / (index + 1)))

    if names_sum % 2 == 0:
        even_set.add(names_sum)
    else:
        odd_set.add(names_sum)

if sum(odd_set) == sum(even_set):
    unions = odd_set | even_set
    names_set = unions
if sum(odd_set) > sum(even_set):
    differences = odd_set - even_set
    names_set = differences
if sum(odd_set) < sum(even_set):
    sym_differences = even_set ^ odd_set
    names_set = sym_differences

result = [str(el) for el in names_set]
print(", ".join(result))
