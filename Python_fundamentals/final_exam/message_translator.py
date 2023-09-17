import re

n = int(input())
result = []

final_message = []

for _ in range(n):
    text = input()

    matches = re.findall(r"![A-Z][a-z]{3,}!|\[[A-Za-z]{8,}\]", text)

    if matches:
        result = matches
        if len(matches) < 2:
            print("The message is invalid")
            continue
        command = result[0][1:-1]
        message = result[1][1:-1]

        for el in message:
            decoded_message = ord(el)
            final_message.append(decoded_message)
        print(f"{result[0][1:-1]}: {' '.join(str(n) for n in final_message)}")
    else:
        print("The message is invalid")
