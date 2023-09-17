string_input = input()
new_string = ""
strength = 0
s = 0
idx = 0

while idx < len(string_input):
    element = string_input[idx]
    idx += 1

    if element == ">":
        strength = int(string_input[idx])

        if strength < 2:
            new_string += string_input[idx + 1]
        else:
            if string_input[idx + 1] == ">":
                strength += (strength - 1)
                s = strength
                new_string += string_input[idx + 1]

            else:
                new_string += string_input[idx + s]
        strength_explosion = int(string_input[idx])
        idx += 1
    else:
        new_string += element

print(new_string)
