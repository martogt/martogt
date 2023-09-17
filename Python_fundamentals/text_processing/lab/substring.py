line1_input = input()
line2_input = input()
result = line2_input

for rep in range(len(line1_input)):
    result = result.replace(line1_input, "")

print(result)
