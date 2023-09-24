row = int(input())

matrix = [[int(j) for j in input().split(", ") if int(j) % 2 == 0] for i in range(row)]

print(matrix)
