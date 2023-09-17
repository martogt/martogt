concealed_message = input()

while True:
    line_input = input()
    if line_input == "Reveal":
        break

    splitted_commands = line_input.split(":|:")

    command = splitted_commands[0]

    if command == "InsertSpace":
        index = int(splitted_commands[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)

    elif command == "Reverse":
        substring = splitted_commands[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "")
            reversed_substring = substring[-1::-1]
            concealed_message += reversed_substring
            print(concealed_message)
        else:
            print("error")

    elif command == "ChangeAll":
        substring = splitted_commands[1]
        replacement = splitted_commands[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")
