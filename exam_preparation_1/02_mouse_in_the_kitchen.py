def matrix_is_valid(r, c, n):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False


row, cow = [int(x) for x in input().split(",")]

matrix = [[j for j in input()] for i in range(row)]

mapper = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
