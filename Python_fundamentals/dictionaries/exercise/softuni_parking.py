num_of_users = int(input())

entrance_info = {}

for _ in range(num_of_users):
    line_input = input().split()
    name = line_input[1]

    if line_input[0] == "register":
        if name in entrance_info:
            print(f"ERROR: already registered with plate number {line_input[2]}")
        else:
            entrance_info[name] = line_input[2]
            print(f"{name} registered {entrance_info[name]} successfully")
    elif line_input[0] == "unregister":
        if name in entrance_info:
            del entrance_info[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name in entrance_info:
    print(f"{name} => {entrance_info[name]}")
