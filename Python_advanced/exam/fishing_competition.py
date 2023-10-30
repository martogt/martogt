def find_starting_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'S':
                return row, col


def is_inside_matrix(row, col, n):
    return 0 <= row < n and 0 <= col < n


n = int(input())
matrix = [list(input()) for _ in range(n)]
move_commands = input().split()

fish_caught = 0
row, col = find_starting_position(matrix)

for command in move_commands:
    matrix[row][col] = '-'
    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    if not is_inside_matrix(row, col, n):
        if row < 0:
            row = n - 1
        elif row >= n:
            row = 0
        elif col < 0:
            col = n - 1
        elif col >= n:
            col = 0

    if matrix[row][col] == '-':
        continue
    elif matrix[row][col] == 'W':
        result = "You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{} ,{}]".format(
            row, col)
        break
    else:
        fish_caught += int(matrix[row][col])
        matrix[row][col] = '-'

    if fish_caught >= 20:
        result = "Success! You managed to reach the quota!"
        break

if fish_caught < 20:
    result = "You didn't catch enough fish and didn't reach the quota!\nYou need {} tons of fish more.".format(
        20 - fish_caught)
else:
    result = "Amount of fish caught: {} tons.".format(fish_caught)

print(result)
if "Amount of fish caught" not in result:
    for row in matrix:
        print(''.join(row))
