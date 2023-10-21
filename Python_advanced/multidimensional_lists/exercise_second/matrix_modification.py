matrix_size = int(input())
matrix = [[int(rows) for rows in input().split()] for cols in range(matrix_size)]

command = input()

while command != "END":
    input_command = command.split()

    row = int(input_command[1])
    col = int(input_command[2])
    value = int(input_command[3])

    if row < 0 or row >= matrix_size or col < 0 or col >= matrix_size:
        print("Invalid coordinates")

    elif input_command[0] == "Add":
        matrix[row][col] += value

    elif input_command[0] == "Subtract":
        matrix[row][col] -= value

    command = input()

for el in matrix:
    print(*el)
