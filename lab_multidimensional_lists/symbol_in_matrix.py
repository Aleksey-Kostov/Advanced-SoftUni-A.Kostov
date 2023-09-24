row = int(input())

matrix = [[j for j in input()] for i in range(row)]
symbol = input()
find = False

for index_row in range(row):
    if find:
        break
    for index_col in range(len(matrix[index_row])):
        if matrix[index_row][index_col] == symbol:
            print((index_row, index_col))
            find = True
            break

if not find:
    print(f"{symbol} does not occur in the matrix")
