from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

data = {150: "Doll",
        250: "Wooden train",
        300: "Teddy bear",
        400: "Bicycle"}

product_dict = {}

while materials and magic:
    counter = 0
    first_magic = magic.popleft()
    last_materials = materials.pop()
    current_data = first_magic * last_materials
    if first_magic == 0 and last_materials == 0:
        continue
    elif first_magic == 0:
        materials.append(last_materials)
    elif last_materials == 0:
        magic.appendleft(first_magic)
    if current_data in data:
        counter += 1
        if data[current_data][::] not in product_dict:
            product_dict[data[current_data][::]] = counter
        else:
            product_dict[data[current_data][::]] += counter
        continue
    elif current_data > 0:
        materials.append(last_materials + 15)
    elif current_data < 0:
        current_data = first_magic + last_materials
        materials.append(current_data)

if (("Doll" in product_dict and "Wooden train" in product_dict) or
        ("Teddy bear" in product_dict and "Bicycle" in product_dict)):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(material) for material in materials[::-1]])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
for key, value in product_dict.items():
    print(f"{key}: {value}")
