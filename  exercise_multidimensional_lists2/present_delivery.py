m = int(input())
n_size_neighborhood = int(input())

matrix = []
position = []
naughty_kid = []
nice_kid = []
cookie = []

for i in range(n_size_neighborhood):
    matrix.append(input().split())
    for j in range(n_size_neighborhood):
        if matrix[i][j] == "S":
            position = [i, j]
        elif matrix[i][j] == "":
            naughty_kid.append([i, j])
        elif matrix[i][j] == "V":
            nice_kid.append([i, j])
        elif matrix[i][j] == "C":
            cookie.append([i, j])

directions_dict = {"left": [0, -1], "right": (0, 1), "up": (-1, 0), "down": (1, 0)}

