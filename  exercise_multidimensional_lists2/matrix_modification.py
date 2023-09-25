rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    row, coll, value = int(command[1]), int(command[2]), int(command[3])
    if row < 0 or row >= rows or coll < 0 or coll >= rows:
        print("Invalid coordinates")
        continue
    if command[0] == "Add":
        matrix[row][coll] += value
    elif command[0] == "Subtract":
        matrix[row][coll] -= value

for row in matrix:
    print(*row, sep=" ")
