while True:
    word = input()
    if word == "end":
        break
    result = word[::-1]

    print(f"{word} = {result}")
