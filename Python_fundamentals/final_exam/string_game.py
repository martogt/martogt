text = input()

while True:
    line_input = input()

    if line_input == "Done":
        break

    command_line = line_input.split()
    command = command_line[0]

    if command == "Change":
        char = command_line[1]
        replacement = command_line[2]
        text = text.replace(char, replacement)
        print(text)

    elif command == "Includes":
        substring = command_line[1]
        if substring in text:
            print("True")
        else:
            print("False")

    elif command == "End":
        substring_end = command_line[1]
        if text.endswith(substring_end):
            print("True")
        else:
            print("False")

    elif command == "Uppercase":
        text = text.upper()
        print(text)

    elif command == "FindIndex":
        char_find = command_line[1]
        print(text.find(char_find))

    elif command == "Cut":
        start_index = int(command_line[1])
        count = int(command_line[2])
        cut_text = text[start_index:start_index + count]
        print(cut_text)
