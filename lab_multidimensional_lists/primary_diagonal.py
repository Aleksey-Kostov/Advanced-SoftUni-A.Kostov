cow = int(input())

matrix = [[int(j) for j in input().split()] for i in range(cow)]

sum_diagonal = 0
for i in range(cow):
    sum_diagonal += matrix[i][i]

print(sum_diagonal)
