row, col = [int(x) for x in input().split(", ")]

matrix = [[int(j) for j in input().split(" ")] for i in range(row)]

sum_matrix = []

for j in range(col):
    current_matrix = 0
    for i in range(row):
        current_matrix += (int(matrix[i][j]))
    sum_matrix.append(current_matrix)

print([x for x in sum_matrix])
