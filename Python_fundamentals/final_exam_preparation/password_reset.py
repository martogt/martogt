password = input()

old_pass = ""
new_pass = ""

while True:
    line_input = input()
    if line_input == "Done":
        break
    command = line_input.split()

    if "TakeOdd" in command:
        for idx in range(len(password)):
            if idx % 2 != 0:
                new_pass += (password[idx])
        old_pass = new_pass
        print(new_pass)

    elif "Cut" in command[0]:
        index = int(command[1])
        length = int(command[2])
        new_pass = old_pass[:index] + old_pass[index + length:]
        old_pass = new_pass
        print(new_pass)

    elif "Substitute" in command[0]:
        if command[1] not in old_pass:
            print("Nothing to replace!")
        else:
            new_pass = new_pass.replace(command[1], command[2])
            old_pass = new_pass
            print(new_pass)

print(f"Your password is: {new_pass}")
