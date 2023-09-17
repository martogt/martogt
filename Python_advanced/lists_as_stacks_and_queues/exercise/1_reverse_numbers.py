numbers = ([int(x) for x in input().split()])
stack = []

for _ in range(len(numbers)):
    stack.append(numbers.pop())

for elements in stack:
    print(elements, end=" ")
