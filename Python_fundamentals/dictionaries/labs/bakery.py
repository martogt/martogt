line_input = input().split()
dict_list = {}

for idx in range(0, len(line_input), 2):
    key = line_input[idx]
    value = line_input[idx + 1]
    dict_list[key] = int(value)

print(dict_list)
