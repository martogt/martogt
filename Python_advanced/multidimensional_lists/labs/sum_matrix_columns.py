# rows = i
# columns = j

rows, cols = input().split(', ')

matrix = []

total = 0
index_j = 0

for i in range(int(rows)):
    matrix.append([int(j) for j in input().split()])

for _ in range(int(cols)):
    for i in range(int(rows)):
        total += matrix[i][index_j]

    print(total)
    total = 0
    index_j += 1
