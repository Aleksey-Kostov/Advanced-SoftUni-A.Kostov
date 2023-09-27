m = int(input())
n_size_neighborhood = int(input())

matrix = []
position = []
firs_position = []
nice_kid = []
counter = 0

for i in range(n_size_neighborhood):
    matrix.append(input().split())
    for j in range(n_size_neighborhood):
        if matrix[i][j] == "S":
            position = [i, j]
            firs_position = [i, j]
        elif matrix[i][j] == "V":
            nice_kid.append([i, j])


directions_dict = {"left": [0, -1], "right": (0, 1), "up": (-1, 0), "down": (1, 0)}

while True:
    command = input()
    if command == "Christmas morning":
        break
    r = position[0] + directions_dict[command][0]
    c = position[1] + directions_dict[command][1]
    matrix[position[0]][position[1]] = "-"
    position[0] = r
    position[1] = c
    if 0 <= r < n_size_neighborhood and 0 <= c < n_size_neighborhood:
        if matrix[r][c] == "V":
            m -= 1
            matrix[r][c] = "S"
            counter += 1
        elif matrix[r][c] == "X":
            matrix[r][c] = "S"
        elif matrix[r][c] == "C":
            current_position = [r, c]
            matrix[r][c] = "S"
            current_r = current_position[0] + directions_dict["up"][0]
            current_c = current_position[1] + directions_dict["up"][1]
            if matrix[current_r][current_c] != "-":
                if matrix[current_r][current_c] == "V":
                    counter += 1
                m -= 1
                matrix[current_r][current_c] = "-"
                if m == 0:
                    break
            current_r = current_position[0] + directions_dict["down"][0]
            current_c = current_position[1] + directions_dict["down"][1]
            if matrix[current_r][current_c] != "-":
                if matrix[current_r][current_c] == "V":
                    counter += 1
                m -= 1
                matrix[current_r][current_c] = "-"
                if m == 0:
                    break
            current_r = current_position[0] + directions_dict["left"][0]
            current_c = current_position[1] + directions_dict["left"][1]
            if matrix[current_r][current_c] != "-":
                if matrix[current_r][current_c] == "V":
                    counter += 1
                m -= 1
                matrix[current_r][current_c] = "-"
                if m == 0:
                    break
            current_r = current_position[0] + directions_dict["right"][0]
            current_c = current_position[1] + directions_dict["right"][1]
            if matrix[current_r][current_c] != "-":
                if matrix[current_r][current_c] == "V":
                    counter += 1
                m -= 1
                matrix[current_r][current_c] = "-"
                if m == 0:
                    break
        else:
            matrix[r][c] = 'S'
        if m == 0:
            break
    else:
        continue

if m == 0 and counter < len(nice_kid):
    print("Santa ran out of presents!")
[print(" ".join(x)) for x in matrix]
if counter == len(nice_kid):
    print(f"Good job, Santa! {counter} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kid) - counter} nice kid/s.")
