def check_if(c_row, c_col, m_row, m_col):
    if matrix[c_row][c_col] > 0:
        matrix[c_row][c_col] -= matrix[m_row][m_col]


matrix = []
lines = int(input())
upper_flag = False
lower_flag = False
left_flag = False
right_flag = False
for _ in range(lines):
    matrix.append(list(int(x) for x in input().split()))
commands = input().split()
for command in commands:
    row, col = list(int(x) for x in command.split(','))
    if matrix[row][col] > 0:
        if row == 0:
            upper_flag = True
        elif row == lines - 1:
            lower_flag = True
        if col == 0:
            left_flag = True
        elif col == lines - 1:
            right_flag = True

        if upper_flag:
            upper_flag = False
            check_if(row + 1, col, row, col)
            if left_flag:
                left_flag = False
                check_if(row, col + 1, row, col)
                check_if(row + 1, col + 1, row, col)
                matrix[row][col] = 0
            elif right_flag:
                right_flag = False
                check_if(row, col - 1, row, col)
                check_if(row + 1, col - 1, row, col)
                matrix[row][col] = 0
            else:
                check_if(row, col + 1, row, col)
                check_if(row + 1, col + 1, row, col)
                check_if(row, col - 1, row, col)
                check_if(row + 1, col - 1, row, col)
                matrix[row][col] = 0
            continue
        elif lower_flag:
            lower_flag = False
            check_if(row - 1, col, row, col)
            if left_flag:
                left_flag = False
                check_if(row - 1, col + 1, row, col)
                check_if(row, col + 1, row, col)
                matrix[row][col] = 0
            elif right_flag:
                right_flag = False
                check_if(row - 1, col - 1, row, col)
                check_if(row, col - 1, row, col)
                matrix[row][col] = 0
            else:
                check_if(row - 1, col + 1, row, col)
                check_if(row, col + 1, row, col)
                check_if(row - 1, col - 1, row, col)
                check_if(row, col - 1, row, col)
                matrix[row][col] = 0
            continue
        if left_flag:
            left_flag = False
            check_if(row - 1, col, row, col)
            check_if(row - 1, col + 1, row, col)
            check_if(row, col + 1, row, col)
            check_if(row + 1, col + 1, row, col)
            check_if(row + 1, col, row, col)
            matrix[row][col] = 0
        elif right_flag:
            right_flag = False
            check_if(row - 1, col, row, col)
            check_if(row - 1, col - 1, row, col)
            check_if(row, col - 1, row, col)
            check_if(row + 1, col - 1, row, col)
            check_if(row + 1, col, row, col)
            matrix[row][col] = 0
        else:
            check_if(row - 1, col - 1, row, col)
            check_if(row - 1, col, row, col)
            check_if(row - 1, col + 1, row, col)
            check_if(row, col + 1, row, col)
            check_if(row + 1, col + 1, row, col)
            check_if(row + 1, col, row, col)
            check_if(row + 1, col - 1, row, col)
            check_if(row, col - 1, row, col)
            matrix[row][col] = 0

counter = 0
sums = 0
for row in matrix:
    for value in row:
        if value > 0:
            sums += value
            counter += 1

print(f"Alive cells: {counter}")
print(f"Sum: {sums}")
for row in matrix:
    print(' '.join(list(str(x) for x in row)))