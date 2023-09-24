square_matrix = int(input())

matrix = []
flattened_matrix = ''
result = ()

for row in range(square_matrix):
    matrix_input = input()
    matrix.append(matrix_input)

symbol = input()

for row_idx, row in enumerate(matrix):
    for col_idx, char in enumerate(row):
        flattened_matrix += char
        if char == symbol:
            result = (row_idx, col_idx)

if symbol in flattened_matrix:
    print(result)
else:
    print(f'{symbol} does not occur in the matrix')
