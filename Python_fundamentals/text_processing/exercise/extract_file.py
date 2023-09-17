directory = input().split("\\")

group = directory[-1]
file, extension = group.split(".")

print(f"File name: {file}")
print(f"File extension: {extension}")
