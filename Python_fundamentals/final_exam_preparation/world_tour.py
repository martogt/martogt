def is_valid_idx(idx, text):
    return 0 <= idx < len(text)


travel = input()

while True:
    line_input = input()
    if line_input == "Travel":
        break

    command = line_input.split(":")

    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]

        if is_valid_idx(index, travel):
            travel = travel[:index] + string + travel[index:]

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])

        if is_valid_idx(start_index, travel) and is_valid_idx(end_index, travel):
            travel = travel[:start_index] + travel[end_index + 1:]

    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        travel = travel.replace(old_string, new_string)

    print(travel)

print(f"Ready for world tour! Planned stops: {travel}")
