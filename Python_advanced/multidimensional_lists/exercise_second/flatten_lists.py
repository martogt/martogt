data = input()
rows = data.split("|")
matrix = []

for row in rows:
    row_values = [int(value) for value in row.split()]
    matrix.append(row_values)

matrix = matrix[::-1]

matrix = [element for row in matrix for element in row]

print(*matrix)
