ROWS = 6
COLS = 7


class FullColumnError(Exception):
    pass


def print_matrix(matrix):
    for row in matrix:
        print(row)


def is_valid_column_choice(selected_column_index):
    if 0 <= selected_column_index < COLS:
        return True
    return False


def place_player_number(column_index, matrix, player_number):
    for row_index in range(ROWS - 1, -1, -1):
        if matrix[row_index][column_index] == 0:
            matrix[row_index][column_index] = player_number
            return row_index, column_index
    else:
        raise FullColumnError


matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
print_matrix(matrix)

player = 1
while True:
    try:
        selected_column_number = int(input(f"Player {player}, please choose a column: "))
        selected_column_index = selected_column_number - 1
        if not is_valid_column_choice(selected_column_index):
            raise ValueError
        current_row, current_col = place_player_number(selected_column_index, matrix, player)
        print_matrix(matrix)
    except ValueError:
        print(f"Player {player}, please select number between 1 and {COLS}")
        continue
    except FullColumnError:
        print(f"Player {player}, this column is full, please select another one")
        continue

    player += 1
    player = 2 if player % 2 == 0 else 1
