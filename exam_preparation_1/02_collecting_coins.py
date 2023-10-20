from math import floor

n = int(input())

matrix = []
coord_wall = []
coord_position = []
total_coins = 0
collection_coord = []


def move(position, commands):
    mapper = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
    r = position[0] + mapper[commands][0]
    c = position[1] + mapper[commands][1]
    return r, c


def is_valid(current_r, current_c, size):
    if size > current_r >= 0 > current_c or current_c >= size:
        coord = [current_r, size - abs(current_c)]
        return coord
    elif size > current_c >= 0 > current_r or current_r >= size:
        coord = [size - abs(current_r), current_c]
        return coord
    elif 0 <= current_r < size and 0 <= current_c < size:
        coord = [current_r, current_c]
        return coord


for row in range(n):
    matrix.append(input().split())
    for coll in range(n):
        if matrix[row][coll] == "X":
            coord_wall.append((row, coll))
        elif matrix[row][coll] == "P":
            coord_position = [row, coll]
            collection_coord.append(coord_position)
            matrix[row][coll] = "0"


while total_coins < 100:
    command = input()
    if command not in ["up", "down", "left", "right"]:
        continue
    current_row, current_col = move(coord_position, command)
    coord_position = is_valid(current_row, current_col, n)
    row_m = coord_position[0]
    coll_m = coord_position[1]
    collection_coord.append([row_m, coll_m])
    if matrix[row_m][coll_m] == "X":
        total_coins /= 2
        total_coins = floor(total_coins)
        break
    else:
        total_coins += int(matrix[row_m][coll_m])
        matrix[row_m][coll_m] = "0"

if total_coins < 100:
    print(f"Game over! You've collected {total_coins} coins.")
else:
    print(f"You won! You've collected {total_coins} coins.")

print("Your path:")
for i in collection_coord:
    print(i)
