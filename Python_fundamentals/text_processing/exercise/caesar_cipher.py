line_input = input()

encrypted_text = ""

for el in range(0, len(line_input)):
    encrypted_char = ord(line_input[el])
    encrypted_text += chr(encrypted_char + 3)

print(encrypted_text)
