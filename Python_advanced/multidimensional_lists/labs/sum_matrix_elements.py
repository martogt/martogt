row, col = input().split(', ')

matrix = []
total = 0

for r in range(int(row)):
    matrix.append([])
    value = input().split(', ')
    for r_value in range(len(value)):
        matrix[r].append(int(value[r_value]))

for el in matrix:
    result = sum(el)
    total += result

print(total)
print(matrix)
