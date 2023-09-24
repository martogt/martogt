rows, cols = (int(x) for x in input().split(', '))
matrix = []

max_sum_matrix = []
max_sum_el = []

for el in range(rows):
    matrix.append([int(i) for i in input().split(', ')])

for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        current_el = matrix[row_idx][col_idx]
        next_el = matrix[row_idx][col_idx + 1]
        bottom_el = matrix[row_idx + 1][col_idx]
        diagonal_el = matrix[row_idx + 1][col_idx + 1]

        sum_el = current_el + next_el + bottom_el + diagonal_el

        max_sum = float('-inf')

        if max_sum < sum_el:
            max_sum_el = sum_el
            max_sum_matrix = [[current_el, next_el], [bottom_el, diagonal_el]]

print(matrix[0])
print(matrix[1])
print(max_sum_matrix)
