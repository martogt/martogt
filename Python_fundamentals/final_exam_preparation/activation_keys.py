raw_key = input()

while True:
    line_input = input()
    if line_input == "Generate":
        break

    command_line = line_input.split(">>>")
    command = command_line[0]

    if command == "Contains":
        substring = command_line[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        start_index = int(command_line[2])
        end_index = int(command_line[3])

        if command_line[1] == "Upper":
            raw_key = raw_key[:start_index] + raw_key[start_index: end_index].upper() + raw_key[end_index:]
        elif command_line[1] == "Lower":
            raw_key = raw_key[:start_index] + raw_key[start_index: end_index].lower() + raw_key[end_index:]

        print(raw_key)

    elif command == "Slice":
        parameter_1 = int(command_line[1])
        parameter_2 = int(command_line[2])
        raw_key = raw_key[:parameter_1] + raw_key[parameter_2:]
        print(raw_key)

print(f"Your activation key is: {raw_key}")
