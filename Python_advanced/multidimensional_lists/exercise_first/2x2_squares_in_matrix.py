rows, cols = (int(i) for i in input().split())

matrix = [[chars for chars in input().split()] for col in range(rows)]
counter = 0

for row_i in range(rows - 1):
    for col_i in range(cols - 1):
        current_el = matrix[row_i][col_i]
        next_el = matrix[row_i][col_i + 1]
        bottom_el = matrix[row_i + 1][col_i]
        diagonal_el = matrix[row_i + 1][col_i + 1]

        if current_el == next_el == bottom_el == diagonal_el:
            counter += 1

print(counter)
