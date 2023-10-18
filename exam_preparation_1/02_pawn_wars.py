n = 8
matrix = []
coord_w = []
coord_b = []
chessboard_matrix = [[chr(97 + j) + str(n - i) for j in range(n)] for i in range(n)]

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == "w":
            coord_w.append((i, j))
        elif matrix[i][j] == "b":
            coord_b.append((i, j))

mapper = [(0, -1), (-1, -1), (0, 1), (1, 1), (1, 0), (1, -1), (-1, 0), (-1, 1)]


def move(coord_white, coord_black, current_maper, matrix_input, matrix_chess):
    white_win = False
    black_win = False
    for current_move in current_maper:
        r_w = coord_white[0][0] + current_move[0]
        r_b = coord_black[0][0] + current_move[0]
        c_w = coord_white[0][1] + current_move[1]
        c_b = coord_white[0][1] + current_move[1]
        if matrix_input[r_w][c_w] == "b":
            return f"Game over! White win, capture on {matrix_chess[r_w][c_w]}."
        if matrix_input[r_b][c_b] == "w":
            return f"Game over! Black win, capture on {matrix_chess[r_b][c_b]}."
    return False


for i in range(n):
    if not move(coord_w, coord_b, mapper, matrix, chessboard_matrix):
        r_white = coord_w[0][0] + 0
        r_black = coord_b[0][0] + 0
        c_white = coord_w[0][1] + 1
        c_black = coord_w[0][1] - 1
        coord_w = [(r_white, c_white)]
        coord_b = [(r_black, c_black)]



print(move(coord_w, coord_b, mapper, matrix, chessboard_matrix))
