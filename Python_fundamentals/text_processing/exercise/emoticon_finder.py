line_input = input()

for el in range(len(line_input)):
    if line_input[el] == ":":
        print(line_input[el] + line_input[el + 1])
