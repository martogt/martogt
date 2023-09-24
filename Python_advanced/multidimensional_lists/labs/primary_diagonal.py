square_matrix = int(input())

matrix = []
matrix_index = 0
diagonal_sum = 0

for i in range(square_matrix):
    matrix.append([int(j) for j in input().split()])

for el in range(square_matrix):
    diagonal_sum += matrix[el][matrix_index]
    matrix_index += 1

print(diagonal_sum)
