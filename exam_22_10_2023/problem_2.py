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


n = int(input())

matrix = []
position_ship = []
whirlpool_position = []
fish_caught = 0
ship_in_whirlpool = False

for i in range(n):
    matrix.append([x for x in input()])
    for j in range(n):
        if matrix[i][j] == "S":
            position_ship = [i, j]
        if matrix[i][j] == "W":
            whirlpool_position = [i, j]

mapper = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}

command = input()

while command != "collect the nets":
    r = position_ship[0] + mapper[command][0]
    c = position_ship[1] + mapper[command][1]
    # matrix[position_ship[0]][position_ship[1]] = "-"
    r, c = is_valid(r, c, n)
    # matrix[r][c] = "S"
    if matrix[r][c].isdigit():
        fish_caught += int(matrix[r][c])
        matrix[position_ship[0]][position_ship[1]] = "-"
        position_ship = [r, c]
        matrix[r][c] = "S"
    elif matrix[r][c] == "W":
        fish_caught = 0
        matrix[position_ship[0]][position_ship[1]] = "-"
        position_ship = [r, c]
        ship_in_whirlpool = True
        break
    elif matrix[r][c] == "-":
        matrix[position_ship[0]][position_ship[1]] = "-"
        position_ship = [r, c]
        matrix[r][c] = "S"
    command = input()

if ship_in_whirlpool:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
          f" Last coordinates of the ship: [{','.join(map(str, position_ship))}]")
elif not ship_in_whirlpool and fish_caught < 20:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - fish_caught} tons of fish more.")
elif not ship_in_whirlpool and fish_caught >= 20:
    print(f"Success! You managed to reach the quota!")

if fish_caught > 0:
    print(f"Amount of fish caught: {fish_caught} tons.")
if not ship_in_whirlpool:
    [print("".join(row)) for row in matrix]
