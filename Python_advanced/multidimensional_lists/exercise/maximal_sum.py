rows, cols = (int(x) for x in input().split())

matrix = [[int(row) for row in input().split()] for col in range(cols)]

biggest_matrix = []
biggest_sum = []
result = 0

for row_index in range(rows - 2):

    for col_index in range(cols - 2):
        if result > sum(biggest_sum):
            continue

        first_left = matrix[row_index][col_index]
        second_left = matrix[row_index][col_index + 1]
        third_left = matrix[row_index][col_index + 2]
        firs_middle = matrix[row_index + 1][col_index]
        second_middle = matrix[row_index + 1][col_index + 1]
        third_middle = matrix[row_index + 1][col_index + 2]
        firs_bottom = matrix[row_index + 2][col_index]
        second_bottom = matrix[row_index + 2][col_index + 1]
        third_bottom = matrix[row_index + 2][col_index + 2]

        biggest_matrix.append([first_left, second_left, third_left])
        biggest_matrix.append([firs_middle, second_middle, third_middle])
        biggest_matrix.append([firs_bottom, second_bottom, third_bottom])

        for i in biggest_matrix:
            biggest_sum.append(sum(i))
            result += sum(biggest_sum)

        # biggest_matrix.clear()
