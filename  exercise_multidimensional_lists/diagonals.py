rows = int(input())

matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]

primary_diagonal = [matrix[i][i] for i in range(rows)]
sum_primary_diagonal = sum(primary_diagonal)

secondary_diagonal = [matrix[j][rows - j - 1] for j in range(rows)]
sum_secondary_diagonal = sum(secondary_diagonal)

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum_primary_diagonal}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum_secondary_diagonal}")
