square_matrix = int(input())

matrix = [[int(row) for row in input().split()] for col in range(square_matrix)]

primary_diagonal = [matrix[row][row] for row in range(square_matrix)]
primary_sum = sum(primary_diagonal)
secondary_diagonal = [matrix[row][square_matrix - 1 - row] for row in range(square_matrix)]
secondary_sum = sum(secondary_diagonal)

print(abs(primary_sum - secondary_sum))
