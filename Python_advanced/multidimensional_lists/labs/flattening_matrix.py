rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
flattened_matrix = [el for row in matrix for el in row]
print(flattened_matrix)
