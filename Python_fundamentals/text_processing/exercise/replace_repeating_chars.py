line_input = input()

result = ""

for el in range(-len(line_input), -1):
    if line_input[el] == line_input[el + 1]:
        pass
    else:
        result += line_input[el]

final_symbol = line_input[len(line_input) - 1]
print(result + final_symbol)
