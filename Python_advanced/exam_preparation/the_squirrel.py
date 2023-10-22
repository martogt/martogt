# def is_in_area(row, col, matrix_size):
#     return 0 <= row < matrix_size and 0 <= col < matrix_size
#
#
# field_size = int(input())
#
# hazelnuts = 0
#
# move_command = input().split(", ")
# # move = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}
#
# field = []
# current_row, current_col = 0, 0
#
# for row in range(field_size):
#     field.append(input())
#     for col in range(field_size):
#         if field[row][col] == "s":
#             current_row, current_col = row, col
#
# for command in move_command:
#     if hazelnuts < 3:
#         if command == "left":
#             if is_in_area(current_row, current_col - 1, field_size):
#                 current_row += 1
#                 field[current_row][current_col] += "s"
#         elif command == "right":
#             pass
#         elif command == "down":
#             pass
#         elif command == "up":
#             pass
#     else:
#         print("Good job! You have collected all hazelnuts!")

def is_valid_move(x, y, field_size):
    return 0 <= x < field_size and 0 <= y < field_size


def play_game(field_size, moves, field):
    squirrel_position = None
    hazelnuts = 0
    traps = 0

    # Find initial squirrel position and count hazelnuts and traps
    for x in range(field_size):
        for y in range(field_size):
            if field[x][y] == 's':
                squirrel_position = (x, y)
            elif field[x][y] == 'h':
                hazelnuts += 1
            elif field[x][y] == 't':
                traps += 1

    for move in moves:
        x, y = squirrel_position
        if move == 'left':
            y -= 1
        elif move == 'right':
            y += 1
        elif move == 'up':
            x -= 1
        elif move == 'down':
            x += 1

        if not is_valid_move(x, y, field_size):
            return "The squirrel is out of the field."

        if field[x][y] == 'h':
            hazelnuts -= 1
            if hazelnuts == 0:
                return "Good job! You have collected all hazelnuts."
            field[x] = field[x][:y] + '*' + field[x][y + 1:]

        if field[x][y] == 't':
            return "Unfortunately, the squirrel stepped on a trap."

        squirrel_position = (x, y)

    return "There are more hazelnuts to collect."


# Input
field_size = int(input())
moves = input().split(", ")
field = [input() for _ in range(field_size)]

# Game result
result = play_game(field_size, moves, field)
collected_hazelnuts = 3 if 'Good job' in result else 3 - field.count('h')
print(result)
print(f"Hazelnuts collected: {collected_hazelnuts}")
