n = int(input())
stack = []

for _ in range(n):
    input_values = [int(x) for x in input().split()]
    command = int(input_values[0])

    if input_values[0] == 1:
        number = int(input_values[1])

        if command == 1:
            stack.append(number)

    if stack:
        if command == 2:
            stack.pop()
        elif command == 3:
            print(max(stack))
        elif command == 4:
            print(min(stack))

while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")
