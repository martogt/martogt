squad_matrix = int(input())

matrix = [[int(row) for row in input().split(', ')] for col in range(squad_matrix)]

# Calculate the primary diagonal
primary_diagonal = [matrix[i][i] for i in range(squad_matrix)]
primary_sum = sum(primary_diagonal)

# Calculate the secondary diagonal
secondary_diagonal = [matrix[i][squad_matrix - 1 - i] for i in range(squad_matrix)]
secondary_sum = sum(secondary_diagonal)

# Print the results
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {secondary_sum}")
