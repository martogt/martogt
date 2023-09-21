n = int(input())

usernames = set()

for _ in range(n):
    user = input()
    usernames.add(user)

for name in usernames:
    print(name)
