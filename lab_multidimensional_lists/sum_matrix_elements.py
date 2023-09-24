rows, col = [int(x) for x in input().split(", ")]

matrix = [[int(j) for j in input().split(", ")] for _ in range(rows)]
sum_matrix = 0

print(sum([sum(i) for i in matrix]))
print(matrix)
