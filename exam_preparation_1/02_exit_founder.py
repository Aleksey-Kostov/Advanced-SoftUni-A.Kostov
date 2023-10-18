player_1, player_2 = input(). split(", ")

N = 6
matrix = []
exit_coord = []
trap_coord = []
wall_coord = []
counter = 0
player_1_wall = False
player_2_wall = False


for i in range(N):
    matrix.append(input().split(" "))
    for j in range(N):
        if matrix[i][j] == "E":
            exit_coord.append((i, j))
        elif matrix[i][j] == "T":
            trap_coord.append((i, j))
        elif matrix[i][j] == "W":
            wall_coord.append((i, j))


coord = input()
while coord:
    current_coord = []
    for i in coord:
        if i.isdigit():
            current_coord.append(i)
    coord = (int(current_coord[0]), int(current_coord[1]))
    counter += 1
    if coord in exit_coord:
        if counter % 2 == 0 and not player_2_wall:
            print(f"{player_2} found the Exit and wins the game!")
            break
        elif counter % 2 == 0 and player_2_wall:
            player_2_wall = False
        elif counter % 2 != 0 and not player_1_wall:
            print(f"{player_1} found the Exit and wins the game!")
            break
        elif counter % 2 != 0 and player_1_wall:
            player_1_wall = False
    elif coord in trap_coord:
        if counter % 2 == 0 and not player_2_wall:
            print(f"{player_2} is out of the game! The winner is {player_1}.")
            break
        elif counter % 2 == 0 and player_2_wall:
            player_2_wall = False
        elif counter % 2 != 0 and not player_1_wall:
            print(f"{player_1} is out of the game! The winner is {player_2}.")
            break
        elif counter % 2 != 0 and player_1_wall:
            player_1_wall = False
    elif coord in wall_coord:
        if counter % 2 == 0 and not player_2_wall:
            print(f"{player_2} hits a wall and needs to rest.")
            player_2_wall = True
        elif counter % 2 == 0 and player_2_wall:
            player_2_wall = False
        elif counter % 2 != 0 and not player_1_wall:
            print(f"{player_1} hits a wall and needs to rest.")
            player_1_wall = True
        elif counter % 2 != 0 and player_1_wall:
            player_1_wall = False
    else:
        if counter % 2 != 0 and player_1_wall:
            player_1_wall = False
        elif counter % 2 == 0 and player_2_wall:
            player_2_wall = False
    coord = input()
