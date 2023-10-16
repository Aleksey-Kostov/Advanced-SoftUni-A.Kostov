def is_inside(rows, cols, first_row, first_col):
    return 0 <= rows < first_row and 0 <= cols < first_col


row, col = [int(x) for x in input().split(",")]

matrix = []
mouse_coord = []
cheese = []

for i in range(row):
    matrix.append([x for x in input()])
    for j in range(col):
        if matrix[i][j] == "M":
            mouse_coord = [i, j]
        if matrix[i][j] == "C":
            cheese.append((i, j))

mapper = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}

command = input()

while command != "danger":
    r = mouse_coord[0] + mapper[command][0]
    c = mouse_coord[1] + mapper[command][1]
    if not is_inside(r, c, row, col):
        print("No more cheese for tonight!")
        break
    matrix[mouse_coord[0]][mouse_coord[1]] = "*"
    mouse_coord = [r, c]
    if matrix[r][c] == "C":
        cheese.remove((r, c))
        matrix[r][c] = "*"
        if len(cheese) == 0:
            matrix[r][c] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[r][c] == "*":
        matrix[r][c] = "M"
        mouse_coord = [r, c]
    elif matrix[r][c] == "@":
        r = mouse_coord[0] - mapper[command][0]
        c = mouse_coord[1] - mapper[command][1]
        mouse_coord = [r, c]
    elif matrix[r][c] == "T":
        matrix[r][c] = "M"
        mouse_coord = [r, c]
        print("Mouse is trapped!")
        break
    command = input()
    if command == "danger":
        print("Mouse will come back later!")

[print("".join(row)) for row in matrix]
