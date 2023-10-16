def is_inside(row, coll, first_row, first_col):
    return 0 <= row < first_row and 0 <= coll < first_col


rows, columns = [int(x) for x in input().split()]

matrix = []
position = []
opponent_position = []
moves = 0
touched_opponent = 0

for i in range(rows):
    matrix.append(input().split())
    for j in range(columns):
        if matrix[i][j] == "B":
            position = [i, j]
        elif matrix[i][j] == "P":
            opponent_position.append((i, j))

mapper = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}

command = input()

while command != "Finish":
    r = position[0] + mapper[command][0]
    c = position[1] + mapper[command][1]
    position = [r, c]
    if is_inside(r, c, rows, columns):
        if matrix[r][c] == "P":
            touched_opponent += 1
            moves += 1
            matrix[r][c] = "B"
            r = position[0] - mapper[command][0]
            c = position[1] - mapper[command][1]
            matrix[r][c] = "-"
        elif matrix[r][c] == "O":
            r = position[0] - mapper[command][0]
            c = position[1] - mapper[command][1]
            position = [r, c]
        elif matrix[r][c] == "-":
            moves += 1
            matrix[r][c] = "B"
            r = position[0] - mapper[command][0]
            c = position[1] - mapper[command][1]
            matrix[r][c] = "-"
    else:
        r = position[0] - mapper[command][0]
        c = position[1] - mapper[command][1]
        position = [r, c]
    command = input()

print(moves)
print(touched_opponent)
[print("".join(row)) for row in matrix]
