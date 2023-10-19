def win_collected(current_sum):
    if current_sum in range(100, 200):
        collected = "Football"
        return collected
    elif current_sum in range(200, 300):
        collected = "Teddy Bear"
        return collected
    elif current_sum >= 300:
        collected = "Lego Construction Set"
        return collected


def move_col(coord, current_matrix):
    c = coord[1]
    sum_coll = 0
    for cow in range(6):
        if current_matrix[cow][c] != "B":
            sum_coll += int(current_matrix[cow][c])
    return sum_coll


n = 6

matrix = []
coord_b = []
total_sum = 0

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == "B":
            coord_b.append((i, j))

for _ in range(3):
    coordinates = input()
    new_coord = coordinates.strip("(").strip(")").split(", ")
    trans_coord = (int(new_coord[0]), int(new_coord[1]))
    if trans_coord not in coord_b:
        continue
    else:
        total_sum += move_col(trans_coord, matrix)
        coord_b.remove(trans_coord)

if total_sum < 100:
    print(f"Sorry! You need {100 - total_sum} points more to win a prize.")
else:
    print(f"Good job! You scored {total_sum} points, and you've won {win_collected(total_sum)}.")
