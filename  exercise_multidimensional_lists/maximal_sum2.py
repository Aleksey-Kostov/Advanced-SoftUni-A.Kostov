rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = float("-inf")
max_row = 0
max_column = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(column, column + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_column = column

print(f"Sum = {max_sum}")
subs_sabs_matrix = [matrix[r][max_column:max_column + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in subs_sabs_matrix]
