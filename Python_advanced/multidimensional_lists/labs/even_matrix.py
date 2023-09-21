num_rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(num_rows)]
even_matrix = [[num for num in row if num % 2 == 0] for row in matrix]

print(even_matrix)
