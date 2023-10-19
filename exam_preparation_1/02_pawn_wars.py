n = 8
matrix = []
coord_w = []
coord_b = []
win_white = False
win_black = False
counter = 0
chessboard_matrix = [[chr(97 + j) + str(n - i) for j in range(n)] for i in range(n)]

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == "w":
            coord_w.append((i, j))
        elif matrix[i][j] == "b":
            coord_b.append((i, j))

mapper_white = [(-1, -1), (-1, 1)]
mapper_black = [(1, 1), (1, -1)]

# mapper = [(0, -1), (-1, -1), (0, 1), (1, 1), (1, 0), (1, -1), (-1, 0), (-1, 1)]


def move_black(coord_black, black_mapper,  matrix_input, matrix_chess, size):
    for current_move in black_mapper:
        c_b = coord_black[0][1] + current_move[1]
        r_b = coord_black[0][0] + current_move[0]
        if not 0 <= c_b < size or not 0 <= r_b < size:
            continue
        if matrix_input[r_b][c_b] == "w":
            return f"Game over! Black win, capture on {matrix_chess[r_b][c_b]}."
    return False


def move_white(coord_white, white_maper, matrix_input, matrix_chess, size):
    for current_move in white_maper:
        r_w = coord_white[0][0] + current_move[0]
        c_w = coord_white[0][1] + current_move[1]
        if not 0 <= r_w < size or not 0 <= c_w < size:
            continue
        if matrix_input[r_w][c_w] == "b":
            return f"Game over! White win, capture on {matrix_chess[r_w][c_w]}."
    return False


for i in range(n + n):
    counter += 1
    if not move_white(coord_w, mapper_white, matrix, chessboard_matrix, n):
        if counter % 2 != 0:
            if coord_w[0][0] == 0:
                win_white = True
                break
            r_white = coord_w[0][0] - 1
            c_white = coord_w[0][1]
            if 0 <= r_white < n and 0 <= c_white < n:
                matrix[r_white][c_white] = "w"
                matrix[coord_w[0][0]][coord_w[0][1]] = "-"
                coord_w = [(r_white, c_white)]
                if r_white == 0:
                    win_white = True
                    break
    else:
        print(move_white(coord_w, mapper_white, matrix, chessboard_matrix, n))
        break
    if not move_black(coord_b, mapper_black, matrix, chessboard_matrix, n):
        if counter % 2 == 0:
            if coord_b[0][0] == 7:
                win_black = True
                break
            c_black = coord_b[0][1]
            r_black = coord_b[0][0] + 1
            if 0 <= r_black < n and 0 <= c_black < n:
                matrix[r_black][c_black] = "w"
                matrix[coord_b[0][0]][coord_b[0][1]] = "-"
                coord_b = [(r_black, c_black)]
                if r_black == 7:
                    win_black = True
                    break
    else:
        print(move_black(coord_b, mapper_black, matrix, chessboard_matrix, n))
        break

if win_white:
    print(f"Game over! White pawn is promoted to a queen at {chessboard_matrix[coord_w[0][0]][coord_w[0][1]]}.")
if win_black:
    print(f"Game over! Black pawn is promoted to a queen at {chessboard_matrix[coord_b[0][0]][coord_b[0][1]]}.")
