with open("test.txt") as f:
    for row, line in enumerate(f.readlines()):
        if row % 2 == 0:
            for char in "-,.!?":
                line = line.replace(char, "@")
            print(" ".join(line.split()[::-1]))
