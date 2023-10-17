size_matrix = int(input())
number_car = input()

matrix = []
position = [0, 0]
range_km = 0
tunel_position = []

for i in range(size_matrix):
    matrix.append(input().split())
    for j in range(size_matrix):
        if matrix[i][j] == "T":
            tunel_position.append((i, j))

mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()
    if command == "End":
        matrix[position[0]][position[1]] = "C"
        break
    r = position[0] + mapper[command][0]
    c = position[1] + mapper[command][1]
    position = (r, c)
    if matrix[r][c] == ".":
        range_km += 10
    elif matrix[r][c] == "T":
        matrix[r][c] = "."
        tunel_position.remove((r, c))
        position = tunel_position[0]
        matrix[position[0]][position[1]] = "."
        range_km += 30
    elif matrix[r][c] == "F":
        range_km += 10
        matrix[r][c] = "C"
        break

print(range_km)
[print(" ".join(row)) for row in matrix]
