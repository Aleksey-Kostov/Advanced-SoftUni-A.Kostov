rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = float("-inf")
subs_matrix = []

for row in range(rows - 2):
    for column in range(columns - 2):
        if max_sum < (matrix[row][column] + matrix[row][column + 1] + matrix[row][column + 2] +
                      matrix[row + 1][column] + matrix[row + 1][column + 1] + matrix[row + 1][column + 2] +
                      matrix[row + 2][column] + matrix[row + 2][column + 1] + matrix[row + 2][column + 2]):
            max_sum = (matrix[row][column] + matrix[row][column + 1] + matrix[row][column + 2] +
                       matrix[row + 1][column] + matrix[row + 1][column + 1] + matrix[row + 1][column + 2] +
                       matrix[row + 2][column] + matrix[row + 2][column + 1] + matrix[row + 2][column + 2])
            subs_matrix = [matrix[row][column], matrix[row][column + 1], matrix[row][column + 2]], \
                [matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2]], \
                [matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]

print(f"Sum = {max_sum}")
for num in subs_matrix:
    print(*num, sep=' ')
