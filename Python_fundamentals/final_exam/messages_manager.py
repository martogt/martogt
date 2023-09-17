messages_capacity = int(input())

users_info = {}

while True:
    line_input = input()
    if line_input == "Statistics":
        break

    command_input = line_input.split("=")
    command = command_input[0]

    if command == "Add":

        username = command_input[1]
        sent = int(command_input[2])
        received = int(command_input[3])

        if username in users_info:
            continue

        users_info[username] = [sent, received]

    elif command == "Message":
        sender = command_input[1]
        receiver = command_input[2]

        if sender in users_info and receiver in users_info:
            users_info[sender][0] += 1
            users_info[receiver][1] += 1

            if (users_info[sender][0] + users_info[sender][1]) >= messages_capacity:
                print(f"{sender} reached the capacity!")
                del users_info[sender]
            if (users_info[receiver][0] + users_info[receiver][1]) >= messages_capacity:
                print(f"{receiver} reached the capacity!")
                del users_info[receiver]

    elif command == "Empty":
        username = command_input[1]

        if username in users_info:
            del users_info[username]

        if username == "All":
            users_info.clear()

print(f"Users count: {len(users_info)}")

for user in users_info:
    print(f"{user} - {sum(users_info[user])}")
