from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

data = {150: "Doll",
        250: "Wooden train",
        300: "Teddy bear",
        400: "Bicycle"}

while materials or magic:
    first_magic = magic.popleft()
    last_materials = materials.pop()
    current_data = first_magic * last_materials
    if current_data in data:
        continue
    else:
        pass
    if current_data < 0:
        current_data = first_magic + last_materials
        materials.append(current_data)

x = 5