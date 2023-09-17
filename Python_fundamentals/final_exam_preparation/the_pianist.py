n = int(input())

the_list = {}

for el in range(n):
    piece, composer, key = input().split("|")
    the_list[composer] = [piece, key]

while True:
    line_input = input()
    if line_input == "Stop":
        break

    command_line = line_input.split("|")
    command = command_line[0]
    piece_input = command_line[1]

    if command == "Add":
        composer_input = command_line[2]
        if composer_input in the_list:
            the_list[composer_input] += command_line[1]
        else:
            the_list[composer_input] = [command_line[1], command_line[3]]

    elif command == "Remove":
        pass

    elif command == "ChangeKey":
        pass
